import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#	load the image of alien
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#	set postion as (0,0)
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#	store the position of alien
		self.x = float(self.rect.x) 
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
