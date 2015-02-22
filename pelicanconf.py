#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yo Gis'
SITENAME = u'Yo Gis'
SITEURL = 'http://yogis.alwaysdata.net'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'


PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'pelican.plugins.sitemap',]

LOAD_CONTENT_CACHE = False

THEME = "pure-single-yo"
# uncomment for pure single theme
COVER_IMG_URL = '/../../images/font2.jpg'
PROFILE_IMG_URL = '/../../images/yogis_stamp_black_little.jpg'
TAGLINE = 'Geomatic, Image & Sound'
#FAVICON_URL - Set the favicon image
#DISQUS_SITENAME - Set this to enable disqus comments in articles.
#DISQUS_ON_PAGES - Set this to True to enable disqus comments in pages.
#GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")
#PIWIK_URL and PIWIK_SITE_ID - Set the URL and site-id for Piwik tracking. (Without 'http://')
MENUITEMS = (('Geomatic', 'pages/project-manager-gis-administrator-and-spatial-analyst.html'),
('Image Sound Prod', 'pages/we-are-prod.html'),('Archives','archives.html'))

STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# sitemap plugin config
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Blogroll
#LINKS = ((,),(,))

# Social widget
SOCIAL = (('soundcloud', 'https://soundcloud.com/yogis-record'),
          ('youtube', 'https://www.youtube.com/channel/UCK6L4K87OB9cQMdMZRnz5hg'),
		  ('map-marker','https://www.openstreetmap.org/user/goym@p/history'),
		  ('github-square','https://github.com/yougis'))

DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
