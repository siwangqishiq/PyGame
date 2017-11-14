__all__ = ["Game"]

import sys,pygame,time

#分数Hub
class ScoreBanner(object):
	TEXT_COLOR = (255 ,0 , 0) #文字颜色设置
	
	def __init__(self , game):
		self.score = 0
		self.left = MainView.WIDTH + 40
		self.top = 0
		self.game = game
		self.font = pygame.font.SysFont("comicsansms", 30)
		#self.font.set_underline(True)
	
	#分数画面绘制
	def update(self , screen):
		#print("font init = "+str(pygame.font.get_init()))
		score_label = self.font.render("SCORE", True , ScoreBanner.TEXT_COLOR)
		#print(score_label)
		screen.blit(score_label , (self.left , self.top))
		
		label_height = score_label.get_height()
		score_value = self.font.render(str(self.score) , True , ScoreBanner.TEXT_COLOR)
		score_offset = score_label.get_rect().width/2 - score_value.get_rect().width/2
		
		screen.blit(score_value , (self.left + score_offset , self.top + label_height))
		#print("time = score")
	
	#添加分数
	def add_socre(add):
		score += add

class BaseShape(object):
	def __init__(self , color):
		self.color = color
		self.x = 0
		self.y = 0
	
	def rotate(self):
		print("rotate")
	
	def down(self):
		print("down")
	
	def left(self):
		print("left")
	
	def right(self):
		print("right")
		
	def update(self ,screen):
		print("render shape")
		
				
#主界面
class MainView(object):
	WIDTH = 400
	HEIGHT = 800
	
	BOUND_COLOR = (0,0,0)
	NET_COLOR = (204,204,204)
	def __init__(self , game):
		self.game = game
		self.row = 20
		self.col = 10
		self.cube = 40
		self.data = [[0 for i in range(self.col)] for j in range(self.row)]
		self.cur_shape = None
		
	def update(self , screen):
		self.draw_net(screen)
		self.draw_bound(screen)
		
		if self.cur_shape != None:  #cur
			self.cur_shapre.update(screen)
		
		
	
	def draw_bound(self, screen):
		pygame.draw.rect(screen , MainView.BOUND_COLOR , 
		(0,0,MainView.WIDTH, MainView.HEIGHT),2)
	
	def draw_net(self,screen):
		for i in range(self.col):
			pygame.draw.line(screen, MainView.NET_COLOR, 
			(i * self.cube,0), (i * self.cube,MainView.HEIGHT), 1)
		
		for i in range(self.row):
			pygame.draw.line(screen, MainView.NET_COLOR, 
			(0,i * self.cube), (MainView.WIDTH,i * self.cube), 1)

class Game(object):
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 800
	
	def __init__(self):
		self.main_view = None
		self.score_banner = None
	
	def init(self):
		#print("game_init")
		self.main_view = MainView(self)
		self.score_banner = ScoreBanner(self)
		pass
		
	def	handle_input(self , ev):
		#print("handle_input")
		#print(ev)
		pass
	
	def update(self , screen):
		#print("game update")
		cur_time = pygame.time.get_ticks()
		self.main_view.update(screen)
		self.score_banner.update(screen)
		#print("time = %s"%(cur_time))
		#pass

				
				
				
				
				
				
