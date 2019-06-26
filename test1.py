import numpy
import datacube
from datetime import datetime
dc = datacube.Datacube(app = 'my_app', config = '/home/localuser/.datacube.conf')

import utils.data_cube_utilities.data_access_api as dc_api  
api = dc_api.DataAccessApi(config = '/home/localuser/.datacube.conf')

# Change the data platform and data cube here

platform = "LANDSAT_7"
# platform = "LANDSAT_8"

# product = "ls7_ledaps_ghana"
product = "ls7_ledaps_general"
# product = "ls7_ledaps_senegal"
# product = "ls7_ledaps_sierra_leone"
# product = "ls7_ledaps_tanzania"
# product = "ls7_ledaps_vietnam"

# Get Extents
extents = api.get_full_dataset_extent(platform = platform, product = product)

latitude_extents = (min(extents['latitude'].values),max(extents['latitude'].values))
longitude_extents = (min(extents['longitude'].values),max(extents['longitude'].values))
#time_extents = (min(extents['time'].values),max(extents['time'].values))
start_date = datetime(2015,12,12)
end_date = datetime(2015,12,12)
date_range = (start_date,end_date)
#print(time_extents)

from utils.data_cube_utilities.dc_display_map import display_map

display_map(latitude_extents, longitude_extents)

dc.load(product=product, platform=platform, lat=latitude_extents, lon=longitude_extents, time=date_range)