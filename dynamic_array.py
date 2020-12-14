# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Abhimanyu, bais

import numpy as np

class DynamicArray:

    def __init__(self):
        self.capacity = 10
        rocky = np.empty(self.capacity, object)
        self.data = rocky
        self.howMuchStuff = 0
        self.next_index = 0

    def __len__(self):
        return self.howMuchStuff

    def __getitem__(self, item):
        if item < 0 or item > self.howMuchStuff-1:
            raise IndexError('index out of range')
        return self.data[item]

    def next_index(self):
        return self.next_index

    def append(self, thingYouWantToAppend):
        self.data[self.howMuchStuff] = thingYouWantToAppend
        self.howMuchStuff += 1
        self.next_index += 1

    def is_empty(self):
        if self.howMuchStuff == 0:
            return True
        elif self.howMuchStuff != 0:
            return False

    def clear(self):
        a2 = DynamicArray
        self.data = a2
        self.howMuchStuff = 0
        self.next_index = 0

    def pop(self):
        self.data[self.howMuchStuff - 1] = None








