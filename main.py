import folium
import pandas

map = folium.Map(location=[38.0,-99],zoom_start=6, titles="mapBox")

map.save("Map1.html")
