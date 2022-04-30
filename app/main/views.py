from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Welcome To Online Hot News'
    source = get_sources()
    description = get_sources()
    
    return render_template('index.html',title = title,source= source,description=description)