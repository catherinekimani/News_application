from distutils.command.config import config
from turtle import back, title
from unicodedata import category
import urllib.request,json
from .models import Source,Articles #importing source class and articles class


# getting api key
api_key = None

# getting the news source url
base_url = None

# getting the articles url
articles_url = None

def configure_request(app):
    global api_key,base_url
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
            source_results = process_results(source_results_list)
            
    return source_results
        
def process_results(source_list):
    '''
    Function that processes the source result and transform them to a list of objects
        Args:
            source_list: List of dictionaries that contain source details
        Returns:
            source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url_path')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        
        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)
            
    return source_results

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(id,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None
    
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)
            
    return articles_results

def process_results(articles_list):
    '''
    Function that processes the articles result and transform them to a list of objects
        Args:
            articles_list: List of dictionaries that contain articles details
        Returns:
            articles_results: A list of artcicles objects
    '''
    articles_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishesAt')
        content = article_item.get('content')
        
        if urlToImage:
            articles_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results