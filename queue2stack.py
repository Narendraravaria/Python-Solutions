from stack import stack;
# queue implementation using Two stack;

class MyQueue():
    def __init__ (self):
        self.__s1 = stack();
        self.__s2 = stack();
    
    def isEmpty(self):
        return (self.__s1.isEmpty() and self.__s2.isEmpty());
        
    def enqueue(self,e):
        if (self.isEmpty()):
            self.__s1.push(e);
        else:
            while (not self.__s2.isEmpty()):
                self.__s1.push(self.__s2.pop());
            self.__s1.push(e);
    
    def dequeue(self):
        if (self.isEmpty()):
            print ("Can't perform dequeue as Queue is Empty");
            return None;
        if (self.__s1.isEmpty()):
            return self.__s2.pop();
        else:
            while (not self.__s1.isEmpty()):
                self.__s2.push(self.__s1.pop());
            return self.__s2.pop();
            
    def printQueue(self):
        if (self.isEmpty()):
            print "Queue is Empty";
            return;
        #t = 1 if (self.__s1.isEmpty()) else 2;
        if (self.__s1.isEmpty()):
            self.__s2.printStack();
        else:
            self.__s1.printStack();

if __name__ == '__main__':        
    q1 = MyQueue();
    q1.enqueue(5);
    q1.enqueue(6);
    q1.enqueue(8);

    q1.printQueue();
    assert (q1.dequeue() == 5), "Not Matching";
    q1.printQueue();

    q1.enqueue(1);
    q1.enqueue(3);
    q1.enqueue(9);

    q1.printQueue();
       