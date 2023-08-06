from setuptools import (setup, find_packages,)


setup(
    name = "balelib",
    version = "1.0.1",
    author = "Shayan Heidari",
    author_email = "snipe4kill.tg@gmail.com",
    install_requiers = ['requests'],
    description = "This is an almost official library for managing bots in bale Messenger...",
    long_description = "Loading...",
    long_description_content_type = "text/markdown",
    url = "https://github.com/snipe4kill/bale/",
    packages = find_packages(),
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)