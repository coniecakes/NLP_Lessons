# install nltk module
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
# #once the download dialog opens - download book and popular packages
# #also download punkt from Models tab
# #and averaged_perception_tagger also from Model tab
from nltk.book import *
#