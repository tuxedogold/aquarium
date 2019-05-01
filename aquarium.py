from GridSenseHat import GridSenseHat
from fish import fish
from food import food
from time import sleep

import datetime
class aquarium():
	def __init__(self):
		self.sense = GridSenseHat()	
		self.sense.clear()
		self.bg_color= (0,0,155)
		
		b = self.bg_color
		self.bg = [b for x in range(0,64)]
		
		self.sense.set_pixels(self.bg)
		
		self.fish = [fish(self.sense,self.bg_color)]
		self.food=[]
		self.hour = datetime.datetime.now()
		self.minute = 0
		self.creation_time = datetime.datetime.now()

	def play_again(self):
		self.fish = [fish(self.sense,self.bg_color)]
		#self.food = []
		self.sense.set_pixels(self.bg)
		self.hour = datetime.datetime.now()
		self.creation_time = datetime.datetime.now()
		self.hour = 0
		
		
	def pass_time(self):
		x, y, z = self.sense.get_accelerometer_raw().values()
		#print(x,y,z)
		if x>1.5 or y>1.5 or z>1.5:
			self.food.append(food(self.sense,self.bg_color))

		food_eaten = None
		food_expire = None
		for a_food in self.food: # food loop
		
			a_food.fall()
			if(a_food.should_expire()):
				food_expire = a_food
		
			for a_fish in self.fish: # check for collision being eating
				if(a_fish._x,a_fish._y) == (a_food._x,a_food._y):
					foodremove = a_food
					a_fish.feed()
			
		if(food_eaten is not None):
			self.food.remove(food_eaten)
		if(food_expire is not None):
			self.food.remove(food_expire)
			
			
		for a_fish in self.fish:
			if(a_fish.should_move()):
				a_fish.make_move()
				
			if(self.hour != datetime.datetime.now().hour):
				if(not a_fish.make_hungry()):
					self.fish.remove(a_fish)
				if(len(self.fish)==0):
					self.sense.show_message("dead = "+ str( datetime.datetime.now() -self.creation_time))
					
					self.play_again()
				self.hour = datetime.datetime.now().hour		
				
game = aquarium()
while True:
	game.pass_time()
	sleep(1)
	
