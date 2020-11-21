import urllib, urllib2, json
import googlemaps
import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_key = os.getenv("GMAP_API_KEY")

gmaps = googlemaps.Client(key=API_key)
def decodeAddressToCoordinates( address ):
        urlParams = {
                'address': address,
                'sensor': 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode( urlParams )
        response = urllib2.urlopen( url )
        responseBody = response.read()

        body = StringIO.StringIO( responseBody )
        result = json.load( body )
        if 'status' not in result or result['status'] != 'OK':
                return None
        else:
                return {
                        'lat': result['results'][0]['geometry']['location']['lat'],
                        'lng': result['results'][0]['geometry']['location']['lng']
                }  