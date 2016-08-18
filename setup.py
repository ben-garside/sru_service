"""
SRU Service
Special Reconnaissance Unit
-----------
python SRU Service
Link
`````
* Source
  https://github.com/abusaidm/
"""
from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="sru_service",
    version=version,
    author="Mohamed Abusaid",
    author_email="m.abusaid<at>yahoo<dot>com",
    packages=find_packages(),
    # package_data={"sru_service":['*.*', "sru_service/executable/*.*"]},
    include_package_data=True,
    url="http://github.com/abusaidm/sru_service/packages/{}/".format(version),

    # license="LICENSE.txt",
    description="sru_service",
    # long_description=open("README.txt").read() or just """ lots of text here too""",
    # Dependent packages (distributions)
    dependency_links=[
    ],
    install_requires=[
    ]
)