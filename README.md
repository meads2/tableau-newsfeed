# Tableau Dashboard Newsfeed
![Tableau Newsfeed](docs/imgs/README-header.png?raw=true "Title")

A Python web server for embedding custom newsfeed within a Tableau Dashboard that can be customized in several ways, including parameters in tableau.

In order for this to work make sure you have Python & Pip installed.

## 1. Get API Key
To get news from the News API you will need to first head on over to [NEWS API](https://newsapi.org) to get a API Key which will be required to get articles.

Got your key? Great lets move on to setting up the server.

Open up terminal if on mac or command prompt if on Windows and enter the following.
```bash
# Ensure PIP & PYTHON ARE INSTALLED
python --version
pip --version

# Install Dependencies
pip install flask, requests

# Mac Users might need to run
sudo pip install flask, requests

# Windows users use 'set', Mac Users use 'export'
set NEWS_API_KEY='YOUR_API_KEY'
set FLASK_APP=server.py

flask run

```

## 2. Open Tableau & Create Parameter
Open Tableau and click the sample superstore data set, any data will do as, the data is not the focus.

Once you have a sheet right click somewhere in the left hand parameters bar until you get a menu with create. Click create>parameters and enter the following. Feel free to choose your own topics, for best results make the topics rather vague in order to get a lot of articles back.

![Tableau Newsfeed](docs/imgs/create-param.png?raw=true "Title")

## 3. Create A Dashboard
Once you have your newly created sheet, go ahead and create a dashboard. In your dashboar drag a new web page obeject into the. Click the dropdown arrow in the top right of that sheet and click edit URL.

![Tableau Newsfeed](docs/imgs/newsfeed.png?raw=true "Title")
```bash
# Enter the following:
http://127.0.0.1:5000/news/

```

If you are wondering this the default address of the Python Web server you created. Once you have this URL, click the right dropdown arrow on the side and click the news parameter you created. Your new URL should look like the following.

```bash
# New URL
http://127.0.0.1:5000/news/<Parameters.Newfeed Controller>
```
This URL is telling your web app that you want news for whatever topic the current parameter is set to. This is very useful and can be customized much further to create really unique dashboards.

## 4. Show Off Your Awesome Dashboard
There you go, you just created your own custom newsfeed for Tableau. This demo has endless possibilites, with a little bit of programming know how you can add new routes for all sorts of uses such as weather for location, tweets by user, market price from public finance data, the possibilities are endless.

--Note:--
This is a great option for a local dashboard, but the webserver only works on your local computer. To share with others you have to deploy this app on a server

--Here are a few options:--
[Digital Ocean](https://www.digitalocean.com/)
[AWS](https://aws.amazon.com/)
[Python Anywhere](https://www.pythonanywhere.com/)
[Heroku](https://www.heroku.com/)

### Feedback
If the above steps were unclear or something did not work, create an issue. This is a side project and will be maintained as best as possible. Hope you enjoyed and learned something or sparked a creative idea for your next dashboard.
