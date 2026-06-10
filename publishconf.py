# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://ngjunsiang.github.io/laymansguide"
RELATIVE_URLS = False

# CSS path will be resolved relative to SITEURL by the template
STYLESHEET_URL = "theme/css/style.css"

# Apply typographical improvements
TYPOGRIFY = True

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""