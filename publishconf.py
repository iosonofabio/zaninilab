#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# NOTE: THIS CONFIG FILE ONLY APPLIES TO PRODUCTION
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
# Import config for local development and overwrite a bunch of things
from pelicanconf import *

#SITEURL = 'http://www.fabilab.org'
SITEURL = 'https://iosonofabio.github.io/zaninilab'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
