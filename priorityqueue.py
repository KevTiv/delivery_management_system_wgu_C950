# Name : Kevin Tivert
# Student ID: 001372496

# O(1)
class QElement(object):
  # Constructor
  # O(1)
  # This funtion initialize the queue object.
  def __init__(self, element, priority):
    super().__init__()
    self.element = element
    self.priority = priority

# O(n)
class PriorityQueue(object):
  # Constructor
  # O(1)
  # This function initialize the priority queue object
  def __init__(self):
    super().__init__()
    self.items = []

  # This function check if queue is empty
  # O(1)
  def is_empty(self):
    return len(self.items) == 0

  # This function enqueue a new element
  # O(n)
  def enqueue(self, element, priority):
    # Construct new queue element with element 
    # object and it's priority status
    q_element = QElement(element, priority)
    contain = False

    # loop through queue
    for u in range(0, len(self.items)):
      # If an item is found with lower or equal 
      # priority assign new element 
      # in it's position and shift the rest of 
      # items one position back
      if self.items[u].priority <= q_element.priority:
        self.items.insert(u, q_element)
        contain = True
        break
    # If the new element has lower priority than everything
    # else in the list append it to the back
    if contain == False:
      self.items.append(q_element)

  # This function pop the element from the front of the queue off and return it
  # O(1)
  def dequeue(self):
    if self.is_empty():
      return 'Underflow'
    return self.items.pop(0).element

  # This function take peek at what element is at the back of the queue
  # O(1)
  def rear(self):
    if self.is_empty():
      return 'No elements in Queue'
    return self.items[len(self.items) - 1].element

  # This function take a peek at what element is at the front of the queue
  # O(1)
  def front(self):
    if self.is_empty():
      return 'No elements in Queue'
    return self.items[0].element

  