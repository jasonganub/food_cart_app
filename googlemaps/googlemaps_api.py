import googlemaps

def get_key():
	key_file = open('..\etc\google_map_key.txt', 'r')
	google_key = key_file.readline()

	return google_key

def get_googlemap_client():
	return googlemaps.Client(key=get_key())


def get_formatted_address(gmaps, address):
	return gmaps.geocode(address)[0]['formatted_address']

def get_state(gmaps, address):
	return gmaps.geocode(address)[0]['address_components'][4]['short_name']