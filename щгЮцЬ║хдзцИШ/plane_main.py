import pygame
from plane_sprites import *
class PlaneGame(object):

    def __init__(self):
        print("游戏初始")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        self.clock = pygame.time.Clock()

        self.__create_sprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000) 

        pygame.time.set_timer(HERO_FIRE_EVENT,500)





    def start_game(self):

        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()



    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        #bg2.rect.y = -bg2.rect.height

        self.hero = Hero()
        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)



    def __event_handler(self):

        for event in pygame.event.get():
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                print("向右边移动")
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed =  -2
                print("向左边移动")
            else:
                self.hero.speed = 0

            # pygame.event.get()

            if event.type == pygame.QUIT:

                self.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:

                print("新的敌机产生")

                self.enemy_group.add(Enemy())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

       
    # 更新精灵和精灵组
    def __update_sprites(self):

        self.back_group.update()

        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)


        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)



    def __check_collide(self):

        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)


        if len(enemies)>0:
            self.hero.kill()
            self.__game_over() 


    
    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()