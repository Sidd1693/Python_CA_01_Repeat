#Create and test a class Basket
#Add a class/static variable pricelist of type dictionary
#Add a data structure to store the individual basket contents - the quantities of each item being purchased
#create a method to add an item with a given quantity to the basket
#create a method value to return the cost of the basket contents
#Test that:
#the value is zero on creation
#Value is correct after adding one item
#Value is correct after adding more of one item (quantity >1)
#Value is correct after adding even more of one item (two calls to add method)
#Value is correct after adding some additional items of another product
#Cannot add a negative quantity (Error)
#Cannot add something not in the pricelist (Should give a ValueError!)

#Creating Class Basket
class Basket:
	def __init__(self) -> None:
		self.list = {}

#Setting Condition and Checking for Error
	def addItem(self, item, quantity):
		if quantity < 1:
			print("[Error] Cannot add a negative quantity")
			return
		
		if item not in pricelist:
			print("[Error] Value Error")
			return

		if item in self.list: self.list[item] += quantity
		else: self.list[item] = quantity

	def getCost(self):
		s = 0
		for item in self.list:
			s += pricelist[item] * self.list[item]
		return s
		

#Creating Dictionary PriceList
pricelist = {
	"A": 100,
	"B": 200,
	"C": 250,
	"D": 150
}


#Calculating Cost Based Selected Products
b = Basket()
while True:
	print("1. Add Item")
	print("2. Get Cost")
	print("3. Exit")
	ch = int(input("Enter your choice: "))
	if ch == 1:
		product = input("Enter the product: ")
		quantity = int(input("Enter the no. of quantity: "))
		b.addItem(product, quantity)
	elif ch == 2:
		print(b.getCost())
	elif ch == 3:
		break
	else:
		print("Invalid Choice")