# import required libraries
import json
import requests
import time
import folium

# begin infinite loop to continuously update information
while True:
    # GET request from API
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()

    # retrieve latitude and longitude data from response
    lat = float(data['iss_position']['latitude'])
    long = float(data['iss_position']['longitude'])

    # output latitude and longitude position to terminal
    print('The current position of the ISS is:')
    print('Latitude: %.2f' % (lat))
    print('Longitude: %.2f' % (long) + '\n')

    # create web map and add current position marker of ISS
    map = folium.Map(location=[lat, long], zoom_start=4, tiles="Stamen Terrain")
    featureGroup = folium.FeatureGroup(name="ISS Position")
    icon = folium.Icon(color='black', icon_color='white', icon='space-shuttle', angle=0, prefix='fa')
    popup = folium.Popup(html='Latitude: %.2f, Longitude: %.2f' % (lat, long), max_width=300)
    featureGroup.add_child(folium.Marker(location=[lat, long], popup=popup, icon=icon))
    map.add_child(featureGroup)
    map.save("ISS Position.html")

    # set delay until next iteration/request
    time.sleep(5)
