import setuptools

name = "urld"

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = "{}/version.py".format(name)
with open(version_file) as fi:
    vs = {}
    exec(fi.read(), vs)
    __version__ = vs["__version__"]

setuptools.setup(
    name=name,
    version=__version__,
    author="Eloy Perez",
    author_email="zer1t0ps@protonmail.com",
    description="Descompose URL in parts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Zer1t0/" + name,
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "urld = urld.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
