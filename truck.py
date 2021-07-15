# Name : Kevin Tivert
# Student ID: 001372496

from set import Set
from timing import Timing
from deliverystatus import IN_ROUTE, DELIVERED

# Calculate route using the nearest node
# Greedy algorithm
# O(n)
def caculate_route(graph, start_location, locations):

    # create a new list with the starting location
    route = [start_location]

    # create a variable that is the current location node
    # and assign it the value of the starting location
    current_loc = start_location

   # Using a while loop iterate until their are no more node in
    # locations list parameter
    while len(locations) > 0:

        # Nearest location
        nearest = None

        # Shortest distance from the current location
        nearest_dist = None

         # Index value of the nearest location
        nearest_location_index = 0

        # Index of the position in the nested loop
        index = 0

        # Loop over the rest of the locations in the
        # list to find a the nearest node
        for loc in locations:
            u = current_loc.graph_index
            v = loc.graph_index
            dist = graph.get_distance(u, v)

            # if the nearest distance isn't defined
            # or the nearest dist is greater than the new dist
            # set the following variables to keep track of
            # current node
            if nearest_dist == None or nearest_dist > dist:
                nearest_dist = dist
                nearest = loc
                nearest_location_index = index
            index += 1

        # Remove the nearest node from the location list
        # and assign the route
        route.append(locations.pop(nearest_location_index))

        # change the current location to the nearest node
        current_loc = nearest

    # Because the trucks need to return the starting point
    # assign the starting location to the end of the route
    route.append(start_location)

    # Use the new route to caculate the overall cost or distance traveled.
    last_stop = None
    cost = 0.0
    for stop in route:
        if last_stop == None:
            last_stop = stop
            continue
        cost = round(
            cost + graph.get_distance(last_stop.graph_index, stop.graph_index), 2)
        last_stop = stop
    return (route, cost)


# O(n^2)
class Truck(object):
    
    # O(1)
    # Constructor 
    # This function initialize the truck object
    def __init__(self, id, graph, start_loc, avg_mph=18.0, max_cap=16):
        super().__init__()
        self.id = id
        self.graph = graph
        self.avg_mph = avg_mph
        self.max_cap = max_cap
        self.packages = []
        self.start_location = start_loc
        self.current_location = start_loc
        self.location_set = Set(lambda l: (l.street, l.city, l.zip_code))
        self.route = []
        self.route_cost = 0.0
        self.traveled = 0.0
        self.current_time = None

    # Load a package onto the truck
    # O(n)
    def load(self, package):
        # Check to make sure the truck could handle another package
        if len(self.packages) == self.max_cap:
            return False
        # Add package to the list of packages
        self.packages.append(package)
        # Try to add the packages delivery address to the location set.
        if self.location_set.add(package.delivery_address) != False:
            # If a new location was added to the set then
            # recalculate the route using nearest neighbor
            result = caculate_route(
                self.graph, self.start_location, list(self.location_set))
            # record the results
            self.route = result[0]
            self.route_cost = result[1]
        return True

    # Check if truck is full
    # O(1)
    def is_full(self):
        return len(self.packages) == self.max_cap

    # Leave the hub
    # O(n^2)
    def leave_hub(self, time):
        # set the current time for the truck to be
        # when it leaves the hub
        self.current_time = Timing(time)
        # Loop through the packages list and update
        # the status of each package
        for package in self.packages:
            package.left_hub_at = Timing(time)
            package.delivery_status = IN_ROUTE
        # Print a message indicating the truck is leaving
        print('Truck {} is leaving at {}'.format(self.id, time))
        # Loop through the route calculating the total time and distance spent
        for i in range(1, len(self.route)):
            currt = self.route[i - 1]
            next = self.route[i]
            distance = self.graph.get_distance(
                currt.graph_index, next.graph_index)
            minutes = (distance/self.avg_mph) * 60.0
            print('Traveling from {} -> {}, distance is {} miles away and it should take {} minutes'.format(
                currt.name, next.name, distance, round(minutes,2))) ## round minutes to 2 decimals
            self.current_location = next
            self.traveled = round(self.traveled + distance, 2)
            self.current_time.add_minutes(minutes)
            # At a stop loop through the list of packages and if the package's
            # delivery address matches record the current time and set the status to DELIVERED
            for package in self.packages:
                if self.current_location == package.delivery_address:
                    package.delivered_at = Timing(self.current_time.hours, self.current_time.minutes)
                    package.delivery_status = DELIVERED
                    deadline = package.deadline
                    if deadline != '':
                        deadline = ', Deadline was {}'.format(deadline)
                    print('Package {} was delivered to {} at {}{}'.format(
                        package.package_id, package.delivery_address, package.delivered_at, deadline))
        print('Final time: {}'.format(self.current_time))
        print('Total Distance: {} miles'.format(self.traveled))
        