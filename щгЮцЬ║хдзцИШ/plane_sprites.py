import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)



CREATE_ENEMY_EVENT = pygame.USEREVENT


HERO_FIRE_EVENT = pygame.USEREVENT + 1



class GameSprite(pygame.sprite.Sprite):

	def __init__(self,new_image,new_speed=1):
		super().__init__()

		self.image = pygame.image.load(new_image)

		self.rect = self.image.get_rect()

		self.speed = new_speed

	def update(self):

		self.rect.y += self.speed


class Background(GameSprite):
	"""背景精灵类"""
	def __init__(self,is_alt=False):

		super().__init__("/home/yuqilin/于奇林background.png")
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height

class Enemy(GameSprite):
	"""敌机精灵类"""
	def __init__(self):
		super().__init__("/home/yuqilin/于奇林/enemy1.png")
		self.speed = random.randint(1, 2)
		self.rect.bottom = SCREEN_RECT.bottom - 100
		max_x= SCREEN_RECT.width - self.rect.width
		# 随机一个位置
		self.rect.x = random.randint(SCREEN_RECT.bottom - 100, max_x)
 

		def update(self):
			# 1 调用父类方法
			super().update()

			if self.rect.y >= SCREEN_RECT.height:
				print("敌机飞出屏幕")
				# 移出屏幕  就销毁
				self.kill()

# 英雄精灵类
class Hero(GameSprite):
	def __init__(self):
		# 英雄的初始速度我设置为0
		super().__init__('/home/yuqilin/于奇林/me1.png',0)

		self.rect.centerx = SCREEN_RECT.centerx
		# 这里是设置我飞机的y轴
		self.rect.bottom = 0
		#SCREEN_RECT.bottom - 100

		# 子弹组
		self.bullets = pygame.sprite.Group()


	def update(self):
		# 飞机水平移动
		self.rect.x += self.speed

		# 控制英雄边界 屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right >SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		# 英雄的方法。。。发射子弹  是一个动作  是一个行为 。。。
		print("发射子弹....")

		for i in (1,2,3):
			# 子弹精灵 我们在 英雄的这个fire（）方法里面去创建
			#1 创建 子弹精灵
			bullet = Bullet()
			#2 设置精灵位置
			bullet.rect.bottom = self.rect.y -20
			bullet.rect.centerx = self.rect.centerx
			#3 将精灵添加到精灵组
			self.bullets.add(bullet)


class Bullet(GameSprite):
	"""子弹精灵"""
	def __init__(self):
		super().__init__('/home/yuqilin/于奇林/bullet1.png',-2)
	def update(self):
		super().update()
		# 判断是否超出屏幕
		if self.rect.bottom < 0:
			self.kill()
