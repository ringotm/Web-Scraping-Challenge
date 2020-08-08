from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraper

app = Flask(__name__)

# Or set inline
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars_data=mars_data)


@app.route("/scrape")
def scrape():
    mongo.db.collection.drop()
    mars_facts = mars_scraper.scrape_info()
    mongo.db.collection.update({}, mars_facts, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
