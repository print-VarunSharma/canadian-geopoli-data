import pandas as pd
import googlemaps
import simplejson
import os
from dotenv import load_dotenv
load_dotenv()
API_key = os.getenv("GMAP_API_KEY")

data = pd.read_csv(r'data\bcprovincial-coordinates.csv', encoding='cp1252') 
# data_name = print("Enter excel data name to read: ")
# data = pd.read_excel(r'data\bcprovincial-coordinates.xlsx')
output_filename = 'bc-distances.csv'


gmaps = googlemaps.Client(key=API_key)

#Add the list of coordinates to the main data set

# Federal Parliament origin = "45.420638,-75.708088" 

# Provincial Parliament	Address	coordinates
# BC	501 Belleville St, Victoria, BC V8V 2L8	48.419617,-123.370285
# AB	10800 97 Ave NW, Edmonton, AB T5K 2B6	53.5334764,-113.5066378
# MB	450 Broadway, Winnipeg, MB R3C 0V8	49.8861418,-97.1452309
# SK	2405 Legislative Dr, Regina, SK S4S 0B3	50.4324892,-104.6152067
# ON	111 Wellesley St W, Toronto, ON M7A 1A2	43.6622891,-79.3915068
# QC	1045 Rue des Parlementaires, Québec, QC G1A 1A3	46.808706,-71.2141788
# NS	1726 Hollis St, Halifax, NS B3J 2Y3	44.6479459,-63.57334890000001
# PEI	165 Richmond St, Charlottetown, PE C1A 1J1	46.2349926,-63.1260783
# NL	100 Prince Philip Dr, St. John's, NL A1B 3R4	47.58319119999999,-52.7242471
# NB	706 Queen St, Fredericton, NB E3B 1C5	45.9593069,-66.63628100000001

origin = "48.419617,-123.370285"

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
        distance = get_distance(apiKey, origin, destination)
        print(distance)
        print('Origin:      {}\nDestination: {}\nDistance:  {} km'.format(origin, destination, distance))
 
        actual_distance.append(distance)
    


#Add the list of coordinates to the main data set

data["distance (Km)"] = actual_distance
data.head(86)

pd.DataFrame(actual_distance).to_csv(output_filename, encoding='cp1252')
