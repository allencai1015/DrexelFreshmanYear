#File:     TestingLinearDS.py
#Purpose:  demo on how to use Python's queue, LifoQueue, and PriorityQueue classes
#Author:   Adelaida Medlock
#Date:     2/16/2020

from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue


class Customer:
    def __init__(self, name, seat):
        self.__name = name
        self.__seat = seat

    def getName(self):
        return self.__name
    
    def getSeat(self):
        return self.__seat
    
    def changeSeat(self, seat):
        self.__seat = seat
    
    def __str__(self):
        return self.__name + ' has seat# ' + str(self.__seat)
    
    def __gt__(self, other):
        return self.__seat > other.__seat    
    
def main():
    # let's create a few objects to place in our queue, stack, and priority stack
    julie = Customer('Julie', 18)
    harry = Customer('Harry', 20)
    marie = Customer('Marie', 15)
    
    # using the Python Queue class 
    q = Queue()
    q.put(julie)
    q.put(harry)
    q.put(marie)
    
    print('Servicing customers in the order they arrived (FIFO):')
    while not q.empty():
        print(q.get())
    print()
        
    # using the Python Stack class --> LifoQueue
    s = LifoQueue()
    s.put(julie)
    s.put(harry)
    s.put(marie)
    
    print('Servicing customers starting with one that arrived last (LIFO):')
    while not s.empty():
        print(s.get())
    print()
    
    # using the Python priority queue class --> PriorityQueue
    p = PriorityQueue()
    p.put(julie)
    p.put(harry)
    p.put(marie)
    
    # seat number is used as the priority: seat ticket number means lower priority
    print('Servicing customers by priority:')
    while not p.empty():
        print(p.get())
    print()  
    
    # another example of priority queue with simple data added to the queue
    tasks = PriorityQueue()

    tasks.put((2, 'code'))
    tasks.put((1, 'eat'))
    tasks.put((3, 'sleep'))
    
    print('Here are tasks in the to-do list, in order of priority:')
    while not tasks.empty():
        next_item = tasks.get()
        print(next_item)
