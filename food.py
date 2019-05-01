from  GridSenseHat import GridSenseHat
from random import randint
import datetime

class food():
	def __init__(self,sense,clear_color=(0,0,0)):
		self.sense = sense
		self._x = randint(0,7)
		self._y = 0
		self.clear_color = clear_color
		self.color = (255,228,196)
		self.creation_time = datetime.datetime.now()
		self.expiration_date = 15
		
	def fall(self):
		self.sense.set_pixel(self._x,self._y,self.clear_color)
		if(self._y < 7):
			self._y+=1
		self.sense.set_pixel(self._x,self._y,self.color)
		
	
	def should_expire(self):
		if((datetime.datetime.now().minute - self.creation_time.second) > 15):
			self.sense.set_pixel(self._x,self._y,self.clear_color)
			return True
		else:
			return False
			