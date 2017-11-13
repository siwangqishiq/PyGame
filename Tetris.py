import sys,pygame,time
from GameTeris import Game

def main():
	COLOR_WHITE = (255,255,255)	
	
	pygame.init()
	screen = pygame.display.set_mode((Game.SCREEN_WIDTH , Game.SCREEN_HEIGHT),0 , 32)
	pygame.display.set_caption("Tetris Game")
	
	game = Game()
	game.init()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			else:
				game.handle_input(event)
			
		screen.fill(COLOR_WHITE)
		game.update(screen)
		pygame.display.flip()
		
		time.sleep(0.1)
	
	
	
if __name__=="__main__":
	main()