import urllib.request,json
from .models import Sources,Articles

# Getting api key
api_key = None
# Getting the news and article base url
news_url = None
article_url = None

def configure_request(app):
    global api_key,news_url,article_url
    api_key = app.config['NEWS_API_KEY']
    news_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']


