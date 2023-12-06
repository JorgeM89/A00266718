import requests
import json
import time
from iso3166 import countries

# 2. Complete the if statement to ask the user for the Webex access token.
choice = input("Do you wish to use the hard-coded Webex token? (y/n) ")

if choice.lower() == 'n':
    accessToken = input("Please enter your Webex access token: ")
    accessToken = "Bearer " + accessToken
else:
    accessToken = "Bearer MTczYjFmMzEtOWE2ZS00ZTg4LTk3NWMtMDAxZWI5ZGY0MzIzMTBlZTVmOWEtMmVj_PC75_47fe537e-27d1-4e32-b2dc-2c26e4aa4fa0"

# 3. Provide the URL to the Webex Teams room API.
r = requests.get("https://webexapis.com/v1/rooms",
                 headers={"Authorization": accessToken})
# Code to handle response status...

# 4. Create a loop to print the type and title of each room.
print("List of rooms:")
rooms = r.json()["items"]
for room in rooms:
    print("Type: " + room["type"] + ", Name: " + room["title"])

# Code to search for the Webex Teams room...

# Webex Teams Bot Code...
while True:
    time.sleep(1)
    GetParameters = {"roomId": roomIdToGetMessages, "max": 1}
    r = requests.get("https://webexapis.com/v1/messages",
                     params=GetParameters,
                     headers={"Authorization": accessToken})
    # Code to handle response...

    if message.startswith("/"):
        location = message[1:]

        # 6. Provide your MapQuest API consumer key.
        mapsAPIGetParameters = {
            "location": location,
            "key": "SazHRCAva9pjAKDRnmxHFnLKpg07IxyI"
        }

        # 7. Provide the URL to the MapQuest GeoCode API.
        r = requests.get("https://www.mapquestapi.com/geocoding/v1/address",
                         params=mapsAPIGetParameters)
        # Code to handle MapQuest API response...

        # 8. Provide the MapQuest key values for latitude and longitude.
        locationLat = json_data["results"][0]["locations"][0]["displayLatLng"]["lat"]
        locationLng = json_data["results"][0]["locations"][0]["displayLatLng"]["lng"]

        # 9. Provide the URL to the Sunrise/Sunset API.
        ssAPIGetParameters = {
            "lat": locationLat,
            "lon": locationLng
        }
        r = requests.get("https://api.sunrise-sunset.org/json",
                         params=ssAPIGetParameters)
        # Code to handle Sunrise/Sunset API response...

        # 10. Provide the Sunrise/Sunset key value for day_length, sunrise, and sunset time.
        dayLengthSeconds = json_data["results"]["day_length"]
        sunriseTime = json_data["results"]["sunrise"]
        sunsetTime = json_data["results"]["sunset"]

        # 11. Complete the code to format the response message.
        responseMessage = "In {} the sun will rise at {} and will set at {}. The day will last {} seconds.".format(locationResults, sunriseTime, sunsetTime, dayLengthSeconds)

        # 12. Complete the code to post the message to the Webex Teams room.
        HTTPHeaders = {
            "Authorization": accessToken,
            "Content-Type": "application/json"
        }
        PostData = {
            "roomId": roomIdToGetMessages,
            "text": responseMessage
        }
        r = requests.post("https://webexapis.com/v1/messages",
                          data=json.dumps(PostData),
                          headers=HTTPHeaders)
        # Code to check response status...
