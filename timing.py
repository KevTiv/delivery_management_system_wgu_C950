# Name : Kevin Tivert
# Student ID: 001372496


# O(1)
class Timing(object):
  
  # O(1)
  # Constructor
  # This function initialize a Timing (time) object
  def __init__(self, *args):
    super().__init__()
    if len(args) == 1:
      time_str = args[0]
      time_str_parts = time_str.split(':')
      hours = float(time_str_parts[0].strip())
      time_str_parts = time_str_parts[1].split(' ')
      minutes = float(time_str_parts[0].strip())
      meridiem = time_str_parts[1].strip()
      if meridiem.upper() == 'AM':
        if hours == 12:
          self.hours = 0
        else:
          self.hours = hours
        self.minutes = minutes
      else:
        self.hours = hours + 12
        self.minutes = minutes
    elif len(args) == 2:
      self.hours = args[0]
      self.minutes = args[1]
    else:
      print('Not Supported')
  
  # O(1)
  # This function adds a given amount of minutes to the minute element.
  def add_minutes(self, minutes):
    combined_minutes = self.minutes + minutes
    if (combined_minutes >= 60):
      hours = (combined_minutes//60)
      self.hours += hours
      combined_minutes = (combined_minutes - (hours * 60))
    self.minutes = combined_minutes

  # O(1)
  # This boolean function check if the programs holds correct time values.
  def __eq__(self, value):
    return self.hours == value.hours and self.minutes == value.minutes
  
  # O(1)
  # This function returns the invert boolean check of eq() function above
  def __ne__(self, value):
    return not self.__eq__(value)

  # O(1)
  # This boolean function returns the comparision of the time value passed as 
  # a parameter and the time value stored in the program.
  def __lt__(self, value):
    if self.hours < value.hours:
      return True
    elif self.hours > value.hours:
      return False
    else:
      if self.minutes < value.minutes:
        return True
      else:
        return False
  
  # O(1)
  # This boolean function returns the comparision of the time value passed as 
  # a parameter and the time value stored in the program.
  def __le__(self, value):
    if self.hours < value.hours:
      return True
    elif self.hours > value.hours:
      return False
    else:
      if self.minutes <= value.minutes:
        return True
      else:
        return False
  
  # O(1)
  # This boolean function returns the comparision of the time value passed as 
  # a parameter and the time value stored in the program.
  def __gt__(self, value):
    if self.hours > value.hours:
      return True
    elif self.hours < value.hours:
      return False
    else:
      if self.minutes > value.minutes:
        return True
      else:
        return False
  
  # O(1)
  # This boolean function returns the comparision of the time value passed as 
  # a parameter and the time value stored in the program.
  def __ge__(self, value):
    if self.hours > value.hours:
      return True
    elif self.hours < value.hours:
      return False
    else:
      if self.minutes >= value.minutes:
        return True
      else:
        return False

  # O(1)
  # Overloaded string conversion function to handle the string conversion of time 
  # object and format time display. 
  def __str__(self):
    meridiem = None
    if self.hours < 12:
      meridiem = 'AM'
    else:
      meridiem = 'PM'
    adjusted_hours = (self.hours % 12)
    if adjusted_hours == 0:
      adjusted_hours += 12
    return '{:02d}:{:02d} {}'.format(int(adjusted_hours), int(self.minutes), meridiem)