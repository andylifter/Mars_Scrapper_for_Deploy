from NASA_api_key import API_KEY
import requests 
import datetime
import json
import time
import os


def get_images_Curiosity():
   while True:
      count_Curiosity = 0 
      jsondata = json.loads(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=' + API_KEY).text)
      for i in jsondata['latest_photos']:
         time.sleep(0.4)
         count_Curiosity += 1
         link = (i['img_src'])
         os.makedirs('static/Curiosity', exist_ok=True)
         dt = str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))
         img_data = requests.get(link).content
         with open(os.path.join("static/Curiosity", f"{dt}.jpg"), 'ab') as f:
            f.write(img_data)      
      # for file in os.listdir('static/Curiosity'): # clear directory from old images
      #    count_Curiosity -= 1
      #    os.remove('static/Curiosity/' + file)
      #    if count_Curiosity == 0:
      #       break      
      # time.sleep(1)
      # for item in os.listdir('static/Curiosity'): # delite small files
      #    if os.stat('static/Curiosity/' + item)[6] < 50000:
      #       os.remove('static/Curiosity/' + item)
      time.sleep(86500)
   




def get_images_Perseverance():
   while True:
      count_Perseverance = 0
      jsondata = json.loads(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key=' + API_KEY).text)
      for i in jsondata['latest_photos']:
         time.sleep(0.3)
         count_Perseverance += 1
         link = (i['img_src'])
         os.makedirs('static/Perseverance', exist_ok=True)
         dt = str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))
         img_data = requests.get(link).content
         with open(os.path.join("static/Perseverance", f"{dt}.jpg"), 'ab') as f:
            f.write(img_data)
      # for file in os.listdir('static/Perseverance'): # clear directory from old images
      #    count_Perseverance -= 1
      #    os.remove('static/Perseverance/' + file)
      #    if count_Perseverance == 0:
      #       break
      # time.sleep(1)
      # for item in os.listdir('static/Perseverance'): # delite small files
      #    if os.stat('static/Perseverance/' + item)[6] < 50000:
      #       os.remove('static/Perseverance/' + item)
      time.sleep(86500)


   