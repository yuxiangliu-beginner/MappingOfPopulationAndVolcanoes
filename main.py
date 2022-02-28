import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
print(data.columns)
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
map = folium.Map(location=[38.0,-99],zoom_start=6, titles="mapBox")

# map.add_child(folium.Marker(location=[38.0,-99],
#                 popup="Hi, I am a maker",
#                 icon = folium.Icon(color="green")))
fg = folium.FeatureGroup(name="My map")

for lt,lo,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker([lt,lo]),popup=folium.Popup(str(el)+" m",parse_html=True),
                    icon = folium.Icon(color="green"))
map.save("Map1.html")
