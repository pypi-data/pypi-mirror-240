import glob
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read()

setup(
    name="phalcon",
    version="1.0.10.33",
    author_email="mreyeswilson@gmail.com",
    author="Wilson Mendoza",
    packages=find_packages(),
    install_requires=[requirements],
    include_package_data=True,
    package_data={
        "phalcon_data": glob.glob("phalcon_data/**/*", recursive=True),
        "phalcon_data": ["phalcon_data/*"],
        "phalcon_data": ["phalcon_data/**/*"],
    },
    entry_points="""
        [console_scripts]
        phalcon=app.main:cli
    """,
    description="Command Line Interface for phalcon dev env"
)