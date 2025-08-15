from flask import Flask, jsonify
from flask_cors import CORS
import requests



app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

#CORS(app, resources={r'/*':{'origins':'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})


#Dashboard
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")





def get_launches(api_url, params=None):
    """
    Fetches data from a specified API URL.

    Args:
        api_url (str): The URL of the API endpoint.
        params (dict, optional): A dictionary of query parameters to send with the request.

    Returns:
        dict or None: The JSON response from the API, or None if an error occurs.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()  # Parse the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None


if __name__ == "__main__":
    app.run(debug=True)