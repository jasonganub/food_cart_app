import googlemaps
from datetime import datetime
import googlemaps_api as gAPI

# key_file = open('..\etc\google_map_key.txt', 'r')
# google_key = key_file.readline()

# Replace the API key below with a valid API key.
# gmaps = googlemaps.Client(key=gAPI.get_key())
gmaps = gAPI.get_googlemap_client()

# my_address = '8800 SW Oleson Rd Portland, OR 97223'
my_address = '2333 NE Glisan St, Portland, OR 97232'
# Geocoding and address
print(gmaps.geocode(my_address))
print(gAPI.get_formatted_address(gmaps, my_address))
print(gAPI.get_state(gmaps, my_address))
lat, lng = gAPI.get_coordinates(gmaps, my_address)
print(lat)
print(lng)
print(gAPI.get_zip(gmaps, my_address))

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# print(gmaps)
# print("-------------------------------------")
# print(geocode_result)
# print("-------------------------------------")
# print(geocode_result[0]['formatted_address'])
# print("-------------------------------------")
# print(geocode_result[0]['geometry']['viewport']['southwest']['lat'])
# # print(reverse_geocode_result)
# print("-------------------------------------")
# print(geocode_result[0]['geometry']['viewport']['southwest']['lng'])
# # print(directions_result)
