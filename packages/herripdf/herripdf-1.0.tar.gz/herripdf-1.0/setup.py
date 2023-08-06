from gettext import find
from pathlib import Path
import pathlib
import setuptools
from pathlib import Path

setuptools.setup(
    name="herripdf",
    version=1.0,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
