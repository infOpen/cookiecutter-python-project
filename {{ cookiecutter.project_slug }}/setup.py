#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

try:
    from sphinx.setup_command import BuildDoc
    doc_cmdclass = {'doc': BuildDoc}
except ImportError:
    print('WARNING - No documentation can be managed before Sphinx installed')
    doc_cmdclass = {}


# Command classes
cmdclass = doc_cmdclass


# Setup function, settings are in setup.cfg
setup(cmdclass=cmdclass)
