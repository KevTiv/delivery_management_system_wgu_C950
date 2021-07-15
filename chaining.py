# Name : Kevin Tivert
# Student ID: 001372496

# Use of hashtable to store necessary data
# O(n)
class Chaining(object):

    # Constructor
    # Constructor with predefine storage capacity
    # Assigns all buckets with an empty list.
    # O(1)
    def __init__(self, inital_storage=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(inital_storage):
            self.table.append([])
    
    # Assign a new item 
    # Function will first determine the length of the current list then 
    # assign the new object at the end of the existing bucket list or 
    # create a new bucket list. 
    # O(1)
    def insert(self, item):
        
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

       # Assign the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for item with same key in the hash table and return result
    # Similar as the insert () function this function will first determine 
    # the size of the list and using a loop, the function will go through the 
    # list and compare every single object until one matches our search object 
    # or will return none
    # O(n)
    def search(self, key):
        
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # No key found
            print("No Result")
            return None

     # Remove an item with same key from the hash table.
     # The function will first determine the size of the list, go through the list 
     # using a loop and compare object in the list with the given object (key) the 
     # function has to remove. If the key is found in the list, it will be removed 
     # but if it is not found the function will go through the list and end.
    # O(n)
    def remove(self, key):
        
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is found
        if key in bucket_list:
            bucket_list.remove(key)

    # Overloaded string conversion method to create a strings that represent the hashtable
    # bucket in the hastable is shown as a pointer to a list object.
    # O(1)
    def __str__(self):
        index = 0
        wrd =  "   -----\n"
        for bucket in self.table:
            wrd += "%2d:|   ---|-->%s\n" % (index, bucket)
            index += 1
        wrd += "   -----"
        return wrd