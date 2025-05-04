from flask import Flask, render_template
from NASA_api_key import API_KEY
import os

'''**********************************************************************************************************************************************'''
app = Flask(__name__)

'''**********************************************************************************************************************************************'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curiosity')
def curiosity():
    photos_curiosity = os.listdir('static/Curiosity') 
    photos_curiosity = ['Curiosity/' + image for image in sorted(photos_curiosity)]
    return render_template('curiosity.html', photos_curiosity=photos_curiosity) 
    
@app.route('/opportunity')
def oppopportunity():
    photos_opportunity = os.listdir('static/Opportunity')
    photos_opportunity = ['Opportunity/' + image for image in sorted(photos_opportunity)]
    return render_template('opportunity.html', photos_opportunity=photos_opportunity)

@app.route('/perseverance')
def perseverance():
    photos_perseverance = os.listdir('static/Perseverance')
    photos_perseverance = ['Perseverance/' + image for image in sorted(photos_perseverance)]
    return render_template('perseverance.html', photos_perseverance=photos_perseverance)

@app.route('/spirit')
def spirit():
    photos_spirit = os.listdir('static/Spirit')
    photos_spirit = ['Spirit/' + image for image in sorted(photos_spirit)]
    return render_template('spirit.html', photos_spirit=photos_spirit)

'''**********************************************************************************************************************************************'''

if __name__ == '__main__':
    app.run(debug=True)

# set FLASK_APP=app.py
# export FLASK_DEBUG=1
# flask run