#!/usr/bin/env python3
from setuptools import setup, find_packages, Extension

setup(
	name="hello",
	version="0.0.1",
	ext_modules=[Extension("_hello", ["bind.c", "libhello.c"])]
);
