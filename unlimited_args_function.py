def func(*args):
    for arg in args:
        print arg;

#func(1,2,3,4,5,6,"Narendra");
l = [1,2,4,"narend"];
func(l);    #iterpreted as one argument only(list)

func(*l);   # pass each as individual arguments


def func1(**kwargs):     #kwargs is dictionary
    for item in kwargs.items():
        print item

func1(x = 456,y = 3)

func3(*args, **kwargs):
    
    for arg in args:
        print arg;
    for item in kwargs.items():
        print item


func3(1,2,3,x = "na")
