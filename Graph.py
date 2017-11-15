import sys,pygame,time

SCREEN_WIDTH = 800;
SCREEN_HEIGHT = 450;
COLOR_WHITE = (255,255,255)	
COLOR_BLACK = (0,0,0)	
screen = None

#绘制一个像素点
def setPoint(x, y):
	screen.set_at((x,y) , COLOR_BLACK)
	

def drawLine():
	#print("draw line")
	setPoint(122, 122)
	#pass

def main_framework():
	global screen
	
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT),0 , 32)
	pygame.display.set_caption("计算机图形学")
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				sys.exit()
			else:
				#game.handle_input(event)
				pass
			
		screen.fill(COLOR_WHITE)
		drawLine()
		pygame.display.flip()
		time.sleep(0.01)
	
if __name__=="__main__":
	main_framework()
	