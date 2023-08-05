import platform
import sys

from setuptools import find_packages, setup

import versioneer

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


def tf_version():
    if sys.platform == "darwin" and platform.machine() == "arm64":
        return "tensorflow-macos==2.9.1"
    elif sys.platform == "darwin" and platform.machine() == "x86_64":
        return "tensorflow==2.9.1"
    elif sys.platform == "linux" and platform.machine() == "x86_64":
        return "tensorflow==2.9.1"
    elif sys.platform == "linux" and platform.machine() == "aarch64":
        return "tensorflow-aarch64==2.9.1"
    return "tensorflow==2.9.1"


setup(
    name="smart_app_framework",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Salute-Developers",
    description="SmartApp Framework — это фреймворк, "
                "который позволяет создавать смартапы "
                "с поддержкой виртуальных ассистентов Салют.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=[
        "aiohttp==3.7.4",
        "aioredis==2.0.0",
        "boto==2.49.0",
        "confluent_kafka==1.7.0",
        "croniter",
        "dawg==0.8.0",
        "dill==0.3.3",
        "ics==0.6",
        "Jinja2==3.0.3",
        "keras==2.9.0",
        "lazy",
        "nltk==3.5",
        "numpy",
        "objgraph==3.4.1",
        "prometheus-client==0.7.1",
        "psutil==5.8.0",
        "pyignite==0.5.2",
        "pymorphy2==0.8",
        "pymorphy2_dicts==2.4.393442.3710985",
        "python-dateutil==2.7.3",
        "python-json-logger==0.1.11",
        "PyYAML==5.3",
        "redis",
        "requests==2.22.0",
        "rusenttokenize==0.0.5",
        "scikit-learn==1.1.1",
        "setuptools",
        "tabulate",
        "tatsu==4.4.0",
        tf_version(),
        "timeout-decorator==0.4.1",
        "tqdm",
        "Twisted",
        "freezegun==1.1.0",
        "protobuf<4.21.0"  # https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9"
    ]
)
