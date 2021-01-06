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

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/badge-css-3-512.png" alt="css3" width="60" height="60"/> </a> <a href="https://www.djangoproject.com/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-original.svg" alt="django" width="60" height="60"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png" alt="python" width="60" height="60"/> </a> <a href="https://getbootstrap.com/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="60" height="60"> </a> <a href="https://web.dev/progressive-web-apps/" target="_blank"> <img src="https://media.prod.mdn.mozit.cloud/attachments/2019/06/14/16742/4a5f228a878fe1e8de5213bdb599eeef/pwa.png" alt="pwa" width="60" height="60"> </a>  <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank"> <img src="https://play-lh.googleusercontent.com/yMjUC6LBh7uOCK6wUcIEf5MHZQmSqDPXoInOQLZzw0DWQsPJuvkwSymX2zI4Ok7i_BY=s180-rw" alt="bf4" width="60" height="60"> </a>  <a href="https://www.heroku.com/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/heroku/heroku-original-wordmark.svg" alt="heroku" width="60" height="60"> </a> <a href="https://www.postgresql.org/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="60" height="60"> </a></p>

