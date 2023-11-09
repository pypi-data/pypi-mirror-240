import glob
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read()

setup(
    name="phalcon",
    version="1.0.10.11",
    author_email="mreyeswilson@gmail.com",
    author="Wilson Mendoza",
    packages=find_packages().extend("data"),
    install_requires=[requirements],
    include_package_data=True,
    package_data={
        "data": glob.glob("data/**/*", recursive=True),
    },
    entry_points="""
        [console_scripts]
        phalcon=app.main:cli
    """,
    description="Command Line Interface for phalcon dev env"
)