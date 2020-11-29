
# Dependencies

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

# Create a dictionary to store Mars info

mars_dict = {}


# Create a function to initializate the browser
 
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path)

### NASA Mars News ###

# Create a function to store the scrape proccess 

def mars_news():

    # Initialize browser

    browser = init_browser()

    # Visit the website
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    # Delay the extraction of information since the website took several seconds to load completely
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    
    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the list of articles
    slide_elem = soup.find_all('div', class_='list_text')
    
    # Obtain the lastest news title
    
    news_title = slide_elem[0].find('a').text
    
    # Obtain the summary paragraph of the lastest new 
    
    news_p = slide_elem[0].find('div', class_='article_teaser_body').text

    # Append the two variable to the dictionary

    mars_dict['news_title']= news_title
    mars_dict['news_paragraph']= news_p

    # Returns infomartion

    return mars_dict

    browser.quit()

## JPL Mars Space Images ##

# Use spliter to obtain the information from the website 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)



# Scrape page into Soup
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')
image_elem = image_soup.find_all('div', class_='carousel_items')


# Iterate through the feature image botton
feature_image_botton = image_elem[0].find('a', class_="button fancybox")
feature_image_botton


# Find the website source of the image

browser.links.find_by_partial_text('FULL IMAGE').click()
browser.links.find_by_partial_text('more info').click()

#Delay the extraction of information since the website took several seconds to load completely
browser.is_element_present_by_css("figure.lede", wait_time=1)


# Store the html of the current website
image_html = browser.html

# Scrape page into Soup
image_soup = BeautifulSoup(image_html, 'html.parser')


# Retrieve the figure tag 
figure_tag= image_soup.find_all('figure', class_='lede')


# Retrieve the image source from figure tag
image_source = figure_tag[0].find('a')['href']

image_source

# Store the image url 

website_url = 'https://www.jpl.nasa.gov'
image_url = website_url + image_source
image_url


### Mars Facts ###

# Use spliter to obtain the information from the website 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)
url = 'https://space-facts.com/mars/'
browser.visit(url)


# Dependencies
import pandas as pd


# Use Pandas to 'read_html' to parse the url
table_facts = pd.read_html('https://space-facts.com/mars/')

# Store the Mars Facts Table into a variable
mars_facts = table_facts[0]

# Assign hearders

mars_facts.columns = ['Facts', 'Value']
mars_facts.set_index('Facts', inplace =True)
mars_facts


# Convert the table to html

html_mars_facts = mars_facts.to_html(classes = 'table table-striped', header =True, index=True,justify='left')
print(html_mars_facts)


### Mars Hemispheres ###


# Use spliter to obtain the information from the website 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)

# Scrape page into Soup
hemispheres_html = browser.html
hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')

# Retrieve information for the four Mars hemispheres

hemispheres = hemispheres_soup.find_all('div', class_='item')


# Store the main url for the website

main_url = 'https://astrogeology.usgs.gov/'

# Create empty list to store hemisphere url

hemispheres_info = []

# Iterate throught the four hemispheres information

for item in hemispheres:
    
    # Find the title contained in the h3 tag
    
    title = item.find('h3').text
    
    # Retrieve the parcial url for each hemisphere
    
    parcial_url = item.find('a', class_="itemLink product-item")['href']
    
    # Combine the main url + parcial url to visit the four pages
    
    hemisphere_page_url = (main_url + parcial_url)
    
    # Visit the hemispheres pages
    
    browser.visit(hemisphere_page_url)
    
    # Scrape page into Soup
    
    hemisphere_page_html = browser.html
    hemisphere_page_soup = BeautifulSoup(hemisphere_page_html, 'html.parser')
    
    # Find the parcial link for the image
    
    parcial_image_url = hemisphere_page_soup.find('img', class_='wide-image')['src']
    
    # Combine the main url + parcial link
    
    image_url = main_url + parcial_image_url
    
    # Create dictionary with title and image url
    
    hemispheres_info.append({'title':title, 'image_url':image_url})


# Display the dictionary with the hemisphere info

hemispheres_info





