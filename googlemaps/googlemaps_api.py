import googlemaps

def get_key():
	key_file = open('..\etc\google_map_key.txt', 'r')
	google_key = key_file.readline()

	return google_key

def get_googlemap_client():
	return googlemaps.Client(key=get_key())

def get_sorted_geocode(gmaps, address):
	geocode_result = gmaps.geocode(address)[0]
	sorted_dictionary = sorted(geocode_result.items(), key=operator.itemgetter(1))

def get_formatted_address(gmaps, address):
	return gmaps.geocode(address)[0]['formatted_address']

def get_state(gmaps, address):
	return get_formatted_address(gmaps, address).split(' ')[-3]

def get_coordinates(gmaps, address):
	latitude = gmaps.geocode(address)[0]['geometry']['location']['lat']
	longitude = gmaps.geocode(address)[0]['geometry']['location']['lng']

	return latitude, longitude

def get_zip(gmaps, address):
	return get_formatted_address(gmaps, address).split(' ')[-2][0:5]