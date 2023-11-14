from setuptools import setup, find_packages

VERSION = "0.1.1"
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
        "pypiwin32",
        "pycryptodome",
        "pyinstaller",
        "pillow",
        "requests",
        "numpy",
        "pyautogui",
    ],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
