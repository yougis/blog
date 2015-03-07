blog de Yo Gis
====
http://yogis.alwaysdata.net


hebergeur alwaysdata : Pack gratuit (10 Mo) 
Python : 2.7 
Pelican : 3.5

Automatisation des déploiements desktop -> git -> alwaysdata


````sh
cd projects/
git clone git://github.com/yougis/blog.git
git clone git://github.com/yougis/pure-single-yo.git
git clone git://github.com/yougis/flickr.git

git clone git://github.com/getpelican/pelican-plugins.git
cd pelican-plugins
git clone git://github.com/La0/pelican-flickr.git
cd pelican-flickr
sudo python setup.py install

mkvirtualenv envpelican
workon envpelican


pip install pelican

pip install markdown

pip install pelican-flickrs

pelican-themes --install pure-single-yo
````sh

need plugins :
- pelican-flickr
- liquid_tags
- sitemap

pelcan-themes install pure-sigle-yo