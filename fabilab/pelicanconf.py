#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = 'Fabio Zanini'
SITENAME = 'fabilab'
SITEURL = 'http://fabilab.org'
TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = 'en'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican_javascript']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/fabiousername'),
          ('github', 'https://github.com/iosonofabio'),
          )

THEME = 'themes/pelican-blue'
DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
LOAD_CONTENT_CACHE = False
TYPOGRIFY = True
PAGE_ORDER_BY = 'order'
AVATAR = '/images/logo2.png'
SUBLOGO = 'Data driven biomedicine<br>UNSW SYDNEY, AUSTRALIA'
SUMMARY_MAX_LENGTH = 0
INDEX_SAVE_AS = 'news.html'
FAVICON = '/images/favicon.ico'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
