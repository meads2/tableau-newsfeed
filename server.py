from flask import Flask, render_template
import requests as r
import os
from endpoints.getNews import getArticles
from datetime import datetime

# Create App Instance
app = Flask(__name__)


# Create Index Route
@app.route('/')
def index():
    return 'App is up and working!'

# Create News Route
@app.route('/news/<topic>')
def handler(topic):
    '''
    Handles a news request for a certain topic
    from the news api
    
    URL Params:
    @topic string (Required) | The topic of news you would like
    '''
    # Get Articles From API
    articles = getArticles(topic=topic)
        
    # Date
    date = str(datetime.strftime(datetime.now(), '%B %-d, %Y'))

    # Render Template
    return render_template('index.html', date=date, topic=topic, articles=articles)

'''
All news articles are attributed to:
    NewsAPI.org
'''

@app.route('/tweets')
def tweets():
    return 'This page will eventually get tweets!'


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)