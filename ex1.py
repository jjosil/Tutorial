class myCar:
	def __init__(self, make, model):
		self.CarMake = make
		self.CarModel = model
		
	def func(self):
		print(self.CarMake, self.CarModel)

car = myCar('Toyota', 'Camry SE')

#car.func()	
#print()

print('My car is a:\nMaker:\t{}\nModel:\t{}\n'
.format(car.CarMake, car.CarModel))
	
class myBike(myCar):
	def __init__(self, make, model, year):
		super().__init__(make, model)
		self.bikeYear = year
		
	def other_type(self):
		print('I also own a bike made by', 
		self.CarMake, 'model', self.CarModel, "year", 
		self.bikeYear)
	
bike = myBike('Giant', 'Hybrid', '2019')
bike.other_type()