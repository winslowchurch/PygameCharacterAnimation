import pygame 
from support import import_folder
from math import sin

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,surface):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = self.animations['idle'][self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)

		self.display_surface = surface
		# player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 6 # does nothing ?

		# Player status
		self.status = 'idle'
		self.facing_right = True
		self.on_left = False
		self.on_right = False

	def import_character_assets(self):
		character_path = '../graphics/lemon/'
		self.animations = {'idle':[],'run':[], 'sit':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def animate(self):
		animation = self.animations[self.status]

		# loop over frame index 
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		image = animation[int(self.frame_index)]
		if self.facing_right:
			self.image = image
		else:
			flipped_image = pygame.transform.flip(image,True,False)
			self.image = flipped_image

		self.image.set_alpha(255)

		# set the rect
		if self.on_right:
			self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
		elif self.on_left:
			self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
		else:
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.direction.x = 1
			self.facing_right = True
		elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.direction.x = -1
			self.facing_right = False
		elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.direction.x = 0
			self.status = 'sit'
		elif keys[pygame.K_UP] or keys[pygame.K_w]:
			self.direction.x = 0
			self.status = 'idle'
		else:
			self.direction.x = 0

	def get_status(self):	
		if self.direction.x != 0:
			self.status = 'run'
		else:
			if self.status != 'sit':
				self.status = 'idle'

	def wave_value(self):
		value = sin(pygame.time.get_ticks())
		if value >= 0: return 255
		else: return 0

	def update(self):
		self.get_input()
		self.get_status()
		self.animate()
		self.wave_value()

		self.rect.x += self.direction.x * self.speed
		self.rect.y += self.direction.y * self.speed
		