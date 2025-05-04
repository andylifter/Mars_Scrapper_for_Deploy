from fake_useragent import UserAgent
from NASA_api_key import API_KEY
import requests
import json

'''*Парсер собирает актуальные фото от 4 марсоходов*'''


''' parameters for parser *******************************************************************************************************************************'''
ua = UserAgent()
headers = {"User-Agent": ua.random, "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"}
params = {'api_key': API_KEY}


''' requests mars rovers photo **************************************************************************************************************************'''
request_curiosity = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=DEMO_KEY', 
                                 headers=headers, params=params)
json_curiosity = json.loads(request_curiosity.text)
photos_curiosity = json_curiosity['latest_photos']


request_opportunity = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/latest_photos?api_key=DEMO_KEY', 
                                   headers=headers, params=params)
json_opportunity = json.loads(request_opportunity.text)
photos_opportunity = json_opportunity['latest_photos']


request_perseverance = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key=DEMO_KEY', 
                                    headers=headers, params=params)
json_perseverance = json.loads(request_perseverance.text)
photos_perseverance = json_perseverance['latest_photos']


request_spirit = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/latest_photos?api_key=DEMO_KEY', 
                              headers=headers, params=params)
json_spirit = json.loads(request_spirit.text)
photos_spirit = json_spirit['latest_photos']


''' managmen for tags 'img_src', save and download in folder*********************************************************************************************'''
curiosity_quantity = 0
for i in photos_curiosity:    
    curiosity = requests.get(i['img_src'], stream=True)
    curiosity_quantity += 1
    curiosity_open = open('/home/aser/Рабочий стол/VSC_files/HTML_CSS/Mars_Image_Scrapper/static/Curiosity/' + str(curiosity_quantity) + '.jpg', 'wb')
    for value in curiosity.iter_content(1024*1024):
        curiosity_open.write(value)
    curiosity_open.close()

opportunity_quantity = 0
for i in photos_opportunity:
    opportunity = requests.get(i['img_src'], stream=True)
    opportunity_quantity += 1
    opportunity_open = open('/home/aser/Рабочий стол/VSC_files/HTML_CSS/Mars_Image_Scrapper/static/Opportunity/' + str(opportunity_quantity) + '.jpg', 'wb')
    for value in opportunity.iter_content(1024*1024):
        opportunity_open.write(value)
    opportunity_open.close()

perseverance_quantity = 0
for i in photos_perseverance:
    perseverance = requests.get(i['img_src'], stream=True)
    perseverance_quantity += 1
    perseverance_open = open('/home/aser/Рабочий стол/VSC_files/HTML_CSS/Mars_Image_Scrapper/static/Perseverance/' + str(perseverance_quantity) + '.jpg', 'wb')
    for value in perseverance.iter_content(1024*1024):
        perseverance_open.write(value)
    perseverance_open.close()

spirit_quantity = 0
for i in photos_spirit:
    spirit = requests.get(i['img_src'], stream=True)
    spirit_quantity += 1
    spirit_open = open('/home/aser/Рабочий стол/VSC_files/HTML_CSS/Mars_Image_Scrapper/static/Spirit/' + str(spirit_quantity) + '.jpg', 'wb')
    for value in spirit.iter_content(1024*1024):
        spirit_open.write(value)
    spirit_open.close()



