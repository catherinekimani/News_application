from distutils.command.config import config
from turtle import back
from unicodedata import category
import urllib.request,json
from .models import Source #importing source class

# getting api key
api_key = None

# getting the news source url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    
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
        
    