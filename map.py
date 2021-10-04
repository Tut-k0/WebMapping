import folium as f
import pandas as pd

data = pd.read_csv("Volcanoes.csv")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])


def color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'


html = """<h4>Volcano information:</h4>
<p>Name: %s </p>
<p>Height: %s m </p>
"""

map = f.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = f.FeatureGroup(name='Volcanoes')

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = f.IFrame(html=html % (nm, str(el)), width=200, height=100)
    fgv.add_child(f.CircleMarker(location=[lt, ln], radius=6, popup=f.Popup(iframe),
                                fill_color=color(el), color='grey', fill_opacity=0.7))

fgp = f.FeatureGroup(name='Population')

fgp.add_child(f.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                       style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(f.LayerControl())
map.save("output/test.html")
