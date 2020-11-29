from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars_copy
from webdriver_manager.chrome import ChromeDriverManager


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars_dict=mars_dict)

@app.route('/scrape')
def scraper():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars_copy.scrape()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect('/', code=302)