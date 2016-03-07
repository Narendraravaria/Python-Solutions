class Hero:
    count = 0;  # class variable, value shared among all instance of Hero class
    c = "";
    def __init__ (self, name):
        self.name = name;
        self.health = 100;
        Hero.count += 1;    #class variable need to refer by using classname.variable
                            # from inside or outside class

    def eat (self, food):
        if (food == 'apple'):
            self.health -=20;
        elif (food == "Roti"):
            self.health +=20;

    def printStat(self):
        self.c = self.name + str(Hero.count);
        Hero.c = "Global";
        # self.c creats instance varible 
        
        print "self.c: ",self.c,
        print "Name: ",self.name,
        print "Health: ",self.health;


h1 =Hero("narendra");
print "count: ",Hero.count;
h1.printStat();
print "self.c: ", h1.c;
print "Hero.c: ", Hero.c;

h2 = Hero("Hansal");
print "count: ",Hero.count;
h2.eat("apple")
h2.printStat();
