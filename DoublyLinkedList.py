from NodeDL import Node
class DoublyLinkedList():
    def __init__ (self, head = None, end = None):
        self.head = head;
        self.end = end;
     
    def isEmpty(self):
        return (1 if (self.head == None and self.end == None) else 0);
        
    def insertFirst(self, data):
        new = Node(data);
        if (self.isEmpty()):
            #new.next = None;
            #new.prev = None;
            self.head = new;
            self.end = self.head;
        else:
            new.next = self.head;
            #new.prev = self.head.prev;
            self.head.prev = new;
            self.head = new;
            
    def removeFirst(self):
        if (self.isEmpty()):
            print "Empty Linked List";
            return None;
        
        curr = self.head;
        if(self.head == self.end):
            self.head = None;
            self.end = None;
            return curr;
         
        self.head = self.head.next;
        self.head.prev = None;
        return curr;
        
    def printList(self):
        if(self.isEmpty()):
            print "None";
            return;
        curr = self.head;
        while (curr.next != None):
            print curr.data," ->",;
            curr = curr.next;
        print curr.data;
        
L = DoublyLinkedList();
L.insertFirst(10);
L.insertFirst(20);
L.printList();

L.removeFirst();
L.removeFirst();
L.printList();

L.removeFirst();

