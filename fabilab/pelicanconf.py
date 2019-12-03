#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fabio Zanini'
SITENAME = 'fabilab'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/fabiousername'),
          ('github', 'https://github.com/iosonofabio'),
          )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_javascript']

#THEME = 'themes/simple'
#THEME = 'themes/nikhil-theme'
#THEME = 'themes/nmnlist'
THEME = 'themes/pelican-blue'
#THEME = 'themes/pelican-mockingbird'

DEFAULT_PAGINATION = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
LOAD_CONTENT_CACHE = False
TYPOGRIFY = False
PAGE_ORDER_BY = 'order'
