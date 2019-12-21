from setuptools import setup

PACKAGE_NAME = "ais2gpd"


def find_version(path):
    import re

    # path shall be a plain ascii text file.
    s = open(path, "rt").read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", s, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Version not found")


setup(
    name=PACKAGE_NAME,
    version=find_version(f"{PACKAGE_NAME}/__init__.py"),
    author="Nick Hand",
    maintainer="Nick Hand",
    maintainer_email="nick.hand@phila.gov",
    description="A Python utility to query the City of Philadelphia's Address Information System (AIS)",
    license="MIT",
    python_requires=">=3.6",
)
