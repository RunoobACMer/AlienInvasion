import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_q:
		sys.exit()
	#	push down
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		#	limit bullet quantity
		fire_bullet(ai_settings,screen,ship,bullets)
		


def check_keyup_events(event,ship):
	#	release key
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
	
	#	react to keyboard and mouse
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)	
		
		
def update_screen(ai_settings,screen,ship,aliens,bullets):
	#	update the image on the screen, and shift to a new screen
	
	#	repaint the screen while cicle
	screen.fill(ai_settings.bg_color)
	
	#	draw all the bullet
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	aliens.draw(screen)
	
	#	make the last screen visiable
	pygame.display.flip()

def update_bullets(bullets):
	bullets.update()
	
	#	delete the vanished bullet
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
def get_number_aliens_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x
	
def get_number_rows(ai_settings,ship_height,alien_height):
	available_space_y = (ai_settings.screen_height - 
							(3*alien_height) - ship_height)
	number_rows = int(available_space_y / (2*alien_height))
	return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	#	create a alien and put on the first row
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width * alien_number
	alien.y = alien.rect.height + 2*alien.rect.height * row_number	
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
	aliens.add(alien)
	
def create_fleet(ai_settings,screen,ship,aliens):
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,
		alien.rect.height)
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,
				row_number)










