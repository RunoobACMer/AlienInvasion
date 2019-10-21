import pygame
import game_functions as gf
from setting import Setting
from ship import Ship
from alien import Alien
from pygame.sprite import Group

def run_game():
	#	initial the game and create a screen object
	pygame.init()
	ai_settings = Setting()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invesion")
	
	#	set background color
	bg_color = (230,230,230)
	
	#	create a ship
	ship = Ship(ai_settings,screen)
	
	#	create many aliens
	aliens = Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#	create many bullets
	bullets = Group()
	
	#	main cycle
	while(True):
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
