from NASA_api_key import API_KEY
import requests 
import datetime
import json
import time
import os


def get_images_Rover():
   try:

      while True:
         
         for filename in os.listdir('static/Curiosity'):
            file_path = os.path.join('static/Curiosity', filename)
            if os.path.isfile(file_path):
               os.remove(file_path)

         for filename in os.listdir('static/Perseverance'):
            file_path = os.path.join('static/Perseverance', filename)
            if os.path.isfile(file_path):
               os.remove(file_path)

         time.sleep(1)
         jsondata = json.loads(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=' + API_KEY).text)
         for i in jsondata['latest_photos']:
            time.sleep(0.4)
            link = (i['img_src'])
            os.makedirs('static/Curiosity', exist_ok=True)
            dt = str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))
            img_data = requests.get(link).content
            with open(os.path.join("static/Curiosity", f"{dt}.jpg"), 'ab') as f:
               f.write(img_data)     

         time.sleep(1)
         jsondata = json.loads(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key=' + API_KEY).text)
         for i in jsondata['latest_photos']:
            time.sleep(0.4)
            link = (i['img_src'])
            os.makedirs('static/Perseverance', exist_ok=True)
            dt = str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))
            img_data = requests.get(link).content
            with open(os.path.join("static/Perseverance", f"{dt}.jpg"), 'ab') as f:
               f.write(img_data) 
         
         time.sleep(1)
         for item in os.listdir('static/Curiosity'): # delite small files
            if os.stat('static/Curiosity/' + item)[6] < 50000:
               os.remove('static/Curiosity/' + item)

         time.sleep(1)
         for item in os.listdir('static/Perseverance'): # delite small files
            if os.stat('static/Perseverance/' + item)[6] < 50000:
               os.remove('static/Perseverance/' + item)

         time.sleep(14400) # 6 times per twenty-four hours 14400

   except:
      pass                  
      
      

  

