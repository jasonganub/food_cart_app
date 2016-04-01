import googlemaps

def get_key():
	key_file = open('..\etc\google_map_key.txt', 'r')
	google_key = key_file.readline()

	return google_key

def get_googlemap_client():
	gmaps = googlemaps.Client(key=get_key())

	return gmaps
