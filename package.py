# Name : Kevin Tivert
# Student ID: 001372496

# O(1)
class Package:
    # Constructor
    # O(1)
    # This function initializes the package object.
    def __init__(self, package_id, delivery_address, deadline, weight, delivery_status):
        self.package_id = package_id
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.weight = weight
        self.delivery_status = delivery_status
        self.truck = None
        self.left_hub_at = None
        self.delivered_at = None

    # O(1)
    # This function using the package ID as parameter return the package stored 
    # value in the location bucket list. 
    def __hash__(self):
        return hash(self.package_id)

    # O(1)
    # This Boolean function check confirms the key passed as a parameter 
    # is the same the package ID. 
    def __eq__(self, key):
        return self.package_id == key