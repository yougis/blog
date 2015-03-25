#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yo Gis'
SITENAME = u'Yo Gis'
SITEURL = 'http://yogis.alwaysdata.net'

PATH = 'content'

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = u'fr'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
    'fr': '%d %m %Y'}

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'sitemap',
          # 'pelican-flickr',
           ]

LOAD_CONTENT_CACHE = False

THEME = "pure-single-yo"
EXTRA_TEMPLATES_PATHS = ['../pelican-themes/flickr/',]

DEFAULT_LANG = 'fr'

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

COVER_IMG_URL = '/../../images/font2.jpg'
PROFILE_IMG_URL = '/../../images/yogis_stamp_black_little.jpg'
TAGLINE = 'Geomatic, Image & Sound'
#FAVICON_URL - Set the favicon image
DISQUS_SITENAME = "yogis"
DISQUS_ON_PAGES = True
#GOOGLE_ANALYTICS - Set the Google Analytics code (eg. "UA-000000-00")
#PIWIK_URL and PIWIK_SITE_ID - Set the URL and site-id for Piwik tracking. (Without 'http://')
MENUITEMS = (('Geomatic', 'pages/project-manager-gis-administrator-and-spatial-analyst.html'),
('Image Sound Prod', 'pages/we-are-prod.html'),('Claire Cousergue', 'pages/claire-cousergue-camerawoman-location-manager.html'),('Gallery', 'pages/my-albums.html'),('Archives','archives.html'))

STATIC_PATHS = ['images']

#  generation is usually not desired when developing
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

PDF_GENERATOR = False

FLICKR_API_KEY = '51b43627304c37e85055ba4235ffe9dd'
FLICKR_API_SECRET = '5f49bbdfc0b7e732'
FLICKR_USER = '131609124@N08'


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
