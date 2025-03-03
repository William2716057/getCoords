import requests
import csv
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geo_converter")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def user_input():
    while True:
        address = input("Enter address: ")
        
        coords = get_coordinates(address)
        if coords:
            print(f"{address}\nCoordinates: {coords}\n")
        else:
            print(f"{address}\nCoordinates: Not found\n")
            
def create_csv():
    addresses = input("Enter addresses separated by commas: ").split(",")  
    addresses = [addr.strip() for addr in addresses]  

    with open("addresses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Address", "Latitude", "Longitude"])

        for address in addresses:
            coords = get_coordinates(address)
            if coords:
                writer.writerow([address, coords[0], coords[1]])
                print(f"{address}\nCoordinates: {coords}\n")
            else:
                writer.writerow([address, "Not found", "Not found"])
                print(f"{address}\nCoordinates: Not found\n")

def main():
    choice = input("To enter manually press 1 or to save as CSV file press 2: ").strip()
    
    if choice == "1":
        user_input()
    elif choice == "2":
        create_csv()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()