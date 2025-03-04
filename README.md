# Address to Coordinates Converter

## Overview

- This script conveniences information gathering by converting addresses into geographical coordinates (latitude and longitude).
It eliminates the need for manual research, data entry, and allows for quick insights through CSV generation.

### Features

- Manual Input Mode: Enter addresses one by one and receive instant latitude and longitude results.
- Batch Processing: Input multiple addresses and save the results to a CSV file for further analysis.
- Automated Geolocation: Uses the geopy library to retrieve precise coordinates for given addresses.

### Requirements
- python3.x
- geopy

### Usage
1. Install requirements
```
pip install geopy
```
2. Run the script and choose between manual input mode or batch processing:
3. Enter the desired option
- Option 1: Enter addresses manually and get real-time coordinates.
- Option 2: Input multiple addresses (comma-separated) and save them in a CSV file.

### How It Works

1. User input mode
- Prompts the user to enter an address.
- Uses geopy.Nominatim to fetch latitude and longitude.
- Displays the results immediately.

2. CSV Generation Mode:
- Prompts the user to enter multiple addresses.
- Fetches coordinates and writes them to addresses.csv.
- Saves the data in a structured format for easy reference.

### Example Output

#### Manual Mode
```
Enter address: Times Square, New York
Times Square, New York
Coordinates: (40.7580, -73.9855)
```
#### CSV Output (addresses.csv)
```
Address,Latitude,Longitude
Times Square, New York,40.7580,-73.9855
Eiffel Tower, Paris,48.8584,2.2945
Unknown Address,Not found,Not found
```
## Potential Use Cases

- OSINT (Open Source Intelligence) for data collection
- Automating geolocation for research and analysis
- Creating datasets for mapping and visualization
- Preprocessing address data for further geospatial applications

