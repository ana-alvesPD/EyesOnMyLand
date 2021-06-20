
# coding: utf-8

# In[1]:


#install necessary stuff
get_ipython().system('pip install geopandas')
get_ipython().system('pip install sentinelsat')
get_ipython().system('pip install geojsonio')


# In[2]:


from sentinelsat.sentinel import read_geojson, geojson_to_wkt


#Test params
Query = 'Avelar'
Cloud = '[0,5]'
sort = 'sortParam=cloudCover&sortOrder=ascending'
Satelite = 'Sentinel2'
nIndex = 0
Tipo = 'TrueColor'
ProcessingLevel = 'LEVEL1C'
DataSet = 'ESA-DATASET'

#file geojson for the client land
geo = 'map_avelar.geojson'

#convert geojson for wkt for  API   query
geom = geojson_to_wkt(read_geojson(geo))


#query
URL = 'http://finder.creodias.eu/resto/api/collections/' + Satelite + '/search.json?maxRecords=10&processingLevel=' + ProcessingLevel + '&cloudCover=' + Cloud + '&geometry=' + geom + '&sortParam=startDate&sortOrder=descending&status=all&dataset=' + DataSet

import json, requests, os
products = json.loads(requests.get(URL).text)['features']
for product in products:
    print(product['properties'] ['productIdentifier'])
    
plik = products[nIndex]['properties'] ['productIdentifier']
plik



# # select product and choose bands
# 
# 

# In[3]:


import rasterio

path = plik + '/GRANULE' + '/' +os.listdir(plik + '/GRANULE')[0] + '/IMG_DATA'
if (os.path.isdir(path + '/' + sorted(os.listdir(path))[0])):
    var_apoio = path + '/' + sorted(os.listdir(pasth))[0]
    
band2 = rasterio.open(path + '/' + sorted(os.listdir(path))[1]) #azul
band3 = rasterio.open(path + '/' + sorted(os.listdir(path))[2]) #verde
band4 = rasterio.open(path + '/' + sorted(os.listdir(path))[3]) #red

path


# ## create geotiff

# In[5]:


from rasterio import plot
import matplotlib.pyplot as plt

nome = "test_file"

trueColor = rasterio.open( nome + '.tiff','w',driver='Gtiff',
                          width=band4.width, height=band4.height,
                          count=3,
                          crs=band4.crs,
                          transform=band4.transform,
                          dtype=band4.dtypes[0]
                         )
trueColor.write(band2.read(1), 3) #blue 
trueColor.write(band3.read(1), 2) #green
trueColor.write(band4.read(1), 1) #red
trueColor.close()
os.path.isfile(nome + '.tiff')



# In[6]:


from rasterio.plot import show

fp = 'test_file.tiff'
img = rasterio.open(fp)
show (img)

