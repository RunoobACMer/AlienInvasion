class Setting():
	# storage for all the settings
	
	def __init__(self):
		#	init()
		
		#	screen setting
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230,230,230)
		
		#	ship setting
		self.ship_speed_factor = 1.5
		
		#	bullet setting
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 10
