
class _const:
    def __init__(self):
        self.__const;
        
    def _getConst(self):
        return self.__const;

class stack:
    def __init__ (self, MAX = 0):
        self._top = -1;
        self.__size = 0;
        self.__MAX = MAX;
        self.__stack = [];
        
    def size(self):
        return self.__size;
    
    def isEmpty(self):
        return 1 if (self.__size == 0) else 0;
        
    def push(self, e):
        # if (self.__size == (self.__MAX)):  #if (self._top == (self.__MAX - 1)):
            # print "STACK IS FULL";  #raise STACKFULLEXCEPTION;
            # return 
        self._top += 1;
        self.__stack.append(e);
        self.__size += 1;
        
    def pop(self):
        if (self.__size == 0):
            print "STACK IS EMPTY";
            return None;     #raise EMPTYSTACKEXCEPTION
            
        self._top -= 1;
        self.__size -= 1;
        return self.__stack.pop();
        
    def top(self):
        if (self.__size == 0):
            print "STACK SI EMPTY NO TOP VALUE";
            return None;     #raise EMPTYSTACKEXCEPTION
            
        return self.__stack[self._top];
        
    def printStack(self):
        if(self.isEmpty()):
            print "Stack is Empty";
            return;
        
        i = self._top;
        while (i >= 0):
            print self.__stack[i],
            i -= 1;
        print "";

def sortStack(s1):
    s2 = stack(20);
    #s1.printStack();
    if (s1.isEmpty()):
        return s2;
    s2.push(s1.pop());
    
    while(not s1.isEmpty()):
        t = s1.pop();
        if(t <= s2.top()):
            s2.push(t);
        else:
            c = 0;
            while((not s2.isEmpty())):
                if (s2.top() > t):
                    break;
                s1.push(s2.pop());
                c += 1;
            s2.push(t);
            while(c != 0):
                s2.push(s1.pop());
                c -= 1;
    return s2;

if __name__ == '__main__':
    s = stack(20);
    s.push(-10);
    s.push(5);
    s.push(7);
    s.push(1);
    s.push(8);
    s.push(3);
    s.push(1);
    s.push(2);
    s.push(9);
    s.push(11);
    s.push(-1);
    s.printStack();
    s2 = sortStack(s);
    print ("Sorted Stack");
    s2.printStack();
