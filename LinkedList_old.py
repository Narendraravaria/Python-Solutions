
# insertFirst
# insertLast
# insertIndex

# removeFirst
# removeLast
# removeIndex

# isEmpty;
# size;

# print
# search

# import Node ;
from Node import *;
class LinkedList():

    def __init__ (self):
        self.__head = None;
        self.__size = 0;

        
    def getHead(self):
        return self.__head;
        
        
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
    
    def reverseLinkedList(self):
        curr = self.__head;
        next = None;
        prev = None;
        
        while (curr != None):
            next = curr.getNext();
            curr.setNext(prev);
            prev = curr;
            curr = next;
        self.__head = prev;
    
            
def sum(L1,L2, L):
    print "L1.getHead().getNum()",L1.getHead().getNum();
    carry = 0;
    c1 = Node();
    c1 = L1.getHead();
    c2 = L2.getHead();
    c = L.getHead();
    #print c1.getNum();
    while (c1 != None and c2 != None):
        t = L1.getHead().getNum() + L2.getHead().getNum() + carry;
        carry = t / 10;
        num = t % 10;
        L.insertLast(num);
        c1 = c1.getNext;
        c1 = c2.getNext;
        
    if (c2 == None):
        while (c1 != None):
            t = c1.getNum() + carry;
            carry = t / 10;
            num = t % 10;
            L.insertLast(num);
            c1 = c1.getNext();
    else:
        while (c2 != None):
            t = c2.getNum() + carry;
            carry = t / 10;
            num = t % 10;
            L.insertLast(num);
            c2 = c2.getNext();
    
    if (carry != 0):
        L.insertLast(carry);
    
            
if __name__ == '__main__':
        
    link1 = LinkedList();
    #link1.printList();
    link1.insertLast(2);
    link1.insertLast(1);
    link1.insertLast(5);
    link1.insertLast(9);
    link1.printList();

    link2 = LinkedList();
    #link2.printList();
    link2.insertLast(7);
    link2.insertLast(5);
    link2.insertLast(6);
    link2.printList();

    link = LinkedList();
    #link.printList();

    #sum(link1, link2, link);
    link.printList();

    print "Original Linked List";
    L = LinkedList();
    L.insertFirst(1);
    L.insertFirst(2);
    L.insertFirst(3);
    L.insertFirst(4);
    L.insertFirst(5);

    L.printList();
    L.reverseLinkedList();
    print "Reversed Listed list";
    L.printList();
