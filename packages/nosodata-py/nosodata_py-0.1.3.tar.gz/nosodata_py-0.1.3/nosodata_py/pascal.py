from struct import Struct

"""
  PascalShortString

  An utility class to help manage Pascal Short Strings 
"""

class PascalShortString:

    def __init__(self, data, size):
        self._data = data
        s = Struct('B'+str(size)+'s')
        str_size, str_container = s.unpack(self._data)
        self._string =  str_container[:str_size].decode('utf-8')        

    def __str__(self):
        return self._string

    @property
    def asBytes(self):
        return self._data
