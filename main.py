# Libraries
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Set the dimension of the figure
my_dpi = 96
plt.figure(figsize=(2600 / my_dpi, 1800 / my_dpi), dpi=my_dpi)

coords = {
    "Boston, MA": [42.3, 71.0],
    "Columbus, OH": [39.9, 82.9],
    "Denver, CO": [39.7, 104],
    "Detroit, MI": [42.3, 83.0],
    "Fort Worth (Tarrant County), TX": [32.7, 97.3],
    "Indianapolis (Marion County), IN": [39.8, 86.1],
    "Kansas City, MO": [39.0, 94.5],
    "Las Vegas (Clark County), NV": [36.2, 115.1],
    "Long Beach, CA": [33.8, 118.1],
    "Miami (Miami-Dade County), FL": [25.78, 80.2],
    "Minneapolis, MN": [45.0, 93.3],
    "New York City, NY": [40.7, 74.0],
    "Oakland (Alameda County), CA": [37.8, 122.3],
    "Philadelphia, PA": [40.0, 75.2],
    "Portland (Multnomah County), OR": [45.5, 122.7],
    "San Antonio, TX": [29.4, 98.5],
    "San Diego County, CA": [32.7, 117.2],
    "Seattle, WA": [47.6, 122.3]
}

values = {
    "Boston, MA": -53.6166,
    "Columbus, OH": 23.9012,
    "Denver, CO": -3.7039,
    "Detroit, MI": 72.6978,
    "Fort Worth (Tarrant County), TX": -29.9003,
    "Indianapolis (Marion County), IN": -23.2846,
    "Kansas City, MO": -1.8935,
    "Las Vegas (Clark County), NV": 51.5984,
    "Long Beach, CA": 17.3787,
    "Miami (Miami-Dade County), FL": -16.8231,
    "Minneapolis, MN": -49.0803,
    "New York City, NY": -1.9516,
    "Oakland (Alameda County), CA": -34.3285,
    "Philadelphia, PA": -0.06300,
    "Portland (Multnomah County), OR": -32.1585,
    "San Antonio, TX": 170.25,
    "San Diego County, CA": -32.2585,
    "Seattle, WA": -56.7666,
}
lllon = -140
urlon = -64
lllat = 22.0
urlat = 50.5

# Make the background map
m = Basemap(projection='cyl', llcrnrlon=lllon, llcrnrlat=lllat, urcrnrlon=urlon, urcrnrlat=urlat, resolution='h')
m.drawmapboundary(fill_color='white', linewidth=0)
m.fillcontinents(color='black', alpha=0.1)
m.drawcoastlines(linewidth=0.1, color="white")
shp_info = m.readshapefile('cb_2018_us_state_500k', 'states',
                               drawbounds=True, color='white')

for city, value in values.items():
    # What color is this county?
    smin = 0
    smax = 1

    max_pos_value = max(values.values())
    min_neg_value = min(values.values())


    if value >= 0:
        max_value = max_pos_value
        newvalue = (value - 0) * (smax - smin) / (max_value - 0) + smin
        color = np.array([newvalue, 0, 0])
        #for non col
        color = '#D50000'
        print(city, color)
    else:
        max_value = -min_neg_value
        value = -value
        newvalue = (value - 0) * (smax - smin) / (max_value - 0) + smin
        color = np.array([0, newvalue, 0])
        color = '#64DD17'

        print(city, color)

    coord = coords.get(city)
    x, y = m(-coord[1], coord[0])
    print(value)
    m.scatter(x, y, s=value*30, alpha=0.7, c=color, cmap="Set1")


for key in values:
    coord = coords.get(key)
    x, y = m(-coord[1], coord[0])
    # plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, key, fontsize=10)

# Title/label text
# plt.text(-170, -58,'Text',ha='left', va='bottom', size=9, color='#555555')

# Save as png
plt.savefig('data_map.png', bbox_inches='tight')

plt.show()


