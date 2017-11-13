﻿import sys
import pygame
import time

def main():
	pygame.init()
	
	speed = [2 , 2]
	white = 255 ,255 ,255
	
	width = 320
	height = 240
	screen = pygame.display.set_mode((width,height) , 0 ,32)
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
		
		screen.fill((0,0,0))
		screen.blit(ball, ball_rect)
		
		for i in range(width):
			point = (i,i)
			screen.set_at(point , (255,0,0))
			
		pygame.display.flip()
		
		time.sleep(0.01)
		

if __name__=="__main__":
	main()