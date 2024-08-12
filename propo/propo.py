"""Main module."""

import ipyleaflet

class Map(ipyleaflet.Map):

    def __init__(self, center=[39, -120], zoom=5, **kwargs):
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.add_control(ipyleaflet.LayersControl())
        self.add_control(ipyleaflet.FullScreenControl())
        self.add_control(ipyleaflet.MeasureControl())
        self.add_control(ipyleaflet.ScaleControl(position='bottomleft'))