import googlemaps
from datetime import datetime

def get_key():
	key_file = open('..\etc\google_map_key.txt', 'r')
	google_key = key_file.readline()

	return google_key

