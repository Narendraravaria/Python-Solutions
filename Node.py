class Node(object):
    
    def __init__ (self, num = None, next = None):
        self.__num = num;
        self.__next = next;
        
    def setNum(self, num):
        self.__num = num;
        
    def getNum(self):
        return self.__num;
        
    def setNext(self, next):
        self.__next = next;
        
    def getNext(self):
        return self.__next;

    