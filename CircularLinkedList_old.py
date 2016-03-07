from Node import Node;

class CircularLinkedList():
    def __init__ (self, head = None, end = None):
        self.head = head;
        self.end = end;
        
    def isEmpty(self);
        return 1 if (self.head == None) else 0;
            
    def insertFirst(data):
        new = Node(data);
        if(self.isEmpty()):
            head = new;
            head.next = head;   #loop back to first element
            end = head;
        else:
            new.next = head;
            end.next = new;
            head = new;
            
    def insertLast(data):
        new = Node(data);
        
            
        