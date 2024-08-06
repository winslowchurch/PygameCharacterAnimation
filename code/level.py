import pygame 
from player import Player
from room import Room

# later on, the current level will determine what is in the room?
# and so we need to pass it here i guess idk

class Level:
	def __init__(self,current_level,surface):
		# general setup
		self.display_surface = surface
		self.current_x = None 

		# player 
		self.player = pygame.sprite.GroupSingle()
		self.player_setup(100, 475)

		# room contents 
		self.room = Room()

	def player_setup(self, x, y):
		sprite = Player((x, y), self.display_surface)
		self.player.add(sprite)

	def scroll_x(self):
		player = self.player.sprite
		player.speed = 4

	def run(self):
		# background
		self.room.current.draw(self.display_surface)
		self.room.update(self.player.sprite)

		# player sprites
		self.player.update()
		self.scroll_x()
		self.player.draw(self.display_surface)
		