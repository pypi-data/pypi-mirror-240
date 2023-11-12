import re
from sys import argv

import setuptools



with open("requirements.txt", encoding="utf-8") as r:
    requirements = [i.strip() for i in r]

# requirements = ["redis", "hiredis", "python-decouple", "python-dotenv", "setuptools"]

with open("jawir/__init__.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("jawir/__init__.py", "rt", encoding="utf8") as x:
    license = re.search(r'__license__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


name = "jawir"
author = "jawirTeam"
author_email = "jawirteam@gmail.com"
description = "jawir - Telegram MTProto API Client Library for Python."
url = "https://github.com/jawirTeam/jawir"
project_urls = {
    "Bug Tracker": "https://github.com/jawirTeam/jawir/issues",
    "Documentation": "https://jawirteam.tech",
    "Source Code": "https://github.com/jawirTeam/jawir",
}
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    project_urls=project_urls,
    license=license,
    package_data={
        "jawir": ["py.typed"],
    },
    install_requires=requirements,
    classifiers=classifiers,
    python_requires="~=3.7",
    zip_safe=False,
)
