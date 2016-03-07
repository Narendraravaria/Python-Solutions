from stack import stack;
# implment SetOfStack data structure using several stack
# it is similar to satck but on increasing capacity creat new stack
class Node():
    def __init__ (self, prev = None, next = None):
        self.prev = prev;
        self.next = next;

class SetOfStack():
    def __init__ (self, capacity):
        self.__capacity = capacity;
        self.s = stack();
        self.currSt = s;
        # creeat stack to hold prev and next stack reference
        self.sstack = stack();  # top value holds node cotaing prev and next of curr stack
        node = Node();
        sstack.push(node);
        
        
    def push(self,e):
        if (currSt.size() == self.capacity):
            newStack = stack();
            # change the next value of old stack node
            oldNode = sstack.pop();
            oldNode.next = newStack;
            sstack.push(oldNode);
            
            # creat new node to hold prev value of new stack, update next when we creat new stack
            newNode = node(currSt);
            
            # update newNode prev pointer to currSt
            
            newNode.prev = currSt;
            sstack.push(newNode);
            
            # update currSt to newStack
            currSt = newStack;
        currSt.push(e);
        
        
    def pop():
        # ignore prev if currSt == self.s
        if (currSt != s):
            if (currSt.size() > 1):
                return currSt.pop();
            else:
                data = currSt.pop();
                currNode = sstack.pop();
                currSt = currNode.prev;
                
                # update next value of current Stack
                newCurrNode.next = None;
                newCurrNode = sstack.pop();
                sstack.push(newCurrNode);
        else:
            if (s.size() == 0):
                print "SetOfStack is Empty";
                return None;
            data = currSt.pop();
        
        return data;
            
   
            
                
            
        
        