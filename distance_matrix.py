import pandas as pd
import googlemaps
import simplejson
import os
from dotenv import load_dotenv
load_dotenv()
API_key = os.getenv("GMAP_API_KEY")
data = pd.read_excel(r'data/federal-coordinates.xlsx')
output_filename = 'data/federal-coordinates-new.csv'


gmaps = googlemaps.Client(key=API_key)

#Add the list of coordinates to the main data set

# Federal Parliament 
origin = "45.420638,-75.708088" 
destinations = data.coordinates

# Distance 
actual_distance = []

for destination in destinations:
    def get_distance(apiKey, origin, destination):
        """
        Returns the driving time between using the Google Maps Distance Matrix API. 
        API: https://developers.google.com/maps/documentation/distance-matrix/start


        # INPUT -------------------------------------------------------------------
        apiKey                  [str]
        origin                  [str]
        destination             [str]

        # RETURN ------------------------------------------------------------------
        distance               [float] (kilomters)
        """
        origin = "45.420638,-75.708088"
        apiKey = os.getenv("GMAP_API_KEY")
        import requests
        url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
            .format(origin.replace(' ','+'),
                    str(destination).replace(' ','+'),
                    apiKey
                    )
            )
        try:
            response = requests.get(url)
            resp_json_payload = response.json()
            distance = resp_json_payload['rows'][0]['elements'][0]['distance']['value']/1000
        except:
            print('ERROR: {}, {}'.format(origin, destination))
            distance = 0
        return distance


    if __name__ == '__main__':
        # get key
        apiKey = os.getenv("GMAP_API_KEY")
        # get coordinates 
        origin = "45.420638,-75.708088"
        distance = get_distance(apiKey, origin, destination)
        print(distance)
        print('Origin:      {}\nDestination: {}\nDistance:  {} km'.format(origin, destination, distance))
 
        actual_distance.append(distance)
    


#Add the list of coordinates to the main data set

data["distance (Km)"] = actual_distance
data.head(337)

pd.DataFrame(actual_distance).to_csv(output_filename, encoding='cp1252')
