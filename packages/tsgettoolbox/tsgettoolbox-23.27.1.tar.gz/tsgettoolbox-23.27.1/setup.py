# -*- coding: utf-8 -*-

import os
import shlex
import subprocess
import sys

from setuptools import find_packages, setup

# temporarily redirect config directory to prevent matplotlib importing
# testing that for writeable directory which results in sandbox error in
# certain easy_install versions
os.environ["MPLCONFIGDIR"] = "."

pkg_name = "tsgettoolbox"

version = open("VERSION").readline().strip()

if sys.argv[-1] == "publish":
    subprocess.run(shlex.split("cleanpy ."), check=True)
    subprocess.run(shlex.split("python setup.py sdist"), check=True)
    subprocess.run(
        shlex.split(f"twine upload dist/{pkg_name}-{version}.tar.gz"), check=True
    )
    sys.exit()

README = open("README.rst").read()

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    # "beautifulsoup4",  # needed if ever use local pydap
    # "cdo-api-py", # needed if ever use local ish_parser
    "appdirs",
    "geojson",
    "haversine",
    "isodate",
    "lxml",
    "mechanize",
    "requests",
    "siphon",
    "suds-community",
    "tstoolbox > 103.16.1",
    "zeep",
    "async_retriever",
    "cftime",
    "pydap",
    "pydaymet",
    "cdo_api_py",
]

extras_require = {
    "dev": [
        "black",
        "cleanpy",
        "twine",
        "pytest",
        "coverage",
        "flake8",
        "pytest-cov",
        "pytest-mpl",
        "pre-commit",
        "black-nbconvert",
        "blacken-docs",
        "velin",
        "isort",
        "pyroma",
        "pyupgrade",
        "commitizen",
    ]
}

setup(
    name=pkg_name,
    version=version,
    description="Will get time series from different sources on the internet.",
    long_description=README,
    classifiers=[
        # Get strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="time_series uri url web_services rest",
    author="Tim Cera, PE",
    author_email="tim@cerazone.net",
    url=f"http://timcera.bitbucket.io/{pkg_name}/docs/index.html",
    license="BSD",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={"console_scripts": [f"{pkg_name}={pkg_name}.{pkg_name}:main"]},
    test_suite="tests",
    python_requires=">=3.7.1",
)
