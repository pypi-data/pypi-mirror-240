import os
import googlemaps
import pandas as pd
import random
import requests

class StreetViewSampler:

    def __init__(self, api_key):

        parent_folder = os.path.dirname(os.path.dirname(__name__))
        self.gmaps = googlemaps.Client(key=api_key)
        self.key = api_key
        self.lat_long = []
    
    def convert_long_lat_to_address(self,location):

        """Converts a latitude/longitude tuple into an 
            address string, returns string

            Parameters:
            ----------------
            location: tuple
                The latitude and longitude to return an address for

            Returns
            ----------------
            address: str
                The street address corresponding to the inputted latitude/longitude
            city: str
                The city name corresponding to the inputted latitude/longitude

            """
        assert type(location) == tuple, f"location expected a non-empty tuple, got {type(location)}"

        # Look up address with reverse geocoding
        reverse_geocode_result = self.gmaps.reverse_geocode(location)
        geocode_components = reverse_geocode_result[0]
        coms = geocode_components['address_components']

        #Breaking down geocode results
        street_number = coms[0]['long_name']
        street_name = coms[1]['long_name']
        city = coms[3]['long_name']
        state = coms[5]['long_name']
        country = coms[6]['long_name']
        postal_code = coms[7]['long_name']

        #Assembling into address
        address = street_number +" "+ street_name +" "+ city +" "+ state +" "+ country +" "+ postal_code

        return city,address
    
    def pull_image(self, city, address, parent_folder, city_count):

        """Takes an addres string as an input and returns an image from google maps streetview api"""

        pic_base = 'https://maps.googleapis.com/maps/api/streetview?'

        # define the params for the picture request
        pic_params = {'key': self.key,
                'location': address,
                'size': "1024x1024"}
        
        #Requesting data
        pic_response = requests.get(pic_base, params=pic_params)
        image_name = city + "_ " + str(city_count) + ".jpg"
        with open(parent_folder +"Data\\Images\\"+ image_name, "wb") as file:
            file.write(pic_response.content)
        
        # Closing connection to API
        pic_response.close()


    def query_random_location(self, location, parent_folder, min_distance = 0.005):

        """
        Takes input city coordinates, adds a random element, 
        and pulls an image from this location
        
        Parameters:
        ----------------
            location: str
                tuple containing latitude and longitude
            parent_folder: str 
                containing reference to parent folder
            min_distance: float
                min allowable distance between images

        ------------------
        OUTPUT:
            None
        """

        #One degree Latitude = 64 miles, taking 1/100 of that
        random_multiplier = 0.02
        random_val = (random.random()-0.5) * random_multiplier
        original_lat, original_long = list(location)[0], list(location)[1]

        #Calculating new latitude and longitude values
        new_lat, new_long = round(original_lat + random_val,6), round(original_long + random_val,6)

        #Ensuring new coordinates sufficiently far from old ones
        while max([new_lat, new_long]) < min_distance and (round(new_lat, 3), round(new_long, 3)) not in self.lat_long:
            new_lat, new_long = round(original_lat + random_val,6), round(original_long + random_val,6)

        #Adding coordinate set to previously called list
        self.lat_long.append((round(new_lat, 3), round(new_long, 3)))
        new_location = (new_lat, new_long)

        #Calling functions
        try:
            city, address = self.convert_long_lat_to_address(self.gmaps,new_location)
            self.pull_image(self.gmaps, city, address,parent_folder,str(new_location))
        except:
            print("No Image for Location")

    def query_multiple_locations(self, cities, return_count, parent_folder):

        """
        Queries multiple location saving images as png files
        
        Parameters:
        ----------------
            cities: Dataframe
                Dataframe containing 3 columns, City, Latitude, and Longitude
            parent_folder: str 
                containing reference to parent folder
            return_count: int
                number of images to query from each city

        ------------------
        OUTPUT:
            None
        """
        for index, row in cities.iterrows():
            location = (row['Latitude'], -row['Longitude'])
            for count in range(return_count):
                self.query_random_location(self.gmaps, location, parent_folder)
