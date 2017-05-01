# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Screen(object):
	@property
	def width(self):
		return self.__width
	
	@width.setter
	def width(self, width):
		if not isinstance(width, int):
			raise ValueError("´íÎóÖµ0")
		self.__width = width
		
	@property
	def height(self):
		return self.__height
	
	@height.setter
	def height(self, height):
		if not isinstance(height, int):
			raise ValueError("´íÎóÖµ")
		self.__height = height
		
	@property
	def resolution(self):
		return self.width*self.height
		
s = Screen()
s.width = 10
s.height = 18

print '%d * %d = %d' % (s.width, s.height, s.resolution)