import os
import requests as r


def getArticles(topic='bitcoin', limit=5):
    '''
    Creates a API request to get articles on a certain 
    topic provided by URL.

    Params:
    @topic string (required): The topic you would like news on
    @limit integer : The number of articles you would like to receive
    '''

    # Get News API KEY & Add To Header
    headers = {'X-API-KEY': os.environ['NEWS_API_KEY']}
    # API URL
    api_url = 'https://newsapi.org/v2/top-headlines?q='
    # Makes Request
    data = r.get(api_url + topic, headers=headers).json()
    # Limit Data
    data = data['articles'][:limit]
    # Return Data
    return data
