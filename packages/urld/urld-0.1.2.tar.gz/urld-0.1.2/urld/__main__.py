import argparse
from typing import Iterator, Any, Optional
import logging
import sys
from urllib.parse import urlparse, ParseResult, parse_qs
import os
from functools import partial

logger = logging.getLogger(__name__)


URL_FIELDS = [
    "scheme", "protocol", "proto",
    "netloc",
    "host", "hostname", "domain",
    "port",
    "path",
    "query",
    "fragment",
    "username", "user",
    "password", "pass",
    "extension", "ext",
    "url"
]

def parse_args():
    parser = argparse.ArgumentParser(
        description="Descompose URL in parts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
        "$ echo 'https://domain.com/index.html?a=b' | urld\n"
        "https domain.com /index.html a=b\n"
        "\n"
        "$ echo 'https://domain.com/index.html?a=b' | urld -f protocol host\n"
        "https domain.com\n"
        "\n"
        "$ echo 'https://domain.com/index.html?foo=bar' | urld -p foo\n"
        "bar"
        "\n"
        "$ echo 'https://domain.com/index.html?foo=bar' | urld -P \"{scheme}://{netloc}{path}\"\n"
        "https://domain.com/index.html"
    )

    parser.add_argument(
        "url",
        help="URL",
        nargs="*",
    )

    format_parser = parser.add_mutually_exclusive_group()

    format_parser.add_argument(
        "-f", "--fields",
        help="Parts to show of URL. The options are: %s." % URL_FIELDS,
        metavar="FIELD",
        nargs="+",
        choices=URL_FIELDS,
    )

    format_parser.add_argument(
        "-P", "--pattern",
        help="Format the URL with the given pattern.",
    )

    parser.add_argument(
        "-p", "--params",
        help="Params of URL to show.",
        nargs="+",
    )

    parser.add_argument(
        "-v",
        help="Verbose",
        dest="verbosity",
        action="count",
        default=0,
    )

    args = parser.parse_args()

    if not args.params:
        args.params = []

    if not args.fields:
        if args.params:
            args.fields = []
        else:
            args.fields = ["scheme", "netloc", "path", "query", "fragment"]

    for i, f in enumerate(args.fields):
        if f == "protocol":
            args.fields[i] = "scheme"

        elif f == "host":
            args.fields[i] = "hostname"

    return args


def main():
    args = parse_args()
    init_log(args.verbosity)

    logger.debug("URL Fields: %s", args.fields)
    logger.debug("URL Params: %s", args.params)
    logger.debug("URL Pattern: %s", args.pattern)

    if args.pattern:
        print_url = partial(print_url_pattern, args.pattern)
    else:
        print_url = partial(print_url_fields, args.fields, args.params)

    try:
        for url in read_text_targets(args.url):
            logger.info("URL: %s", url)
            print_url(urlparse(url))
    except KeyboardInterrupt:
        pass


def print_url_pattern(pattern, url):
    parts = {field: get_url_field(url, field) for field in URL_FIELDS}
    print(pattern.format(**parts), flush=True)

def print_url_fields(fields, params, url):
    parts = [get_url_field(url, field) for field in fields]
    params = [
        " ".join(get_url_param(url, param))
        for param in params
    ]

    parts.extend(params)

    line = " ".join(parts)
    if line.strip() != "":
        print(*parts, flush=True)


def init_log(verbosity=0, log_file=None):

    if verbosity == 1:
        level = logging.INFO
    elif verbosity > 1:
        level = logging.DEBUG
    else:
        level = logging.WARN

    logging.basicConfig(
        level=level,
        filename=log_file,
        format="%(levelname)s:%(name)s:%(message)s"
    )


def get_url_field(url_p: ParseResult, field: str) -> str:
    if field in ["scheme", "protocol", "proto"]:
        return url_p.scheme
    elif field in ["hostname", "host", "domain"]:
        return url_p.hostname or ''
    elif field == "port":
        return str(url_p.port) or ''
    elif field == "netloc":
        return url_p.netloc
    elif field == "path":
        return url_p.path
    elif field == "fragment":
        return url_p.fragment
    elif field == "query":
        return url_p.query
    elif field in ["username", "user"]:
        return url_p.username or ''
    elif field in ["password", "pass"]:
        return url_p.password or ''
    elif field in ["extension", "ext"]:
        return os.path.splitext(url_p.path)[1]
    elif field == "url":
        return url_p.geturl()

    raise KeyError(field)


def get_url_param(url_p: ParseResult, param: str) -> [str]:
    return parse_qs(url_p.query).get(param, [])


def read_text_targets(targets: Any) -> Iterator[str]:
    yield from read_text_lines(read_targets(targets))


def read_targets(targets: Optional[Any]) -> Iterator[str]:
    """Function to process the program ouput that allows to read an array
    of strings or lines of a file in a standard way. In case nothing is
    provided, input will be taken from stdin.
    """
    if not targets:
        yield from sys.stdin

    for target in targets:
        try:
            with open(target) as fi:
                yield from fi
        except FileNotFoundError:
            yield target


def read_text_lines(fd: Iterator[str]) -> Iterator[str]:
    """To read lines from a file and skip empty lines or those commented
    (starting by #)
    """
    for line in fd:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("#"):
            continue

        yield line


if __name__ == '__main__':
    main()
