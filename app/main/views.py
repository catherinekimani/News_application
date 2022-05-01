from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Welcome To Online Hot News'
    source = get_sources()
    
    return render_template('index.html',title = title,source= source)

@main.route('/articles<id>')
def articles(id):
    '''
    view articles page function that returns the articles objects and data'''
    articles = get_articles(id)
    
    return render_template('articles.html',articles=articles)