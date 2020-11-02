import pandas as pd
import googlemaps
from itertools import tee
# https://medium.com/how-to-use-google-distance-matrix-api-in-python/how-to-use-google-distance-matrix-api-in-python-ef9cd895303c
#Read CSV file into data frame named 'df'
#change seperator (sep e.g. ',') type if necessary
df = pd.read_csv('data/federal-coordinates.csv')


#Perform request to use the Google Maps API web service
API_key = "AIzaSyCzdSHETxm3V44Remxj9j663Tl-JdUVFLQ"  #enter Google Maps API key
gmaps = googlemaps.Client(key=API_key)


#pairwise function implemented to iterate through two consecutive rows (pairs) in a data frame
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#empty list - will be used to store calculated distances
list = [0]

# Loop through each row in the data frame using pairwise
for (i1, row1), (i2, row2) in pairwise(df.iterrows()):
      #Assign latitude and longitude as origin/departure points
      LatOrigin = row1['latitude'] 
      LongOrigin = row1['longitude']
      origins = (LatOrigin,LongOrigin)

      #Assign latitude and longitude from the next row as the destination point
      LatDest = row2['latitude']   # Save value as lat
      LongDest = row2['longitude'] # Save value as lat
      destination = (LatDest,LongDest)

      #pass origin and destination variables to distance_matrix function# output in meters
      result = gmaps.distance_matrix(origins, destination, mode='walking')["rows"][0]["elements"][0]["distance"]["value"]
      
      #append result to list
      list.append(result)

#Add column 'Distance' to data frame and assign to list values
df['Distance'] = list

df.to_csv('federal_calculated_distances.csv', sep=';', index=None, header= ['id','Latitude','Longitude','track_id','time','distance'])