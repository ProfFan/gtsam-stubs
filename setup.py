from setuptools import setup
import os
from os import path


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gtsam-stubs",
    maintainer="Fan Jiang",
    maintainer_email="gtsam@example.com",
    description="PEP 561 type stubs for GTSAM",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="http://www.gtsam.org",
    license="BSD",
    version="0.0.2",
    packages=["gtsam-stubs"],
    # PEP 561 requires these
    install_requires=[
        "gtsam>=4.0.3",
        'typing_extensions>=3.7.4; python_version>="3.8"',
    ],
    package_data=find_stubs("gtsam-stubs"),
    zip_safe=False,
)
