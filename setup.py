import os
from spammer import __version__
from setuptools import setup, find_packages, Extension


def get_packages():
    """ """
    return [ *filter(lambda x: x!="tests", find_packages()) ]

def get_requirements():
    with open("requirements.txt", 'r', encoding='utf-8') as f:
        requirements = [x.strip() for x in f if x.strip()]
    return [ *filter(lambda x: x!='pytest', requirements) ]

def get_long_description():
    with open("readme.md", "r") as f:
        readme = f.read() 
    return readme

rootdir = os.path.normpath(os.path.join(__file__, os.pardir))

setup(
    name="spammer",
    version=__version__,
    description="module for testing c extentions",
    long_description=get_long_description(),
    author="gurpgork",
    author_email="gurp@gork.com",
    url="www.gurpgork.com",
    license="MIT",
    python_requires=">3.6.4"
    packages=get_packages(),
    install_requires=get_requirements(),
    ext_modules=[
        Extension(
            "_hello", 
            sources=[*map(lambda x: os.path.join(rootdir, x), ["spammer/hello/bind.c", "spammer/hello/libhello.c"])]
        )
    ],
    package_data={'': ['*.h', '*.c']},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Topic :: Software Development :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python 3.9"
    ]
)
