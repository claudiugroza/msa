import requests
from pprint import pprint


# the API service URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# supplied key after generation
API_KEY = '24d7e2582079e9fa0152443d5ea4e9f6'


def fetch_weather(city):
    # construct querry parameters
    query_params = {'APPID': API_KEY, 'q': city}
    # make a HTTP GET request
    response = requests.get(BASE_URL, params=query_params)
    print response.url
    # get the JSON object
    json_response = response.json()
    # print the content
    pprint(json_response)

    if json_response['cod'] == 200:
        # extract and check precipitations prediction
        cloud_percentage = json_response['clouds']['all']
        if cloud_percentage >= 50:
            print 'Hey buddy, you may want to take an umbrella.'
        else:
            print 'Sky is clear. Clear to go.'
    else:
        print 'Request error: ', json_response['message']


fetch_weather('Timisoara')
