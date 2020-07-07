# Find Your Destination

## Summary
We have created a map with an interactive dashboard for anyone looking to decide which state to travel to. Our webpage provides you a choropleth on the most popular states to travel to based on a equation created by our group. By clicking on each state, you can find information on various attractions offered, average flight costs and the value of your money there. Explore the map to find your ideal destination right at your footsteps!

## Group Members
* Solito Reyes
* Kasia Kalemba
* Shrilekha Vijayakanthan
* Sandra Froonjian

## Motivation
Currently, Americans are not allowed to travel outside of the US, so why not find your perfect destination in your own country? With so many options of places to travel to even just within the US, it can be overwhelming to decide where to go for your vacation. This app can help you decide by displaying various charts with information related to the most popular destinations, the most expensive flights, states with the best rated hotels, and states with the most amount of attractions.

### Visualization Examples for Inspiration
![US Chorolpleth Map](.png)
![Graph for Visualization of Attraction](.png)

## Sources
* Flights: Travel cost per destination & amount of passengers 
  [United States Department of Transportation]
  (https://www.transtats.bts.gov/AverageFare/)
  * USED INSERT WHICH YEAR AND DATASET.
* Hotel Rankings 
  [Datafiniti's Business Database]
  (https://www.kaggle.com/datafiniti/hotel-reviews?select=Datafiniti_Hotel_Reviews.csv)
  * USED INSERT WHICH PART OF DATASET
* Attractions based on the state [Wikipedia]
  (https://en.wikipedia.org/wiki/Tourist_attractions_in_the_United_States)
  * Scraped this page to extract info for: Casinos, National Parks, Aquariums, Zoos, Festivals, Amusement Parks, Beaches, Malls, Campsites
* Campground Locations [DataWorld]
  (https://data.world/caroline/campgrounds)
  * USED INSERT WHICH
* Value of dollar based on state [USA Today]
  (https://www.usatoday.com/story/money/2019/05/25/us-dollar-how-much-its-worth-value-in-every-state/39501091/)
  * Scraped the website to extract the value matched with the state

---

## Workflow
### Step 1: Extract Data
* Downloaded data as csvs or scarped it from webpages such as Wikipedia and USA News 
* Downloaded geoJson dataset for state boundaries from Mike Bostock's public file

### Step 2: Clean Data and Enter into Database
* Using Jupyter Notebook, we loaded the data from CSV's to visualize it and clean it up
* Using Jupyter Notebook, we scraped the attraction data from Wikipedia and converted it to CSV files
* Using QuickDB, developed code for Postgres table set up 
* Created tables for ustravelapp_db and made a custom ranking list for each state

### Step 3: Flask App
* Using an app.py file for the Flask App

### Step 3: Render Data
* HTML & CSS Files
  * index.html: main webpage used for the website
  * style.css: custom css file to use for styling of select objects
  * bootstrap.min.css: bootstap theme and styling used for Bootstrap features 

* Javascript Files:
  * logic.js: primary file to launch our interactive page
  * config.js: insert API key for rendering of map objects

  Javascript Packages used:
  * Mapbox
  * Leaflet
  * d3

## System Requirements
* Chrome Web Browser
* Python environment running Python 3.7

## Steps to run the application
1. 
