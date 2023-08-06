from struct import Struct
from .pascal import PascalShortString

"""
   NosoFileStream

   Wrapping binary reads and struct in a simpler package
"""

class NosoFileStream:

    """
      TODO:
        - Implement the write methods, maybe?
        - Implement seek, maybe?
    """
    
    def __init__(self, filename):
        self.f = open(filename, 'rb')

    def read_int(self):
        s = Struct('i')
        data = self.f.read(s.size)
        result, = s.unpack(data)
        return result

    def read_int64(self):
        s = Struct('q')
        data = self.f.read(s.size)
        result, = s.unpack(data)
        return result

    def read_pas_str(self, size):
        data = self.f.read(size + 1)
        result = PascalShortString(data, size)
        return result

    def close(self):
        self.f.close()

class NosoMemStream:
    
    """
      TODO:
        - Implement the read methods, maybe?
        - Implement seek, maybe?
    """
    
    def __init__(self):
        self._data = bytearray()

    def write_int(self, data):
        s = Struct('i')
        self._data += s.pack(data)

    def write_int64(self, data):
        s = Struct('q')
        self._data += s.pack(data)

    def write_pas_str(self, data):
        self._data += data

    @property
    def asByteArray(self):
        return self._data
