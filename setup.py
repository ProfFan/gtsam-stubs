from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="gtsam-stubs",
    maintainer="Fan Jiang",
    maintainer_email="gtsam@example.com",
    description="PEP 561 type stubs for GTSAM",
    url="http://www.gtsam.org",
    license="BSD",
    version="0.0.1",
    packages=["gtsam-stubs"],
    # PEP 561 requires these
    install_requires=[
        "gtsam>=4.0.3",
        'typing_extensions>=3.7.4; python_version>="3.8"',
    ],
    package_data=find_stubs("gtsam-stubs"),
    zip_safe=False,
)
