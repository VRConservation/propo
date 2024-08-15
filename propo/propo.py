"""Main module."""

import ipyleaflet
from ipyleaflet import basemaps

class Map(ipyleaflet.Map):
    """This is the map class that inherits from ipyleaflet.Map

    Args:
        ipyleaflet (Map): ipyleaflet.Map class
    """

    def __init__(self, center=[39, -120], zoom=5, **kwargs):
        """Initializes the map

        Args:
            center (list, optional): Set the center of the map to [39, -120].
            zoom (int, optional): Zooms to 5.
        """
        super().__init__(center=center, zoom=zoom, **kwargs)

    # def add_tile_layer(self, url, name, **kwargs):
    #     layer = ipyleaflet.TileLayer(url=url, name=name, **kwargs)
    #     self.add_layer(layer)

    # def add_basemap(self, name):
    #     """
    #     Adds a basemap to the map.

    #     Args:
    #         name (str or object): The name of the basemap as a string or a basemap object.

    #     If the name is a string, it evaluates the corresponding basemap URL and adds it as a tile layer.
    #     If the name is an object, it directly adds the basemap object.
    #     """

    #     if isinstance(name, str):
    #         url = eval(f"basemaps.{name}").build_url()
    #         self.add_tile_layer(url, name)
    #     else:
    #         self.add(name)    

    # def add_layers_control(self, position='topright'):
    #     """
    #     Adds a layers control to the map.

    #     Args:
    #         position (str): The position of the layers control on the map. 
    #                         Default is 'topright'. Other options include 'topleft', 
    #                         'bottomleft', and 'bottomright'.
    #     """
    #     self.add_control(ipyleaflet.LayersControl(position=position))    