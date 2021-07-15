# Name : Kevin Tivert
# Student ID: 001372496

from dataload import DataLoad
from location import Location
from linearprobing import LinearProbing
from packagehandling import PackageHandling
from formgraph import FormGraph
from packagedelivery import PackageDelivery

# Create a dataload object
data_loader = DataLoad()

def distance_graph():     # O(n^2)
    # load distance 
    distance_data = data_loader.load_distance_data_csv('./data/distance_data.csv')
    # construct graph
    graph = FormGraph(len(distance_data))
    # populate graph 
    for i in range(0, len(distance_data)):
        for j in range(0, len(distance_data[i])):
            graph.add_edge(i, j, distance_data[i][j])
    return graph

def location_table():     # O(n)
    # load location 
    location_data = data_loader.load_location_data_csv('./data/location_data.csv')     
    # construct hashtable 
    location_table = LinearProbing(len(location_data))
    # populate location table
    for element in location_data:
        name = element['name']
        street = element['street']
        city = element['city']
        state = element['state']
        zip_code = element['zip_code']
        index = element['index']
        location = Location(name, street, city, state, zip_code, index)
        location_table.insert(location)
    return location_table

def packages_table(locatons):     # O(n)
    # construct package table
    package = PackageHandling(locatons)
    # load package 
    package_data = data_loader.load_package_data_csv('./data/package_data.csv')
    # populate the hash table
    for element in package_data:
        package_id = element['package_id']
        delivery_address = element['delivery_address']
        city = element['city']
        zip_code = element['zip_code']
        weight = element['weight']
        deadline = element['deadline']
        package.insert(package_id, delivery_address, deadline, city, zip_code, weight)
    return package

# Main program
def main():
    # create program (C950 Project) structures
    distances_graph = distance_graph()  # O(n)
    locations = location_table()   # O(n)
    packages = packages_table(locations)   # O(n)

    ## constuct application runner
    delivery = PackageDelivery(distances_graph, locations, packages)  # O(n)

    # run application
    
    delivery.run()

if __name__ == '__main__':
    main()
    