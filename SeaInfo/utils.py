import bs4 as bs
import urllib.request
from collections import defaultdict

def get_wave_info():
    source = urllib.request.urlopen("http://xwave.co.il/").read()
    soup = bs.BeautifulSoup(source, 'lxml')

    dict_titles = ["date_time","wave_hight","wave_temp","wave_direction"]
    ashdod_weather = list()

    date_time = soup.find('span', {'class': 'tickerTime'}).text
    
    ashdod_weather.append(date_time)

    for i in soup.find_all('span', class_="tickDataPart"):
        ashdod_weather.append(i.text)

    return dict(zip(dict_titles,ashdod_weather))

def get_mediterranean_map():
    source = urllib.request.urlopen("https://isramar.ocean.org.il/isramar2009/wave_model/default.aspx?model=wam").read()
    soup = bs.BeautifulSoup(source, 'lxml')
    info = defaultdict(list)
    date_list_url = list()
    all_urls = list()
    date_dict = dict()

    all_options = soup.find_all('option')
    for options in all_options:
        date = options.get('value')
        if date[0] == '2':
            date_list_url.append(date)
            date_dict[date] = options.text
    for url in date_list_url:
        all_urls.append("https://isramar.ocean.org.il/isramar2009/wave_model/wave_maps/wam/"+date_list_url[0]+"00/coarse/"+url+".windir.gif")

    info["map_dates_url"] = all_urls
    info["map_dates"] = date_dict
    # image_url = "https://isramar.ocean.org.il/isramar2009/wave_model/wave_maps/wam/"+date_list[0]+"/coarse/"+date_list[0]+".windir.gif"
    
    return info

def get_forecast() -> defaultdict():
    
    source = urllib.request.urlopen("https://mavir.co.il/israel/ashdod").read()
    soup = bs.BeautifulSoup(source, 'lxml')
    URL = "https://mavir.co.il/"
    # output = defaultdict(dict)
    output = list()

    #
    # gather current temperature
    #
    now = soup.find("div", {"class": "now_block"})

    now_temp = now.find("strong").text
    now_img = URL + now.find("img").get("src")
    now_cur_time = now.find("p", {"class": ""}).text.replace(u'\xa0', u' ')

    # output.append({"image":now_img, "title": now_cur_time,"max_temp": now_temp,"min_temp": " "})
    output.append({"image":now_img, "title": now_cur_time,"max_temp": now_temp,"min_temp": " "})
    #
    # gathers ten day weather forecast
    #
    weather = soup.find_all("div", {"class": "forecast"})

    for index in range(len(weather)):
        #
        # create a temporary list
        #
        temp = dict()
        #
        # gather all needed info while inserting it into the temporary list
        #
        image = weather[index].find("img")
        temp["image"] = URL + image.get("src")
        temp["title"] = image.get("title")
        max_class = weather[index].find("div", {"class": "max"})
        temp["max_temp"] = max_class.text
        min_class = weather[index].find("div", {"class": "min"})
        temp["min_temp"] = min_class.text
        #
        # insert list into dict
        #
        output.append(temp)
    
    return output