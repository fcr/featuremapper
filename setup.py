#!/usr/bin/env python

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup_args = {}

#############################################################################################
##### CEBALERT: copied from topographica; should be simplified

required = {'param':">=0.0.1",
            'imagen':">=1.0",
            'numpy':">=1.0"}

# optional = {}

packages_to_install = [required]
packages_to_state = [required]

setup_args = {}

if 'setuptools' in sys.modules:
    # support easy_install without depending on setuptools
    install_requires = []
    for package_list in packages_to_install:
        install_requires+=["%s%s"%(package,version) for package,version in package_list.items()]
    setup_args['install_requires']=install_requires
    setup_args['dependency_links']=["http://pypi.python.org/simple/"]
    setup_args['zip_safe']=False # CEBALERT: probably ok for imagen; haven't checked

for package_list in packages_to_state:
    requires = []
    requires+=["%s (%s)"%(package,version) for package,version in package_list.items()]
    setup_args['requires']=requires

#############################################################################################


setup_args.update(dict(
    name='FeatureMapper',
    version="0.2.1",
    description='FeatureMapper coordinates the presentation of input patterns, collating and analysing the responses.',
    long_description=open('README.rst').read(),
    author= "IOAM",
    author_email= "developers@topographica.org",
    maintainer= "IOAM",
    maintainer_email= "developers@topographica.org",
    platforms=['Windows', 'Mac OS X', 'Linux'],
    license='BSD',
    url='http://ioam.github.com/featuremapper/',
    packages = ["featuremapper",
                "featuremapper.analysis"],
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries"]
))


if __name__=="__main__":

    if 'upload' in sys.argv:
        import featuremapper
        featuremapper.__version__.verify(setup_args['version'])

    setup(**setup_args)
