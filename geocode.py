from geocodio import GeocodioClient
import os
from dotenv import load_dotenv
load_dotenv()
GEOCODIO_API_KEY = os.getenv("GEOCODIO_API_KEY")
client = GeocodioClient(GEOCODIO_API_KEY)

geocoded_addresses = client.geocode([
        "2405 Legislative Drive, Regina, SK"
    ])
# print(geocoded_addresses)
print(geocoded_addresses.coords)

print(geocoded_addresses[0].coords)

locations = client.reverse([
    (45.61625, -61.630912),
    (43.685815, -79.759934)])
print(locations.formatted_addresses)