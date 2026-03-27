import requests

# TODO: install the requests module
# try this: pip install requests
# or that:  python3 -m pip install requests

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-03-26&endtime=2026-03-27"


def main():
    locations = extract_locations()
    for location in locations:
        print(location)


def extract_locations():
    """
    Returns a list of (latitude, longitude) pairs from the API source.
    """
    response = requests.get(URL)
    response.raise_for_status()  # raises an error if the request failed
    data = response.json()

    locations = []
    for feature in data["features"]:
        coordinates = feature["geometry"]["coordinates"]
        longitude = coordinates[0]
        latitude = coordinates[1]
        magnitude = feature["properties"]["mag"]
        locations.append([latitude, longitude, magnitude])

    return locations


if __name__ == "__main__":
    main()
