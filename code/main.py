import pygame, sys
from level import Level
from settings import * 

class Game:
	def __init__(self):
		self.create_level(0)

	def create_level(self,level):
		self.level = Level(level, screen)

	def run(self):
		self.level.run()

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	game.run()
	pygame.display.update()
	clock.tick(60)