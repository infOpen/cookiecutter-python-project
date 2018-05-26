#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

try:
    from sphinx.setup_command import BuildDoc
    DOC_CMD_CLASS = {'doc': BuildDoc}
except ImportError:
    print('WARNING - No documentation can be managed before Sphinx installed')
    DOC_CMD_CLASS = {}


# Setup function, settings are in setup.cfg
setup(cmdclass=DOC_CMD_CLASS, version='{{ cookiecutter.version }}')
