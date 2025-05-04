from NASA_api_key import API_KEY
import requests 
import datetime
import json
import time
import os

# *************************************************************** get images ***********************************************************#
count_Curiosity = 0 
jsondata = json.loads(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=' + API_KEY).text)
for i in jsondata['latest_photos']:
   count_Curiosity += 1
   link = (i['img_src'])
   os.makedirs('static/Curiosity', exist_ok=True)
   dt = str(datetime.datetime.now()).replace(' ', '_').replace('-', '_').replace(':', '_')
   img_data = requests.get(link).content
   with open(os.path.join("static/Curiosity", f"{dt}.jpg"), 'ab') as f:
      f.write(img_data)

time.sleep(3)

count_Perseverance = 0
jsondata = json.loads(requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key=' + API_KEY).text)
for i in jsondata['latest_photos']:
   count_Perseverance += 1
   link = (i['img_src'])
   os.makedirs('static/Perseverance', exist_ok=True)
   dt = str(datetime.datetime.now()).replace(' ', '_').replace('-', '_').replace(':', '_')
   img_data = requests.get(link).content
   with open(os.path.join("static/Perseverance", f"{dt}.jpg"), 'ab') as f:
      f.write(img_data)

time.sleep(3)

# **************************************************** clear directory from old images ***********************************************#
# for file in os.listdir('static/Curiosity'):
#    count_Curiosity -= 1
#    print(file, ' Curiosity')
#    os.remove('static/Curiosity/' + file)
#    if count_Curiosity == 1:
#       break


# for file in os.listdir('static/Perseverance'):
#    count_Perseverance -= 1
#    print(file, ' Perseverance')
#    os.remove('static/Perseverance/' + file)
#    if count_Perseverance == 1:
#       break

# time.sleep(1)

# ******************************************************* delite small files **********************************************************#
for item in os.listdir('static/Curiosity'):
   if os.stat('static/Curiosity/' + item)[6] < 50000:
      os.remove('static/Curiosity/' + item)

for item in os.listdir('static/Perseverance'):
   if os.stat('static/Perseverance/' + item)[6] < 50000:
      os.remove('static/Perseverance/' + item)


print(len(os.listdir('static/Curiosity')))
print(len(os.listdir('static/Perseverance')))