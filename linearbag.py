class Bag:
    #constructs an empty bag
    def __init__(self):
        self._theItems = list()

    #returns the number of items in the bag    
    def __len__(self):
        return len(self._theItems)

    #determines if an item is contained in the bag
    def __contains__(self,item):
        return item in self._theItems
    #adds an item to the bag
    def add(self, item):
        self._theItems.append(item)
    #removes and returns an instance of the item from the bag
    def remove(self, item):
        assert item in self._theItems, "The item must be in the bag "
        ndx =self._theItems.index(item)  
        return self._theItems.pop(ndx) 
    #itereator for traversing the list
    #def __iter__(self, item):
        #return item
        #pass

class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem +=1
            return item
        else:
            raise StopIteration    
