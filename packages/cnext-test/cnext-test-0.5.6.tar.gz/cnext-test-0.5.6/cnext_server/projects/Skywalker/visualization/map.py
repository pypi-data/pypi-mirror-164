import folium
from IPython.core.display import display, HTML
m = folium.Map(location=[45.5236, -122.6750])
def folium_show(m, width, height):
    data = m.get_root().render()
    data_fixed_height = data.replace('width: 100%;height: 100%', 'width: {}'.format(width)).replace('height: 100.0%;', 'height: {};'.format(height), 1)
    display(HTML(data_fixed_height))

folium_show(m, '100%', '100%')
# display(m)

from ipyleaflet import Map, Marker

center = (52.204793, 360.121558)

m = Map(center=center, zoom=15)

marker = Marker(location=center, draggable=True)
m.add_layer(marker);
# m
display(HTML(m))