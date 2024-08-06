import pygame

class Room:
	def __init__(self):
		self.streetRoom = Street_Room()
		self.current = self.streetRoom

	def update(self, player):
		mp = pygame.mouse.get_pos()
		# if (pygame.mouse.get_pressed()[0]):
		# 	# street to living room
		# 	if self.current == self.streetRoom and self.streetRoom.door_rect.collidepoint(mp):
		# 		self.current = self.livingRoom
		# 		player.rect.topleft = (950, 475) # update player position
		# 		player.facing_right = False
		
class Street_Room:
	def __init__(self):
		# background image
		self.background = pygame.image.load('../graphics/rooms/street/street.png').convert_alpha()
		
		

	def draw(self,surface):
		surface.fill((255, 192, 203))