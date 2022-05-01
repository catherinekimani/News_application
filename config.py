from instance.config import NEWS_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = 'ffd927c5dc134723b1076da641194ccf'

class ProdConfig(Config):
    '''
    production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
    DEBUG = True
    
config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}