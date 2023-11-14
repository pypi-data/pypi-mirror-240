import os
import re
from typing import Any, Match, cast
from setuptools import find_packages, setup


DEFAULT_PACKAGE_NAME = "gega_promptflow_vectordb"


def get_long_description() -> str:
    with open("README.md", "r") as fh:
        return fh.read()


def get_package_name() -> str:
    if os.path.exists("package_name.txt"):
        with open("package_name.txt", "r") as f:
            return f.read().strip()
    else:
        return DEFAULT_PACKAGE_NAME


def get_version(package_folder_path: str) -> str:
    # Version extraction inspired from 'requests'
    with open(os.path.join(package_folder_path, "_version.py"), "r") as fd:
        version = cast(
            Match[Any],
            re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE)
        ).group(1)
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def get_package_data_list(package_name: str) -> list:
    if package_name == DEFAULT_PACKAGE_NAME:
        return [
            "tool/yamls/*.yaml",
            "tool/yamls/**/*.yaml"
        ]
    else:
        return []


package_name = get_package_name()


setup(
    # Here is the module name.
    name=package_name,

    # version of the module
    version="0.0.1",

    # Name of Author
    author="Microsoft Corporation",

    # your Email address
    author_email="aethercn@microsoft.com",

    # #Small Description about module
    description="Prompt flow tools for accessing popular vector databases",

    # long_description=long_description,

    # Specifying that we are using markdown file for description
    long_description=get_long_description(),
    long_description_content_type="text/markdown",

    # Any link to reach this module, ***if*** you have any webpage or github profile
    # url="https://github.com/username/",
    packages=find_packages(include=[package_name, f"{package_name}.*"]),
    entry_points={
        "console_scripts": [f"{package_name}_service = {package_name}.service.server.rest.app:main"],
        "package_tools": [f"{package_name}_tools = {package_name}.tool.tools_manager:list_package_tools"]
    },

    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package

    install_requires=[
        "psutil",
        "faiss.cpu>=1.7.3",
        "numpy>=1.24.1",
        "pandas>=1.5.3",
        "langchain>=0.0.123",
        "openai>=0.27.0",
        "flask>=2.2.3",
        "requests>=2.28.1"
    ],
    extras_require={
        "azure": [
            "azure.identity>=1.12.0",
            "azure.keyvault>=4.2.0",
            "azure.storage.blob>=12.13.0",
            "azure.core>=1.26.3",
            "azure.ai.ml>=1.5.0",
            "azureml.rag>=0.2.18",
            "opencensus.ext.azure>=1.1.9"
        ]
    },

    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License"
    ],
    package_data={
        package_name: get_package_data_list(package_name)
    }
)
