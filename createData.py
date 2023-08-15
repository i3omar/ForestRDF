"""
Author: Omar Mussa
Date: June 17, 2023
Email: MussaO@cardiff.ac.uk

Description:
This script contains functions for generating and moving polygons within a certain geographical range. 
The polygons can be randomly generated within a specified range and moved in random directions, mimicking 
the movement of an elephant/animal.

Instructions for setting up the virtual environment:

1. Navigate to the directory containing this script.
2. Create a virtual environment using Python's built-in `venv` module (you may need to replace `python3` with `python` or `py` depending on your system setup):
    python3 -m venv env

3. Activate the virtual environment. On Windows, use:
    venv\Scripts\activate
   On Unix or MacOS, use:
    source venv/bin/activate

4. Install the required packages. You can install it using requirements.txt:
pip install -r requirements.txt


You can now run the script using Python:
    python3 createData.py
"""


from faker import Faker
import calendar
import time
from datetime import datetime, timedelta
import random
import string

# 

import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Polygon, Point

import helper


fake = Faker()


Faker.seed(0)

#-----------------------------------------------------

# File Naming
dateName = datetime.now().strftime("%Y_%m_%d-%H%M%S")
outF = open(f"dataset/Forest_synthetic_dataset_{dateName}.ttl", "w")
# 


# This file contains the ttl prefix and sensor description
f = open("dataDefinitions.ttl", "r")
dataDefinitions = f.read()
outF.write(dataDefinitions)
#-----------------------------------------------------

for sensor in helper.sensorsData:
    # >>===============GET observId Result ==================
    # Current GMT time in a tuple format
    current_GMT = time.gmtime()
    # ts stores timestamp
    ts = calendar.timegm(current_GMT)
    observId = ts+random.randint(100000,1000000000)
    # <<=============End of GET observId Result ==================

    baseDT = datetime(2022, 12, 5, 8, 48, 34) #start date
    readingsRate = 3 #number of readings each day
    numberOfReadings = (30*readingsRate)*12 #total number of readings

    sensorName = sensor["name"]
    # record template
    record = helper.recordsTemplates[sensor['templateIndex']]

    # Define a polygon and a range polygon
    range_poly = helper.polygonArray[sensor['areaIndex']] #get a large area polygon
    poly = helper.generate_fixed_size_polygon(range_poly, 100) #define small area within the selected range ploy



    

    placeholders = [tup[1] for tup in string.Formatter().parse(record) if tup[1] is not None]

    # Printing the results.
    for count in range(numberOfReadings):
        observId = observId-1 #get next id
        if count % readingsRate == 0: #if reached the number if readings per day, contintue to the next day.
            baseDT = baseDT - timedelta(1)
        

        poly, direction = helper.elephant_movement(poly, range_poly, random.uniform(0.05, 0.5))


        points = helper.polygon_random_points(poly,1)
        
        p = points[0]

        rtime =  fake.time_object()
        baseDT=baseDT.replace(hour=rtime.hour, minute=rtime.minute, second= rtime.second)

        params = {}

        if 'observationNum' in placeholders:
            params["observationNum"] = observId

        if 'sensorName' in placeholders: 
            params["sensorName"] = sensorName

        if 'resultTime' in placeholders:
            params["resultTime"] = baseDT.isoformat()

        if 'alt' in placeholders:
            params["alt"] = random.randint(-248.0,1195.0)

        if 'lat' in placeholders:
            params["lat"] = p.x

        if 'long' in placeholders: 
            params["long"] = p.y

        if 'temperature' in placeholders: 
            params["temperature"] = round(random.uniform(27.0, 36.6), 1)
        
        if 'extTemp' in placeholders: 
            params["extTemp"] = 0.0

        if 'activity' in placeholders: 
            params["activity"] = 0.0

        if 'direction' in placeholders: 
            params["direction"] = random.randint(0,360)

        if 'speed' in placeholders: 
            params["speed"] = random.randint(0,180)

        if 'PDOP' in placeholders: 
            params["PDOP"] = random.randint(6,82)

        if 'type' in placeholders: 
            params["type"] = random.choice(sensor['type'])

        if 'HDOP' in placeholders:
            type = params.get('type')
            HDOP = sensor.get('HDOP')
            if HDOP is None:
                 params["HDOP"] = random.randint(0,99)
            elif type is None:
                params["HDOP"] = '"{}"^^xsd:float'.format(random.choice(sensor['HDOP']))
            elif params["type"] == "GPS":
                params["HDOP"] = '"{}"^^xsd:float'.format(random.choice(sensor['HDOP']))
            else:
                params["HDOP"] = 'NaN'
        
        if 'cov' in placeholders: 
            params["cov"] = random.randint(0,5)
        
        if 'count' in placeholders: 
            params["count"] = numberOfReadings-count

        if 'distance' in placeholders: 
            params["distance"] = random.randint(0.0,30000.0)

        


        # record = record.format(**params)
        outF.write(record.format(**params))

outF.close()

