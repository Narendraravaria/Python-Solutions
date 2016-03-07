from stack import stack;
# sort stack using two stack
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
s2 = sortStack(s);
print ("Sorted Stack");
s2.printStack();
