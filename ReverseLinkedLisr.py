from Node import *;
class LinkedList():

    def __init__ (self):
        self.__head = None;
        self.__size = 0;

        
    def getHead(self):
        return self.__head;
        
        
    def setHead(self,head):
        self.__head = head;
        
        
    def isEmpty(self):
        if (self.__head == None):
            return 1;
    
    
    def size(self):
        return self.__size;
        
    
    def insertFirst(self, num):
        
        # curr = Node.Node(num);
        curr = Node(num);
        curr.setNext(self.__head);
        self.__head = curr;
        self.__size += 1;
    
    def insertLast(self, num):
        if(self.isEmpty()):
            self.insertFirst(num);
        else:
            curr = self.__head;
            while(curr.getNext() != None):
                curr = curr.getNext();
            newNode = Node(num);
            newNode.setNext(None);
            curr.setNext(newNode);
            
    
    def printList(self):
        if (self.isEmpty()):
            print "Linked List is Empty";
            return;
        curr = self.__head;
        while (curr.getNext() != None):
            print "%d - >"%curr.getNum(),;
            curr = curr.getNext();
        
        print "%d"%curr.getNum();
    
    # def reverseLinkedList(self):
        # curr = self.__head;
        # next = None;
        # prev = None;
        
        # while (curr != None):
            # next = curr.getNext();
            # curr.setNext(prev);
            # prev = curr;
            # curr = next;
        # self.__head = prev;
        
        

L = LinkedList();
L.insertFirst(5);
L.insertFirst(4);
L.insertFirst(3);
L.insertFirst(2);
L.insertFirst(1);

L.printList();


def reverse(head,tail):
    curr = head;
    prev = None;
    next = None;
    while (curr != tail):
        next = curr.getNext();
        curr.setNext(prev);
        prev = curr;
        curr = next;
    #next = curr.getNext();
    curr.setNext(prev);
    prev = curr;
    #curr = next;
    return prev; 

def reverseLinkedList(L):
    head = L.getHead();
    curr = head;   
    while (curr.getNext() != None):
        curr = curr.getNext();
    L.setHead(reverse(head, curr));
    
  
reverseLinkedList(L);
L.printList();
    
    

