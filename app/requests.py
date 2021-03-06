from distutils.command.config import config
from turtle import back, title
from unicodedata import category
import urllib.request,json
from .models import Source
from .models import Articles #importing source class and articles class


# getting api key
api_key = None

# getting the news source url
base_url = None

# getting the articles url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_BASE_URL']
    
def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_news_results(source_results_list)
    return source_results

def process_news_results(source_lists):
    '''
    Function that processes the source result and transform them to a list of objects
        Args:
            source_list: List of dictionaries that contain source details
        Returns:
            source_results: A list of source objects
    '''

    source_results = []
    for source_item in source_lists:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)


    return source_results

def get_articles():
    '''
    Function that gets the json response from our url request
    and returns all articles
    '''
    get_articles_url = articles_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None
        
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

    return articles_results

def process_articles_results(articles_lists):
    '''
    Function that processes the articles result and transform them to a list of objects
        Args:
            articles_list: List of dictionaries that contain articles details
        Returns:
            articles_results: A list of artcicles objects
    '''
    articles_results = []
    for articles_item in articles_lists:
        id = articles_item.get('id')
        name = articles_item.get('name')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')
        
        if urlToImage:
            articles_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results