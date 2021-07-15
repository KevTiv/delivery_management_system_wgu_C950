# Name : Kevin Tivert
# Student ID: 001372496

# O(1)
class Location:
    # Constructor
    # O(1)
    # This function initializes location object. 
    def __init__(self, name, street, city, state, zip_code, graph_index):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.graph_index = graph_index

    # O(1)
    # This function returns the hash dictionary value of street, city, and zip code. 
    def __hash__(self):
        return hash((self.street, self.city, self.zip_code))

    # O(1)
    # This function returns the stored value in the location list.
    def __eq__(self, value):
        if value == None:
            return False
        if isinstance(value, Location) == True:
            return self.street == value.street and self.city == value.city and self.zip_code == value.zip_code
        else:
            return self.street == value[0] and self.city == value[1] and self.zip_code == value[2]

    # O(1)
    # Overloaded string conversion method to display a strings that represent the hashtable
    # bucket in the hastable is shown as a pointer to a list object.
    def __str__(self):
        return '{}, {}, {} {}'.format(self.street, self.city, self.state, self.zip_code)