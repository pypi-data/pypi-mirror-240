# Copyright DataStax, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
from os import path

from astrapy import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="astrapy",
    packages=[
        "astrapy",
    ],
    version=__version__,
    license="Apache license 2.0",
    description="AstraPy is a Pythonic SDK for DataStax Astra",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kirsten Hunter",
    author_email="kirsten.hunter@datastax.com",
    url="https://github.com/datastax/astrapy",
    keywords=["DataStax Astra", "Stargate"],
    python_requires=">=3.6",
    install_requires=[
        "faker~=19.11.0",
        "pytest~=7.4.2",
        "pytest-cov~=4.1.0",
        "pytest-testdox~=3.1.0",
        "httpx[http2]~=0.25.1",
        "python-dotenv~=1.0.0",
        "pre-commit~=3.5.0",
        "cassio~=0.1.3",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
