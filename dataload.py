# Name : Kevin Tivert
# Student ID: 001372496

import csv
import json

# O(n^2)
class DataLoad(object):
  def __init__(self):
    super().__init__()

  # Distance
  # O(n^2)
  # Read line in the csv document,parse values and append to the ADT
  # This function will open the csv file with the distance data and copy this data 
  # into a float list. The resulting list will be used at a later stage in 
  # the “main.py”.
  def load_distance_data_csv(self, file):
    distance_data = []

    def convert_to_float(distance_str):
      distance = float(distance_str.strip())
      return distance

    # Open file
    with open(file, newline='', encoding='utf-8-sig') as distances_file:
      # Construct reader object
      reader = csv.reader(distances_file)
      # read each line in the file
      for row in reader:
        # map the string distance values into floating point number and
        # add them to a list which in turn is added to another list
        distances_row_data_list = list(map(convert_to_float, list(row)))
        distance_data.append(distances_row_data_list)
    return distance_data


  # read each line of the csv file, parse into dictionary of key value pairs, and append to list
  # O(n^2)
  # This function will open the csv file with the location data and copy this data into a dictionary 
  # list. The resulting dictionary list will be used at a later stage in the “main.py”. 
  def load_location_data_csv(self, file):
    location_data = []
    row_index = 0
    # Open file
    with open(file, newline='', encoding='utf-8-sig') as locations_file:
      # construct reader object
      reader = csv.reader(locations_file)
      # read each line of the file
      for row in reader:
        # parse into a dictionary for easy data access later
        loc_data = {
          'index': row_index,
          'name': row[0].strip(),
          'street': row[1].strip(),
          'city': row[2].strip(),
          'state': row[3].strip(),
          'zip_code': row[4].strip()
        }
        # append to list
        location_data.append(loc_data)
        row_index += 1
    return location_data

  # read each line of the csv file, parse into dictionary of key value pairs, and append to list
  # O(n^2)
  # This function will open the csv file with the package data and copy this data 
  # into a dictionary list. The resulting dictionary list will be used at a later 
  # stage in the “main.py”.
  def load_package_data_csv(self, file):
    package_data = []
    # Open file
    with open(file, newline='', encoding='utf-8-sig') as packages_file:
      # create a reader object
      reader = csv.reader(packages_file)
      # read each line of the file
      for row in reader:
        # parse into a dictionary for easy data access later
        pckg_data = {
          'package_id': row[0].strip(),
          'delivery_address': row[1].strip(),
          'city': row[2].strip(),
          'zip_code': row[4].strip(),
          'weight': row[5].strip(),
          'deadline': row[6].strip()
        }
        # append to list
        package_data.append(pckg_data)
    return package_data