import sys,pygame,time

def main():
	pygame.init()
	
	speed = [2 , 2]
	white = 255 ,255 ,255
	BLACK = (0,0,0)
	
	width = 320
	height = 240
	screen = pygame.display.set_mode((width,height) , 0 ,32)
	pygame.display.set_caption("Hello My Ball!")
	ball = pygame.image.load("img/ball.gif")
	ball_rect = ball.get_rect()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			#if event.type == pygame.KEYWORD:
			print(event)
		
		ball_rect = ball_rect.move(speed)
		if ball_rect.left < 0 or ball_rect.right > width:
			speed[0] = -speed[0]
		if ball_rect.top < 0 or ball_rect.bottom > height:
			speed[1] = -speed[1]
		
		screen.fill(white)
		screen.blit(ball, ball_rect)
		
		for i in range(width):
			point = (i,i)
			screen.set_at(point , (255,0,0))
			
		pygame.draw.rect(screen, (200,100,0), [20+200, 20, 100, 100],10)
		pygame.draw.rect(screen, (200,100,0), [20, 20, 100, 100])
			
		pygame.display.flip()
		
		time.sleep(0.01)
		
		#print(pygame.display.get_driver())

if __name__=="__main__":
	main()