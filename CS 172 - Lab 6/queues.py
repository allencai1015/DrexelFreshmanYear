#File:     queuesDemo.py
#Purpose:  implement our our version of a queue
#Author:   Adelaida A. Medlock
#Date:     2/16/2020

class MyQueue():
    def __init__(self):
        self.__theList = []
    
    def __str__(self):
        s = ''
        for i in range(0, len(self.__theList)) :
            s = s + str(i) + ": " + str(self.__theList[i]) + '\n'
        return s
    
    def put(self, item):
        self.__theList.append(item)
    
    def get(self):
        a = self.__theList.pop(0)
        return a
    
    def clear(self):
        self.__theList = []
        
    def empty(self):
        if len(self.__theList) == 0:
            return True
        else:
            return False

# Testing our queue implementation
if __name__ == '__main__' :
    
    print('Testing our queue implementation')
    print('--------------------------------')
    
    # create a dispaly a new queue
    line = MyQueue()
    print('Here is our empty queue:')
    print(line)
    
    # enqueue a few values
    line.put('Mary')
    line.put('John')
    line.put('Rose')
    line.put('Bob')
    
    # display queue again
    if not line.empty() :
        print('Here is our queue after enqueing a few values:')
        print(line)
    
        # dequeue a value from the queue
        first = line.get()  # get first value from the queue
        print('First in line: ', end = ' ')
        print(first)
    
        print('\nHere is our queue after dequeing first item:')
        print(line)
    
