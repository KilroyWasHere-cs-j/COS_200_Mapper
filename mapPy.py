import statistics
import webbrowser
import folium as f
import os
import math
import base64
from folium import IFrame


class mapper:

    def saveMap(self, map, name="map.html"):
        if os.path.exists(os.getcwd() + "/maps"):
            if ".html" in name:
                map.save(os.getcwd() + "/maps/" + name)
            else:
                raise "Not .html file"
        else:
            os.mkdir(os.getcwd() + "/maps")

    def showMap(self, map):
        # Peak programming I tell you
        map.save("map.html")
        webbrowser.open("map.html")

    # Create a map at given a lat and lng
    def createMap(self, lat, lon, zoom_factor=10):
        return f.Map(location=[lat, lon], zoom_start=zoom_factor)

    # Create a map marker
    # Map (the map to add the marker to
    # lat and lon (of the marker you wish to add)
    # title (title of the marker)
    def addMarker(self, map, lat, lon, tooltip="", color="blue", icon="info-sign"):
        encoded = base64.b64encode(open('/home/gabrieltower/PycharmProjects/COS200_Geopandas/data/2022-09-15-124035.jpg', 'rb').read())
        html = '<img src="data:image/JPG;base64,{}">'.format
        iframe = IFrame(html(encoded.decode("UTF-8")), width=632 + 20, height=420 + 20)
        popup = f.Popup(iframe, max_width=2650)
        marker = f.Marker(
            location=[lat, lon],
            popup=popup,
            icon=f.Icon(color=color, icon=icon),
            tooltip=tooltip)
        marker.add_to(map)

    def drawCircle(self, map, lat=0.0, lon=0.0, radius=5, tooltip="Lorem Ipsum"):
        marker = f.CircleMarker(
            location=[lat, lon],
            radius=50,
            popup="<stong>Allianz Arena</stong>",
            tooltip=tooltip)
        marker.add_to(map)


    def drawLine(self, map, lat_lon, colour="blue"):
        loc_1 = list(lat_lon)
        line = f.PolyLine(locations=loc_1, color=colour, no_clip=True)
        line.add_to(map)

    # Get the distance between to points given lat lon using Haversine formula
    def get_distance(self, lat_1, lng_1, lat_2, lng_2):
        lng_1, lat_1, lng_2, lat_2 = map(math.radians, [lng_1, lat_1, lng_2, lat_2])
        d_lat = lat_2 - lat_1
        d_lng = lng_2 - lng_1

        temp = (
                math.sin(d_lat / 2) ** 2
                + math.cos(lat_1)
                * math.cos(lat_2)
                * math.sin(d_lng / 2) ** 2
        )
        # Divide the output by 1.609344 to convert kilometers to miles
        return (6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))) / 1.609344


    def getCenterPoint(self, point):
        return statistics.mean(point)
