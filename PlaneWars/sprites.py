import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

CREATE_ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
# 设置尺寸
		self.rect = self.image.get_rect()
# 记录速度
		self.speed = speed

	def update(self):

		self.rect.y += self.speed

class Background(GameSprite):
	def update(self):
		super().update()


		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y =- self.rect.height

class Enemy(GameSprite):
	def __init__(self):
		super().__init__("./images/enemy1.png")

		self.speed = random.randint(1, 3)
		self.rect.bottom = 0

		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(10, max_x)

	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			print("敵機飛出屏幕")
			self.kill()

class Hero(GameSprite):
	def __init__(self):
		super().__init__("./images/hero1.png", 0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullets = pygame.sprite.Group()
	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed
		if self.rect.y + self.rect.height <= 0:
			self.rect.y = 50
		elif self.rect.y + self.rect.height >= 600:
			self.rect.y = 500
		elif self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
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
	def __init__(self):

		super().__init__("./images/bullet2.png")

	def update(self):

		super().update()

		if self.rect.bottom < 0:
			self.kill()
