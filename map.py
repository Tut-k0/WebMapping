import folium as f
import pandas as pd

data = pd.read_csv("Volcanoes.csv")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = f.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = f.FeatureGroup(name='My Map')

for lt, ln, el in zip(lat, lon, elev):
    iframe = f.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(f.Marker(location=[lt, ln], popup=f.Popup(iframe), icon=f.Icon(color='blue')))

map.add_child(fg)

map.save("output/test.html")
