# SeaScrapes

This is my personal web scraper that collects information about the sea from three different sites.
I needed a way to easily collect this information since I always needed to alter between those sites
before going surfing or diving.

the scraping is done using Beautiful Soup 4 in the Python utils.py file.
I've used django in-order to allow my progressive web application access to the scraped information.

It was designed using bootstrap and the site runs using vanilla js and django templates. 
the app itself was uplaoded to Heroku and is using postgresql for the database.

https://seascrapes.herokuapp.com/SeaInfo/

Information taken from a buoy near Ashdod  | Wave and wind maps of the mediterranean sea | ten day forecast for Ashdod
------------ | ------------- | -------------
![buoy](https://github.com/DrorTsky/SeaScrapes/blob/main/images/Scrapes_details.png) | ![med](https://github.com/DrorTsky/SeaScrapes/blob/main/images/Scrapes_seaMaps.png) | ![weather](https://github.com/DrorTsky/SeaScrapes/blob/main/images/Scrapes_weather.png)
