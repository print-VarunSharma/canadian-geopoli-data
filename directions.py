import googlemaps
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
DISTANCE_API_key = os.getenv("GMAP_API_KEY")"             

gmaps = googlemaps.Client(key=GMAP_DISTANCE_API_KEY)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

