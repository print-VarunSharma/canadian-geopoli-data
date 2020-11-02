import os
from dotenv import load_dotenv
load_dotenv()
GMAP_API_KEY = os.getenv("GMAP_API_KEY")
def get_distance(GMAP_API_KEY, origin, destination):
    """
    Returns the driving time between using the Google Maps Distance Matrix API. 
    API: https://developers.google.com/maps/documentation/distance-matrix/start


    # INPUT -------------------------------------------------------------------
    GMAP_API_KEY                  [str]
    origin                  [str]
    destination             [str]

    # RETURN ------------------------------------------------------------------
    distance               [float] (kilometers)
    """
    origin = "45.420638,-75.708088"
    destination = "49.282729,-123.120738"
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin.replace(' ','+'),
                   destination.replace(' ','+'),
                   GMAP_API_KEY
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
    GMAP_API_KEY = os.getenv("GMAP_API_KEY")

    # get coordinates 
    origin = "45.420638,-75.708088"
    destination = "49.282729,-123.120738"
    distance = get_distance(GMAP_API_KEY, origin, destination)
    print(distance)
    print('Origin:      {}\nDestination: {}\nDistance:  {} km'.format(origin, destination, distance))