# Tableau Dashboard Newsfeed
![Tableau Newsfeed](docs/imgs/README-header.png?raw=true "Title")

A Python web server for embedding custom newsfeed within a Tableau Dashboard that can be customized in several ways, including parameters in tableau.

## 1. Get API Key
To get news from the News API you will need to first head on over to [NEWS API](https://newsapi.org) to get a API Key which will be required to get articles.

Got your key? Great lets move on to setting up the server.

Open up terminal if on mac or command prompt if on Windows and enter the following.
```bash
# Windows users use 'set', Mac Users use 'export'
set NEWS_API_KEY='YOUR_API_KEY'
set FLASK_APP=server.py

flask run

```

## 2. Open Tableau