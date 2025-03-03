import requests
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geo_converter")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def main():
    addresses = input("Enter address")
   # addresses = [
    #    "1600 Amphitheatre Parkway, Mountain View, CA",
    #   "221B Baker Street, London",
    #  "Eiffel Tower, Paris"
    #]
    
    for address in addresses:
        coords = get_coordinates(address)
        if coords:
            print(f"{address}\nCoordinates: {coords}\n")
        else:
            print(f"{address}\nCoordinates: Not found\n")

if __name__ == "__main__":
    main()

