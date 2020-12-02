# web-scraping-challenge

This project aims to create a Flask application connected to a MongoDB, which includes information about the mission to Mars. The information stored in the database is scraped every time the application is run, allowing it to have the most updated information.

There are three components to achieve this project:

### 1. Scraping process 

Four sources were used to retrieve the necessary information:

**NASA Mars News**

Source: https://mars.nasa.gov/news/
The script retrieves the latest News Title and Paragraph summary.

**JPL Mars Space Images - Featured Image**

Source:https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
The script finds the URL of the full-size image for the current Featured Mars Image to display it in the application.

**Mars Facts**

Source: https://space-facts.com/mars/
From the Mars Facts webpage, Pandas scrapes the table containing the main facts about the planet.  

**Mars Hemispheres**

Source: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
Script visits the USGS Astrogeology site and the four links to retrieve the URL of the full resolution images for each of Mars hemispheres.

The jupyter notebook “mission_to_mars” includes the scripts. However, they were stored in a function called “scrape” in the file scrape_mars.py to use it in the flask app.

### 2. Flask application

The connection between the app and MongoDB was established in file “app.py.” The file includes two routes:

(‘/’): It render the HTML template
(‘/scrape’): It returns the information of the database with the aid of the scrape function
 
### 3. HTML 

With the aid of bootstrap, a website was designed to display the information in an organized way.
 
