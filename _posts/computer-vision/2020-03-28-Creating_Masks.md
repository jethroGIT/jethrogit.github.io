---
layout: post
title: Creating Mask Images from Shapely Polygons
category: Computer-Vision
lang: EN
description: How to Create Mask Images from Polygons
---

This tutorial will show you how to create a mask from [Shapely](https://shapely.readthedocs.io/en/stable/manual.html) polygons. Specifically, a Shapely polygon has a [WKT format](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) and we will convert this WKT format into a mask. OK, concretely, suppose we have installed [Shapely library](https://pypi.org/project/Shapely), [Anaconda](https://www.anaconda.com/distribution), and had _an image like the one on left side of images below_. In this tutorial, we will convert _this image_ into _a mask image like the one on the right side_.  

{: .center-image }
[![img4]({{ site.baseurl }}/assets/images/palu-tsunami_00000195_pre_disaster.png){:class="img-resize-2"}]({{ site.baseurl }}/assets/images/palu-tsunami_00000195_pre_disaster.png)
[![img5]({{ site.baseurl }}/assets/images/palu-tsunami_00000195_pre_disaster_mask.png){:class="img-resize-2"}]({{ site.baseurl }}/assets/images/palu-tsunami_00000195_pre_disaster_mask.png)

The image on right side is called a mask image. It contains only binary pixels (_black_ and _white_). Particularly, this mask contains _black pixels as buildings_ and _white pixels otherwise_. 

Let's get started with the code!
We are going to show all these codes as _codes in Jupyter notebook cells_. 

Firstly, we import the libraries
```python
%reload_ext autoreload
%autoreload 2
%matplotlib inline

import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image
import numpy as np
import skimage.io

# To read files in a directory
from os import listdir
from os.path import isfile, join

# To load wkt; this is a specific method in shapely library 
from shapely.wkt import loads
```

Next, we construct paths to _the images_, _the binary labels_ where the masks will be saved, and _the labels_ where the json files are saved. 

```python
# We construct the path to the image 
images_path = Path('/home/hbunyamin/Datasets/asses-building-damage/train/images')

# We construct the path to label path where we want to put the mask image 
label_path = Path('/home/hbunyamin/Datasets/asses-building-damage/train/binaryLabels')

# We construct the path to the json file; the json file contains 
json_path  = Path('/home/hbunyamin/Datasets/asses-building-damage/train/labels')
```

Then, we put all the image files in a list.

```python
list_files = [f for f in listdir(images_path) if isfile(join(images_path, f))]
```

Finally, we process all the images and convert them into mask images.

```python
counter = 0

for img_name in list_files:
    # split the file name
    prefix_file_name = img_name.split(".")
    
    # construct the path to the image
    temp_image_path = images_path / img_name    
    
    # construct the path to the json    
    temp_json_path = json_path / (prefix_file_name[0]+".json")
    
    # read the json
    json_dict = None 
    with open(temp_json_path, 'r') as read_file:
        json_dict = json.load(read_file)  
    
    # construct the list of xy of buildings
    props_xy_list = json_dict['features']['xy']     
    
    # construct list of polygons 
    polygon_geom_list = []
    for prop in props_xy_list:
        polygon_temp = loads(prop['wkt'])
        polygon_geom_list.append(polygon_temp)    
    
    # read the image which we want to draw the polygons
    the_image = skimage.io.imread( temp_image_path )    
    
    # Create the basic mask
    a_mask = np.ones(shape=the_image.shape[0:2], dtype="bool") # original
    
    # For each polygon, draw the polygon inside the mask
    for polygon_geom in polygon_geom_list:
        poly_coordinates = np.array(list(polygon_geom.exterior.coords))
        rr, cc = polygon(poly_coordinates[:,0], poly_coordinates[:,1], the_image.shape)
        a_mask[cc,rr] = False        
    
    # Convert numpy array of the mask into an image with the help of PIL
    mask_image = Image.fromarray(a_mask)
    
    # Save the image of the mask into the "binaryLabels" folder 
    mask_image.save( label_path / (prefix_file_name[0]+"_mask.png"), format="PNG" )
    
    # For debugging purposes
    if counter % 1000 == 0:
        print("Number of images have been processed:", counter)
    counter += 1
```

For conclusion, all _the mask images_ are saved in `label_path`. 