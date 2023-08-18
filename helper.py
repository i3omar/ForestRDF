from faker import Faker
import calendar
import time
from datetime import datetime, timedelta
import random

# 

import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Polygon, Point, box


sensorsData = [
    {'name':"<elephant/Aqeela>", 'templateIndex':0, 'areaIndex':0},
    {'name':"<elephant/Putut>", 'templateIndex':0, 'areaIndex':1},
    {'name':"<elephant/Liun>", 'templateIndex':0, 'areaIndex':2},
    {'name':"<elephant/Abaw>", 'templateIndex':0, 'areaIndex':3},
    {'name':"<elephant/Bikang1>", 'templateIndex':0, 'areaIndex':4},
    {'name':"<elephant/Bikang2>", 'templateIndex':0, 'areaIndex':5},
    {'name':"<elephant/Dara>", 'templateIndex':2, 'areaIndex':0},
    {'name':"<elephant/Guli>", 'templateIndex':0, 'areaIndex':1},
    {'name':"<elephant/Ita>", 'templateIndex':0, 'areaIndex':2},
    {'name':"<elephant/Jasmin>", 'templateIndex':0, 'areaIndex':3},
    {'name':"<elephant/Jasper>", 'templateIndex':0, 'areaIndex':4},
    {'name':"<elephant/Kasih>", 'templateIndex':2, 'areaIndex':5},
    {'name':"<elephant/Kuma>", 'templateIndex':0, 'areaIndex':0},
    {'name':"<elephant/Maliau>", 'templateIndex':0, 'areaIndex':1},
    {'name':"<elephant/Merotai>", 'templateIndex':0, 'areaIndex':2},
    {'name':"<elephant/Puteri>", 'templateIndex':0, 'areaIndex':3},
    {'name':"<elephant/Sandi>", 'templateIndex':0, 'areaIndex':4},
    {'name':"<elephant/Sejati>", 'templateIndex':0, 'areaIndex':5},
    {'name':"<elephant/Tulid>", 'templateIndex':0, 'areaIndex':0},
    {'name':"<elephant/Seri>", 'templateIndex':0, 'areaIndex':1},
    {'name':"<elephant/Tunglap>", 'templateIndex':0, 'areaIndex':2},
    {'name':"<elephant/Umas2>", 'templateIndex':0, 'areaIndex':3},
    {'name':"<python/Juling>", 'templateIndex':1, 'areaIndex':4, 'type':["VHF","GPS"], 'HDOP':[10,20,30,40]},
]


recordsTemplates = [
    """
<observation/{observationNum}> a sosa:Observation ; 
    sosa:madeBySensor {sensorName} ;
    sosa:resultTime "{resultTime}"^^xsd:dateTime ;
    <property/temperature> "{temperature}"^^xsd:float ;
    <property/direction> "{direction}"^^xsd:float ;
    <property/speed> "{speed}"^^xsd:float ;
    <property/PDOP> "{PDOP}"^^xsd:integer ;
    geo:alt "{alt}"^^xsd:float ;
    geo:lat "{lat}"^^xsd:float ;
    geo:long "{long}"^^xsd:float .""",

    """
<observation/{observationNum}> a sosa:Observation ; 
    sosa:madeBySensor {sensorName} ;
    sosa:resultTime "{resultTime}"^^xsd:dateTime ;
    <property/speed> "{speed}"^^xsd:float ;
    <property/HDOP> {HDOP};
    <property/type> "{type}"^^xsd:string;
    geo:lat "{lat}"^^xsd:float ;
    geo:long "{long}"^^xsd:float .""",

    """
<observation/{observationNum}> a sosa:Observation ; 
    sosa:madeBySensor {sensorName} ;
    sosa:resultTime "{resultTime}"^^xsd:dateTime ;
    <property/activity> "{activity}"^^xsd:float ;
    <property/temperature> "{temperature}"^^xsd:float ;
    <property/extTemp> "{extTemp}"^^xsd:float ;
    <property/direction> "{direction}"^^xsd:float ;
    <property/speed> "{speed}"^^xsd:float ;
    <property/PDOP> "{HDOP}"^^xsd:integer ;
    <property/count> "{count}"^^xsd:integer ;
    <property/cov> "{cov}"^^xsd:integer ;
    <property/distance> "{distance}"^^xsd:float ;
    geo:alt "{alt}"^^xsd:float ;
    geo:lat "{lat}"^^xsd:float ;
    geo:long "{long}"^^xsd:float .""",

    """
    """

]

polygonArray = [
    Polygon([
        [ 6.0719851355920875, 116.55986706493424 ],
        [ 6.039551917768937, 116.59643288701774 ],
        [ 6.104085921628729, 116.64716163184495 ],
        [ 6.09245647971452, 116.74739842303097 ],
        [ 6.211349144491809, 116.77658182103187 ],
        [ 6.242721429275905, 116.74866534769536 ],
        [ 6.231772502291595, 116.68761956971142 ],
        [ 6.1999429744869134, 116.72664240002634 ],
        [ 6.140207116541685, 116.702702594921 ],
        [ 6.155667164732214, 116.61041788291188 ],
        [ 6.0719851355920875, 116.55986706493424 ],
    ]),
    Polygon([
        [ 5.4336230112292725, 117.96408967114986 ],
        [ 5.383253913139357, 117.93773688375951 ],
        [ 5.322407881730036, 118.08819690719248 ],
        [ 5.3135057241039, 118.20374982431532 ],
        [ 5.373645229698356, 118.36499618366364 ],
        [ 5.407055368545314, 118.40435282327236 ],
        [ 5.446911817153889, 118.3559488411993 ],
        [ 5.400134145229028, 118.24630273506047 ],
        [ 5.3877458911614715, 118.15612204838546 ],
        [ 5.391045862028463, 118.06428966578098 ],
        [ 5.4336230112292725, 117.96408967114986 ],
    ]),
    Polygon([
        [ 5.706628338215898, 118.39605616405609 ],
        [ 5.707485351583075, 118.32810700871052 ],
        [ 5.586450133883838, 118.30740664154294 ],
        [ 5.543210598763509, 118.28095151111486 ],
        [ 5.5239593653167605, 118.26236187480391 ],
        [ 5.501729710002416, 118.24087914079429 ],
        [ 5.441915000561515, 118.19218690507115 ],
        [ 5.423948789017941, 118.25270692817868 ],
        [ 5.469108763267719, 118.31469881348313 ],
        [ 5.583896196576098, 118.38032852858306 ],
        [ 5.706628338215898, 118.39605616405609 ],
    ]),
    Polygon([
        [ 5.466746185070319, 118.34283034550027 ],
        [ 5.530327275805038, 118.16209304379302 ],
        [ 5.536764446418726, 118.06105389492589 ],
        [ 5.514136428638183, 117.98911738442258 ],
        [ 5.477900003698127, 117.94355155667292 ],
        [ 5.450413306333937, 118.0039639142342 ],
        [ 5.457800960964923, 118.14718955894934 ],
        [ 5.402052005087633, 118.31681115785616 ],
        [ 5.466746185070319, 118.34283034550027 ],

    ]),
    Polygon([
        [ 5.566739939781497, 117.95747544849291 ],
        [ 5.390495854221182, 117.63869310496378 ],
        [ 5.336440206592414, 117.6870066043921 ],
        [ 5.50590684705159, 118.00623691873626 ],
        [ 5.566739939781497, 117.95747544849291 ],
    ]),
    Polygon([
        [ 5.297383432945229, 117.71266941446811 ],
        [ 5.215451677644638, 117.78210007119927 ],
        [ 5.398738825977969, 117.99086612183602 ],
        [ 5.447858282606069, 118.18704205099495 ],
        [ 5.590260622681763, 118.16104038152847 ],
        [ 5.475516726241566, 117.96245666686447 ],
        [ 5.297383432945229, 117.71266941446811 ],
    ]),
    
]
# == Supplementary functions =====================================================

# Function to generate a random fixed-size polygon within a range
def generate_fixed_size_polygon(range_poly, side_length_meters):
    METERS_TO_DEGREES = 1 / 111320
    side_length_degrees = side_length_meters * METERS_TO_DEGREES
    minx, miny, maxx, maxy = range_poly.bounds
    while True:
        # Randomly generate the min x and y values for the new polygon
        poly_minx = random.uniform(minx, maxx - side_length_degrees)
        poly_miny = random.uniform(miny, maxy - side_length_degrees)
        # Create a new polygon (as a box)
        new_poly = box(poly_minx, poly_miny, poly_minx + side_length_degrees, poly_miny + side_length_degrees)
        # Check if the new polygon is within the range polygon
        if new_poly.within(range_poly):
            return new_poly

        
def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)
    return points


# Moves the polygon to the specified direction
def move_polygon(polygon, direction, distance):
    lat_change = distance / 111.32
    lon_change = distance / 85
    if direction.lower() == 'north':
        lat_change *= 1
    elif direction.lower() == 'south':
        lat_change *= -1
    elif direction.lower() == 'east':
        lon_change *= 1
    elif direction.lower() == 'west':
        lon_change *= -1
    new_polygon_coords = [(lat + lat_change, lon + lon_change) for (lat, lon) in list(polygon.exterior.coords)]
    new_polygon = Polygon(new_polygon_coords)
    return new_polygon


# Moves the polygon to a new location, ensuring that it stays within a specific range
def move_within_range(original_polygon, range_polygon, distance, tried_directions = None):
    if tried_directions is None:
        tried_directions = []
    directions = ['north', 'south', 'east', 'west']

    if len(tried_directions) == len(directions):  # All directions have been tried
        return original_polygon
    
    # Choose a random direction not tried before
    direction = random.choice([dir for dir in directions if dir not in tried_directions])
    tried_directions.append(direction)

    new_polygon = move_polygon(original_polygon, direction, distance)
    # If the new position is not within the range polygon, try another direction
    if not new_polygon.within(range_polygon):
        return move_within_range(original_polygon, range_polygon, distance, tried_directions)  # Try again with another direction
    return new_polygon

# Imitate elephant's movement within a specific range
def elephant_movement(original_polygon, range_polygon, distance, previous_direction=None):
    directions = ['north', 'south', 'east', 'west']
    # If there was a previous direction, follow the same direction with a 75% probability
    if previous_direction and random.random() < 0.75:
        direction = previous_direction
    else:
        direction = random.choice(directions)
    new_polygon = move_polygon(original_polygon, direction, distance)
    if not new_polygon.within(range_polygon):
        return original_polygon, previous_direction  # If new position is not within the range, don't move
    return new_polygon, direction  # Return the new position and the chosen direction


# =================================================================================