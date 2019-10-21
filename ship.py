import pygame

class Ship():
	
	def __init__(self,ai_settings,screen):
		#	initial the ship
		self.screen = screen
		self.ai_settings = ai_settings
		
		#	form the ship and get its outsied rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#	put every new ship at the bottom of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#	store decime in center
		self.center = float(self.rect.centerx)
		
		#	moving flag
		self.moving_right = False
		self.moving_left = False
		
		
	def update(self):
		#	update center instead of rect.centerx
		if self.moving_right == True and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left == True and self.rect.left > 0 :
			self.center -= self.ai_settings.ship_speed_factor	
		
		#	update rect.center by center
		self.rect.centerx = self.center
		
	def blitme(self):
		#	paint the ship at certain postion
		self.screen.blit(self.image,self.rect)
		
