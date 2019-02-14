mylist = ["eating", "sleeping", "cutting sheet"]
class Bag ():
    def __init__(self):
        self._theBag = list()

    #a method to add items to the bag
    def additems(self,item):
        return self._theBag.append(item)
    def number_of_items(self):
        return len(self._theBag)
    def bag_items(self, item):
        return item in self._theBag 

    def random_removal(self, _theBag):
        for item in self._theBag:
            return self._theBag.remove(item)


kendo = Bag.additems("eating", mylist)
print (kendo)

