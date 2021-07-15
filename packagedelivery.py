# Name : Kevin Tivert
# Student ID: 001372496

from priorityqueue import PriorityQueue
from packagehandling import PackageHandling
from formgraph import FormGraph
from truck import Truck
from timing import Timing


# O(n^2)
class PackageDelivery(object):
    # Constructor
    # O(1)
    # This function initializes package delivery object.
    def __init__(self, distances, locations, packages):
        super().__init__()
        self.packages = packages

        hub = locations.search(
            ('4001 South 700 East', 'Salt Lake City', '84107'))

       # Create the three truck instances
        truck_one = Truck('1', distances, hub)
        truck_two = Truck('2', distances, hub)
        truck_three = Truck('3', distances, hub)
        self.trucks = {
            '1': truck_one,
            '2': truck_two,
            '3': truck_three
        }
        # based on specific rules map packages to specific trucks
        self.package_map = {
            '1': ['13', '14', '15', '16', '19', '20'],
            '2': ['3', '18', '36', '38', '6', '25', '28', '32'],
            '3': ['9']
        }

    # start algorithm
    # O(n^2)
    # 
    def run(self):

        # load package 
        for key in self.package_map.keys():
            truck = self.trucks[key]
            packages_ids = self.package_map[key]
            for package_id in packages_ids:
                package = self.packages.search(package_id)
                if truck.load(package) == True:
                    package.truck = truck

        # find all of the packages that have not been placed
        # on a truck and enqueue them in a priority queue
        packages = self.packages.find(lambda p: p.truck == None)
        loading_queue = PriorityQueue()
        for package in packages:
            if package.deadline == '9:00 AM':
                loading_queue.enqueue(package, 3)
            elif package.deadline == '10:30 AM':
                loading_queue.enqueue(package, 2)
            else:
                loading_queue.enqueue(package, 1)

       # prioritize loading truck 1 and later just
        # round the rest of the packages into
        # truck 2 and truck 3
        turns = 1
        while loading_queue.is_empty() == False:
            next_load = loading_queue.dequeue()
            if self.trucks['1'].is_full() == False:
                self.trucks['1'].load(next_load)
            else:
                truck_id = '{}'.format((turns % 2) + 2)
                self.trucks[truck_id].load(next_load)
                turns += 1

        # Run trucks
        self.trucks['1'].leave_hub('8:00 AM')
        self.trucks['2'].leave_hub('9:05 AM')
        self.trucks['3'].leave_hub('10:20 AM')

        print('Total miles traveled: {}'.format(round(self.trucks['1'].traveled + self.trucks['2'].traveled + self.trucks['3'].traveled, 2))) ## format to 2 decimals

        # prompt user for input to query the results
        while True:
            request = input('\nEnter request time (HH:MM AM/PM FORMAT) to request package statuses at a given time: ')
            request_time = Timing(request)
            self.print_package_statuse(request_time)

    # print package statuses at given times
    # O(n^2)
    def print_package_statuse(self, time):
        # load packages
        ls = []
        for i in range(0, len(self.packages.table)):
            for j in range(0, len(self.packages.table[i])):
                ls.append(self.packages.table[i][j])
        # 'Key' function for the sort function
        # O(1)
        def get_key(p):
            return int(p.package_id)

        # sort packages by the package ID
        #O(n)
        packages = sorted(ls, key=get_key)
        # loop through and print package statuses using event time stamps
        for package in packages:
            if package.left_hub_at > time:
                print('At {} the package {} was {}'.format(
                    time, package.package_id, 'AT STORAGE FACILITY (HUB)'))
            elif package.left_hub_at <= time and package.delivered_at > time:
                print('At {} the package {} was {}'.format(
                    time, package.package_id, 'IN TRANSIT'))
            else:
                print('At {} the package {} was {}'.format(
                    time, package.package_id, 'DELIVERED'))