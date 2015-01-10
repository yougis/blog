#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hugo Roussaffa'
SITENAME = u'Yo Gis'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

PLUGINS = [
    # ...
    'pelican_youtube',
    # ...
]

#THEME = "pure-single"
# uncomment for pure single theme
#COVER_IMG_URL - Set the sidebar image.
#PROFILE_IMG_URL - Set the image for the top circle cutout.
#TAGLINE - Used for the page titles and some meta tags.
#FAVICON_URL - Set the favicon image
#DISQUS_SITENAME - Set this to enable disqus comments in articles.
#DISQUS_ON_PAGES - Set this to True to enable disqus comments in pages.
#GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")
#PIWIK_URL and PIWIK_SITE_ID - Set the URL and site-id for Piwik tracking. (Without 'http://')


STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('YoGis Production', 'http://youtube.com/'),
         ('YoGis Record', 'https://soundcloud.com/yogis-record'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
