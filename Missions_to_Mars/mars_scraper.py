import pandas as pd
from bs4 import BeautifulSoup
import time
from splinter import Browser

mars_news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

path = {"executable_path": "C:/Users/Tommy/anaconda3/Scripts/chromedriver.exe"}
browser = Browser("chrome", **path, headless=True)

browser.visit(mars_news_url)
time.sleep(2)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

news_title = (
    soup.find("div", class_="list_text").find("div", class_="content_title").text
)

news_p = soup.find("div", class_="article_teaser_body").text


mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


browser.visit(mars_image_url)
time.sleep(2)


html = browser.html
soup = BeautifulSoup(html, "html.parser")


mars_images = soup.find("li", class_="slide").find("a", class_="fancybox")[
    "data-fancybox-href"
]


base_url = "jpl.nasa.gov"
featured_image_url = base_url + mars_images

mars_twitter_url = "https://twitter.com/marswxreport?lang=en"

browser.visit(mars_twitter_url)
time.sleep(2)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

tweets = browser.find_by_css("[data-testid=tweet]").find_by_tag("span")

tweets = browser.find_by_css("[class=r-1qd0xha]")

tweets = browser.find_by_tag("span").find_by_css(".css-16my406")

tweets = browser.find_by_css(
    ".css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0"
)

for tweet in tweets:
    if tweet.text.startswith("InSight"):
        mars_weather = tweet.text
        break


mars_facts_url = "https://space-facts.com/mars/"
browser.visit(mars_facts_url)
time.sleep(2)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

mars_table = pd.read_html(mars_facts_url)[0]


mars_table = mars_table.set_index(0).rename(columns={1: "Facts"})
mars_table.index.name = ""

mars_astrogeology_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


browser.visit(mars_astrogeology_url)
time.sleep(2)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("div", class_="description")

base_url = "https://astrogeology.usgs.gov"

hemisphere_image_urls = []
for link in links:
    mars_dict = {}
    browser.visit(base_url + link.a["href"])
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_dict["title"] = soup.find("h2", class_="title").text[:-9]
    mars_dict["url"] = soup.find("li").a["href"]
    hemisphere_image_urls.append(mars_dict)
    time.sleep(2)

