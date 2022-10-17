# Import Python Packages
import requests
import random

# Declare count integer to keep track of restaurant indexs
count = 0

# Declare empty list of restaurants, rating, links, Phone Numbers, ID numbers (index of restaurants)
restaurants = []
ratings = []
links = []
phone_numbers = []
id_numbers = []

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

# Obtain Business information
restaurant_info = requests.get(url, params=params, headers=headers).json()

# Iterate through restaurants and save the names, ratings, links, phone numbers, and ID numbers in seperate lists
for restaurant in restaurant_info['businesses']:

    restaurants.append(restaurant['name'])
    ratings.append(restaurant['rating'])
    links.append(restaurant['url'])
    phone_numbers.append(restaurant['phone'])
    id_numbers.append(count)

    # Increment count
    count += 1

# Random index selected
choice = random.choice(id_numbers)

# Output the random restaurant selected along with rating, link, and phone number
print('Restaurant: ' + restaurants[choice])
print('Rating: ' + str(ratings[choice]))
print('Phone Number: ' + phone_numbers[choice])
print('Link: ' + links[choice])


