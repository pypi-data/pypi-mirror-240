# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geohexgrid']

package_data = \
{'': ['*']}

install_requires = \
['Rtree>=1.0.0', 'geopandas>=0.11.1']

setup_kwargs = {
    'name': 'geohexgrid',
    'version': '2.0.0',
    'description': "A Python library for making geographic flat-top hexagon grids like QGIS's `create grid` function",
    'long_description': 'Geohexgrid\n**********\nA tiny Python 3.9+ library for making geographic flat-top hexagonal grids like QGIS\'s `create grid function <https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorcreation.html?highlight=create%20grid#create-grid>`_.\nThat\'s it.\nNot designed for making other kinds of grids or `discrete global grid systems <https://en.wikipedia.org/wiki/Discrete_global_grid>`_.\n\nHere a **hexagonal grid**, or **hex grid** for short, is a finite subset of a hexagonal tiling.\nA hexagonal tiling is a covering of the plane with regular hexagons in which exactly three hexagons meet at each vertex.\n(For more details, see `the Wikipedia article on hexagonal tilings <https://en.wikipedia.org/wiki/Hexagonal_tiling>`_.)\nThe **circumradius** of a hex grid is the circumradius of any one of its hexagons, that is, the radius of a circle circumscribing any one of the hexagons.\nThis library favours the word \'grid\' over \'tiling\', because \'grid\' is used more often in geographic context, the main context of this library.\n\nThe two main features of this library are\n\n- Making a flat-top hexagonal grid of given circumradius that minimally covers a GeoDataFrame of features, where distance units come from the GeoDataFrame\'s coordinate reference system (CRS), e.g. no units for no CRS, metres for the New Zealand Transverse Mercator (NZTM) CRS, and decimal degrees for the WGS84 CRS.\n- By default, hex grids made with a common CRS and circumradis share an origin and thus have equal hexagons (and hexagon IDs) where they overlap.\n  In other words, the grids share a single (infinite) hexagonal tiling of the plane, which is useful when reconciling multiple grids across different geographic areas.\n\nThe main non-feature of this library is\n\n- Making any other kind of grid, e.g. ones with pointy-top hexagons, squares, triangles, kisrhombilles, Penrose tiles...\n\nHere\'s an typical example.\n\n.. code-block:: python\n\n  import geopandas as gpd\n  import geohexgrid as ghg\n\n  # Load New Zealand territorial authorities projected in EPSG 2193 (NZTM)\n  nz = gpd.read_file(DATA_DIR / "nz_tas.gpkg")\n\n  # Cover it minimally with hexagons of circumradius 10 kilometres\n  grid = ghg.make_grid_from_gdf(nz, R=10_000)\n\n  # Plot\n  base = nz.plot(color="black", figsize=(20, 20), aspect="equal")\n  grid.plot(ax=base, color="white", edgecolor="red", alpha=0.5)\n\n\n.. image:: nz_10000m.png\n  :width: 400\n  :alt: hexagon grid of 10,000-metre circumradius covering New Zealand\n\n\nBut why hexagons?!\nBecause `hexagons are the bestagons <https://www.youtube.com/watch?v=thOifuHs6eY>`_.\nMore seriously, no one grid type works best for all geographic applications.\nMRCagney, this library\'s funder, often works with isochrones, which favour simple convex equal area grids with equidistant neighbour cells, that is, hex gids.\n\n\nAuthors\n============\n- Alex Raichev (2014-09), maintainer\n\n\nInstallation\n============\nInstall from PyPI, e.g. via ``poetry add geohexgrid``.\n\n\nExamples\n=========\nSee the Jupyter notebook at ``notebooks/examples.ipynb``.\n\n\nNotes\n======\n- This project\'s development status is Alpha.\n  Alex uses this project for work and changes it breakingly when it suits his needs.\n- This project uses semantic versioning.\n- Thanks to `MRCagney <https://mrcagney.com>`_ for periodically funding this project.\n- Red Blog Games has a `great write up of hexagonal grids <https://www.redblobgames.com/grids/hexagons>`_ for computer games.\n- Alex wanted to chose a shorter name for this package, such as \'hexgrid\', \'geohex\', or \'hexcover\', but those were already taken or too close to taken on PyPI.\n\n\nChanges\n=======\n\n2.0.0, 2023-11-14\n-----------------\n- Refactored for simpler architecture, gapless grids, and a ~15x speed up in the main function ``grid_from_gdf``.\n\n1.1.0, 2023-10-27\n-----------------\n- Added the ``clip`` option to the function ``grid_from_gdf``.\n- Updated dependencies.\n- Re-ordered functions.\n- Changed the cell ID separotor to a comma.\n\n1.0.0, 2022-08-15\n-----------------\n- First release.',
    'author': 'Alex Raichev',
    'author_email': 'araichev@mrcagney.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/mrcagney/geohexgrid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
