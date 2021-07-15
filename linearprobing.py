# Name : Kevin Tivert
# Student ID: 001372496

from emptybucket import EmptyBucket

# HashTable class definition using linear probing
# O(n)
class LinearProbing(object):

    # Constructor
    # HashTable class definition using linear probing
    # O(n)
    # This function creates two instances of empty 
    # bucket and initialize the bucket list to “EMPTY_SINCE_START”.
    def __init__(self, initial_storage=10):
        # Constructor with predefine storage. All buckets are set with an EmptyBucket()
        # instance called self.EMPTY_SINCE_START.
        # 2 instance of EmptyBucket possible

        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        # Initialize all buckets to be EMPTY_SINCE_START.
        self.table = [self.EMPTY_SINCE_START] * initial_storage
    
    # O(n)
    # This function first computes the size of the bucket list, then probe every 
    # bucket using a loop to find the next empty bucket. If a bucket is found the 
    # function insert our item in the bucket and return true otherwise the insert 
    # failed, and the function return false
    def insert(self, item):
        bucket = hash(item) % len(self.table)
        buckets_probed = 0
        while buckets_probed < len(self.table):
            # If the bucket is empty, the item can be assign
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item
                return True

            # If the bucket is not empty, continue probing to the next slot
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # If the entire table is full and the key could not be inserted return false
        return False
    
    # O(n)
    # This function similarly at “insert ()” first determine the size of the list, 
    # then probe through the list using a loop. The function will stop loop if it 
    # founds a bucket that was empty from start or reached the end of the list. 
    # If the function finds the item to delete in a bucket, it will set the bucket 
    # to “EMPTY_AFTER_REMOVAL”. 
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL
            
            # If the bucket was assigned, then continue probing to the next slot.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1
        
    # Search for an item with same key in the hashtable.  Return result
    # O(n)
    # This function uses similar logic to the “remove ()” function but instead return the 
    # item and its index (buckets_probed) if found or return “None” if 
    # nothing was found in the list.
    def search(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                return self.table[bucket]

            # If the bucket was assigned, then continue probing to the next slot.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # If item wasn't found after visiting all possible slot return none.
        print ("Not found")
        return None

    # Overloaded string conversion method to create a strings that represent the hashtable
    # bucket in the hastable is shown as a pointer to a list object.
    # ESS represent EMPTY_SINCE_START
    # EAR represent EMPTY_AFTER_REMOVAL
    # O(1)
    def __str__(self):
        wrd = "   -----\n"
        index = 0
        for bucket in self.table:
            value = str(bucket)
            if bucket is self.EMPTY_SINCE_START: value = 'ESS'
            elif bucket is self.EMPTY_AFTER_REMOVAL: value = 'EAR'
            wrd += '{:2}:|{:^6}|\n'.format(index, value)
            index += 1
        wrd += "   -----"
        return wrd