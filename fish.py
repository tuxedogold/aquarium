from  GridSenseHat import GridSenseHat
from random import randint
import datetime

class fish():
	def __init__(self,sense,clear_color=(0,0,0)):
		self.sense = sense
		self.belly = 24
		
		self.color=(0,0,0)
		self.clear_color = clear_color
		self.x_dir=1;
		
		self.lazy = 1
		
		self._x = 4
		self._y = 4
		self.creation_time = datetime.datetime.now()
		
	def make_move(self):
		self.sense.set_pixel(self._x,self._y,self.clear_color)
		if(self._x >= 7 or self._x <= 0):
			self.x_dir *=  -1
		
		elevation = randint(0,2) - 1
		self._y += elevation
		if(self._y <0):
			self._y = 0
		elif(self._y > 7):
			self._y = 7
			
			
		self._x = self._x + self.x_dir
		self.sense.set_pixel(self._x,self._y,self.color)
	def should_move(self):
		should_move = randint(0,self.lazy)
		return should_move == 0
		
		
	def make_hungry(self):
		if(self.belly > 0):
			self.belly -=1
			self.update_color()
			return True
		else:
			return False
			
	def feed(self):
		self.belly = 24
		self.update_color()
	
	def update_color(self):
		colordelta = self.belly * 10
		self.color = (255 - colordelta,colordelta,colordelta)
	
	