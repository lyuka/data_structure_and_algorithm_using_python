# Implementation of Map ADT using a single list.
class myMap:
    # Creates an empty map instance.
    def __init__( self ):
        self._entryList = list()
    
    # Returns the number of entries in the map.
    def __len__( self ):
        return len( self._entryList )

    # Determines if the map contains the given key.
    def __contains__( self, key ):
        ndx = self._findPosition( key )
        return ndx is not None

    # Adds a new entry to the map if the key does exist. Otherwise, the
    # new value replaces the current value assocaited with the key.
    def add( self, key, value ):
        ndx = self._findPosition( key )
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry( key, value )
            self._entryList.append( entry )
            return True

    # Returns the value associated with the key.
    def Valueof( self, key ):
        ndx = self._findPosition( key )
        assert ndx is not None, "Invalid map key. "
        return self._entryList[ndx].value

    # Removes the entry associated with the key.
    def remove( self, key ):
        ndx = self._findPosition( key )
        assert ndx is not None, "Invalid map key. "
        self._entryList.pop( ndx )

    # Returns an iterator for traversing the keys in the map.
    def __iter__( self ):
        return _MapIterator( self._entryList )

    # Helper method used to find the index position of a category. If the
    # key is not found, None is returned.
    def _findPosition( self, key ):
        for i in range( len(self) ):
            if self._entryList[i].key == key:
                return i
        return None

# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

# An iterator for the Map ADT
class _MapIterator:
    def __init__( self, theEntryList ):
        self._entryItems = theEntryList
        self._curItem = 0

    def __iter__( self ):
        return self

    def next( self ):
        if self._curItem < len( self._entryItems ):
            entry = self._entryItems[ self._curItem ]
            self._curItem += 1
            return entry
        else:
            raise StopIteration


if __name__ == '__main__':
    StuMap = myMap()
    print StuMap

    StuMap.add('0301', 'Bell')
    StuMap.add('0302', 'Tang')
    StuMap.add('0303', 'Liu')
    StuMap.add('0304', 'James')
    print StuMap

    for entry in StuMap:
        print entry.key, 
        print entry.value
    print ""

    StuMap.add('0303', 'Ronadol')
    for entry in StuMap:
        print entry.key,
        print entry.value
    print ""
