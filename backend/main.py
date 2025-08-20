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
    response_object['launches'] = get_spacexdata('https://api.spacexdata.com/v4/launches')
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
    keep = ['name', 'date_utc', 'success']
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
    app.run(debug=True)



    #TODO
    # Sacar endpoints de launches  con 
    #   flitro e success  rate    o   frecuencia de lanzamientos
    # Sacar endpooints de starlink
        # con posiciones satelitales o parametros orbitales 
    #Pensar en los endpoints de dashboard
    # try: in filter_endpoint_data... removing keys instead of keep: https://www.google.com/search?q=remove+all+keys+from+list+and+keep+some&sca_esv=abfe88eb74890cc8&source=hp&ei=Kg6gaNTRA92kqtsP78vauAg&iflsig=AOw8s4IAAAAAaKAcOstsFWg2MSaODh_lbcrrhR2wxnA3&ved=0ahUKEwjUjoWBxI6PAxVdkmoFHe-lFocQ4dUDCA0&uact=5&oq=remove+all+keys+from+list+and+keep+some&gs_lp=Egdnd3Mtd2l6IidyZW1vdmUgYWxsIGtleXMgZnJvbSBsaXN0IGFuZCBrZWVwIHNvbWUyBBAhGBVI4H5Q3wRY331wBXgAkAEAmAHBAaABziaqAQQ4LjM0uAEDyAEA-AEBmAIvoAL6J6gCCsICChAAGAMY6gIYjwHCAgoQLhgDGOoCGI8BwgILEC4YgAQYsQMYgwHCAggQLhiABBixA8ICChAAGIAEGEMYigXCAggQABiABBixA8ICDhAAGIAEGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAgsQABiABBixAxiKBcICBRAAGIAEwgIQEAAYgAQYsQMYQxiDARiKBcICDhAuGIAEGLEDGNEDGMcBwgIHEAAYgAQYE8ICCBAAGBMYFhgewgIGEAAYFhgewgIFECEYnwXCAggQABiABBiiBMICBRAAGO8FwgIIEAAYogQYiQWYAwnxBQevWccLAR8pkgcFMTEuMzagB9zQAbIHBDYuMza4B90nwgcHNC4yMy4yMMgHcw&sclient=gws-wiz
