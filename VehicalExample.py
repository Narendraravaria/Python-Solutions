#We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000 with a name of Fer, and car2 to be a 
#blue van named Jump worth $10,000.

class Vehicle (object):

	def __init__ (self, name, type, color, price):
		self.name = name;
		self.type = type;	#???
		self.color = color;
		self.price = price;

	def display(self):
		print "Name: ", self.name, " Type: ", self.type, " Color: ", self.color, " Price: ", self.price;


car1 = Vehicle("Fer", "Covertible", "Red", "$60,000");
car2 = Vehicle("Jump", "Van", "Blue", "$10,000");

car1.display();
car2.display();
