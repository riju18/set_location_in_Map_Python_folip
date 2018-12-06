# install folium by pip [ for data visualization by leaflet map  that's been manipulated in Python ]
# ---------------------------------------------------------------------------------------------

# documentation:
#-------------------

# https://python-visualization.github.io/folium/quickstart.html#Getting-Started
#----------------------------------------------------------------------------------

import folium
import os
folder = os.path.dirname(os.path.abspath(__file__))
mapFile = os.path.join(folder, 'universityPosition.html')

# dir(folium)   # all builtin fn
# help(folium.map) # particular help for fn

# 1st: longitude, latitude; 2nd: zoom; 3rd: bg style
#--------------------------------------------------------
map1 = folium.Map(location=[23.762680, 90.419452],
                  zoom_start=13, tiles='Stamen Terrain')

#particular style in main map
# -----------------------------    

lati = [23.768812, 23.780897, 23.714500, 23.750402]
longi = [90.425823, 90.424380, 90.428612, 90.413471]
location = ['gulsan', 'ewu', 'DIT', 'saydabad']
color = ['green', 'red', 'blue', 'orange']

for la, lo, pla, c in zip(lati, longi, location, color):
    folium.Marker(location=[la, lo], popup=pla,
                  icon=folium.Icon(color=c, icon='info-sign')).add_to(map1)

map1.save(mapFile)

