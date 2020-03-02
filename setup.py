#!/usr/bin/python3
import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="regpy",
	version="1.0",
	description="Implement complex regex in simple way.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ankitdobhal/regpy",
	author="Ankit Dobhal",
	author_email="dobhal.ankit@protonmail.com",
	packages=setuptools.find_packages(),
	classifiers=[
	    "License :: OSI Approved :: MIT License",
	    "Programming Language :: Python :: 3.6",
	    "Programming Language :: Python :: 3.8",
	],
	python_requires='>=3.6',
)