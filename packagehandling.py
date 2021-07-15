# Name : Kevin Tivert
# Student ID: 001372496

from chaining import Chaining
from package import Package
from deliverystatus import AVAILABLE_AT_HUB
from set import Set


# Use of hashtable to store necessary data
# O(n)
class PackageHandling(Chaining):
    # O(1)
    def __init__(self, locations, initial_storage=40):
    # Constructor with predefine storage capacity
    # Assigns all buckets with an empty list.
        self.locations = locations
        super().__init__(initial_storage)

    # Add a new item to the hastable
    # O(n)
    def insert(self, package_id, delivery_address, deadline, city, zip_code, weight, delivery_status=AVAILABLE_AT_HUB):
        
        location = self.locations.search((delivery_address, city, zip_code))
        # construct package object
        package = Package(package_id, location, deadline, weight, delivery_status)
        # insert in the hash table
        return super().insert(package)

    # Searches for item with same key in the hash table and return result
    # O(n)
    def search(self, package_id):
        # find package id
        package = super().search(package_id)
        return package

    # use set operations in the hash table
    # O(n^2)
    def find(self, predicate):
        # get_key function for packages set
        # O(1)
        def get_key(el):
            return el.package_id
        # construct a pacakges set 
        packages_set = Set(get_key)
        # copy all of the elements from the hash table into
        # a list
        table = list(self.table)
       # iterate over the list and any sub lists to assign 
       # the pacakge values into the package set
        for bucket in table:
            for package in bucket:
                packages_set.add(package)
        # Predicate set and return result 
        return list(packages_set.filter(predicate))