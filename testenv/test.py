import pygame, sys

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((400, 800))
		self.clock = pygame.time.Clock()
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()	