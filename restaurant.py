# Import Python Packages
import requests
import random

# Declare API KEY and header information
api_key = ''
headers = {'Authorization': 'Bearer %s' % api_key}

# Get URL for search
url = 'https://api.yelp.com/v3/businesses/search'

# Obtain User Location and User Cuisine Choice
user_location = input('What city are you in? ')
user_cuisine = input('What type of cuisine are you looking for? ')

# Set parameters for search
params = {
    'location': user_location,
    'radius': 5000,
    'sort_by': 'rating',
    'open_now': True,
    'limit': 10
}

information = requests.get(url, params=params, headers=headers).text

