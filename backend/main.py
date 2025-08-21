from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

#CORS(app, resources={r'/*':{'origins':'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})


#Dashboard
@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    response_object = {}
    keep = ['name', 'launches']
    response_object['ships'] = filter_endpoint_data('https://api.spacexdata.com/v4/ships',keep)
    response_object['rockets'] = get_spacexdata('https://api.spacexdata.com/v4/rockets')
    return response_object

#Rokets
@app.route('/api/rockets', methods=['GET'])
def rockets():
    response_object = {}
    #Retrive specific values to compare Height and Mass 
    keep = ['name', 'mass', 'height','id']
    response_object['rockets'] = filter_endpoint_data('https://api.spacexdata.com/v4/rockets',keep)
    return response_object


#Launches
@app.route('/api/launches', methods=['GET'])
def launches():
    response_object = {}
    keep = ['name', 'static_fire_date_utc', 'success']
    response_object['launches'] = filter_endpoint_data('https://api.spacexdata.com/v4/launches',keep)
    return response_object

#Starlink
@app.route('/api/starlink', methods=['GET'])
def starlink():
    response_object = {}
    keep = ['spaceTrack', 'static_fire_date_utc', 'success']
    response_object['starlink'] = filter_endpoint_data('https://api.spacexdata.com/v4/launches',keep)
    return response_object

def get_spacexdata(api_url):
        external_api_url = api_url  
        try:
            response = requests.get(external_api_url)
            response.raise_for_status()  # exception for HTTP errors (4xx or 5xx)
            data = response.json()  
            return data
            #print(data)
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500  # Return error respons


def filter_endpoint_data(url, keep_keys):
        api_data = get_spacexdata(url)
        print('api_data:   ---', type(api_data))
        extracted_ = [{key: d.get(key) for key in keep_keys if key in d} for d in api_data]
        return extracted_


if __name__ == "__main__":
    app.run()