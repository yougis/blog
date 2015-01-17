#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hugo Roussaffa'
SITENAME = u'Yo Gis'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'


PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',]

LOAD_CONTENT_CACHE = False

THEME = "pure-single"
# uncomment for pure single theme
#COVER_IMG_URL - Set the sidebar image.
PROFILE_IMG_URL = '/../../images/yogis_stamp_black_little.jpg'
TAGLINE = geomatic, image and sound production
#FAVICON_URL - Set the favicon image
#DISQUS_SITENAME - Set this to enable disqus comments in articles.
#DISQUS_ON_PAGES - Set this to True to enable disqus comments in pages.
#GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")
#PIWIK_URL and PIWIK_SITE_ID - Set the URL and site-id for Piwik tracking. (Without 'http://')
MENUITEMS = (('About Geomatic', 'pages/about.html'),
         ('About IS Prod', 'pages/prod.html'),)

STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
#LINKS = ((,),(,))

# Social widget
SOCIAL = (('souncloud', 'https://soundcloud.com/yogis-record'),
          ('youtube', 'https://www.youtube.com/channel/UCK6L4K87OB9cQMdMZRnz5hg'),)

DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
