import numpy
import datacube
dc = datacube.Datacube(app = 'my_app', config = '/home/localuser/.datacube.conf')

import utils.data_cube_utilities.data_access_api as dc_api  
api = dc_api.DataAccessApi(config = '/home/localuser/.datacube.conf')


# <hr>  
# 
# ## <a id="plat_prod">Select the Product and Platform</a>  [&#9652;](#top)

# In[2]:


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


# <hr>  
# 
# ## <a id="extents">Determine the Extents of the Data</a>  [&#9652;](#top)

# In[3]:


latitude_extents = (min(extents['latitude'].values),max(extents['latitude'].values))
longitude_extents = (min(extents['longitude'].values),max(extents['longitude'].values))
time_extents = (min(extents['time'].values),max(extents['time'].values))
print(time_extents)


# <hr>  
# 
# ## <a id="define_extents">Define the Region to Be Examined</a>  [&#9652;](#top)

# In[4]:


from utils.data_cube_utilities.dc_display_map import display_map

display_map(latitude_extents, longitude_extents)

print(dc.list_products())