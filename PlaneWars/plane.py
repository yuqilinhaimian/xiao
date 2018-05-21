import pygame

from sprites import *
class PlaneGame(object):

		
	def  __init__(self):
		print("遊戲初始化")
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
		pygame.time.set_timer(HERO_FIRE_EVENT, 500)

	def start_game(self):
		print("遊戲開始")
		while True:
			#遊戲時鍾
			self.clock.tick(60)
			#事件監聽
			self.__event_handler()
			#碰撞檢測
			self.__check_collide()
			#更新精靈組
			self.__update_sprites()
			#更新屏幕顯示
			pygame.display.update()
	#創建精靈族
	def __create_sprites(self):

		bg1 = Background("./images/background.png")
		bg2 = Background("./images/background.png")
		bg2.rect.y =- bg2.rect.height
		self.hero = Hero()
		self.back_group = pygame.sprite.Group(bg1, bg2)
		self.enemy_group = pygame.sprite.Group()
		self.hero_group = pygame.sprite.Group(self.hero)
		self.bullets = pygame.sprite.Group()
	#事件監聽
	def __event_handler(self):
		for event in pygame.event.get():
			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_RIGHT]:
				self.hero.speed = 2
			elif keys_pressed[pygame.K_LEFT]:
				self.hero.speed =-2
			elif keys_pressed[pygame.K_UP]:
				self.hero.speed =-2
			elif keys_pressed[pygame.K_DOWN]:
				self.hero.speed = 2
			else:
				self.hero.speed = 0

			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				print("敌机出场...")
				self.enemy_group.add(Enemy())
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
	#碰撞檢測
	def __check_collide(self):
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)


		if len(enemies)>0:
			self.hero.kill()
			self.__game_over() 
	#更新精靈組
	def __update_sprites(self):

		for group in [self.back_group, self.enemy_group, self.hero_group, self.bullets]:
			group.update()
			group.draw(self.screen)			

	def __game_over():
		print("遊戲結束")
		pygame.quit()
		exit()








if __name__ == '__main__':
	game = PlaneGame()

	game.start_game()