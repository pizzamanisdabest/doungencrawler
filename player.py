import pygame, random
from message import *
from tiles import Tile

class Player(pygame.sprite.Sprite):
    def __init__(self, path, pos,facing_r):
        super().__init__()
        self.path = path
        self.facing_r = facing_r
        self.image = pygame.image.load(self.path)
        if not self.facing_r:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = [0,0]
        self.level = None
        self.heath = 100
        self.attack_damage = 5
        self.defense = 1
        self.ememies = None
        self.facing = "R"
        self.alive = True

    def update(self):
        if self.alive:
            if self.facing == "R"
               self.image = pygame.image.load(self.path)
               if not self.facing_r:
                  self.image = pygame.transform.flip(self.image, True, False)
               else:
                    self.image = pygame.image.load(self.path)
                    if self.facing_r:
                        self.image = pygame.transform.flip(self.image, True, False)
                    self.rect.move_ip(self.movement)
                if len(pygame.sprite.spritecollide(self, self.level.walls, False)) >= 1:
                    if pygame.sprite.spritecollide_rect(self, self.level.exit) and self.level.exit.unlocked:
                        return -1
                    if pygame.sprite.collide_rect(self,self.level.start):
                        return -1
                    if self.level.chest is not None and pygame.sprite.collide_rect(self, self.level.chest):
                        self.level.message.add(MovingMassage(self.level.chest.give_bonus(self), self.level.chest.rect.center))
                    else:
                        self.movement[0] *=
                        self.movement[1] *=
                        self.rect.move_ip(self.movement)
                    self.enemies = pygame.sprite.spritecollide(self, self.level.enemies, False)
                    self.movement[0] = 0
                    self.movement[1] = 1
        def attack (self):
            if len (self.enemies) > 0:
                random.choice(self.enemies).defend(self.attack_damage)

        def defend(self, damage):
            if random.randint(1, 20) > self.defense:
                self.health -= damage
                self.heath = max(0, self.heath)
                self.level.messages.add(movingMessage("--{}".format(damage), self.rect.topleft, (255, 0, 0)))
            if self.heath <= 0:
                self.level.message.add(Message("rip", self.ract.center))
                self.level.floor.add(Tile("images/monsters/grave.gif", (self.rect.x-15, self.rect.y-25)))
                self.image = pygame.image.load("images/terrain/bones.glf")
                self.alive= False

        def up_level(self.level):
            self.movement =[0,0]
            self.level = up_level
            self.rect.topleft = level.start_poss
        def back_level(self, level):
            self.movement =[0,0]
            self.level = back_level
            self.rect.topleft = level.end_pos
        def draw(self, screen):
            screen.blit(self.image, self.rect)

        def change_x(self,change):
            self.movement[1] = change
            if change > 0:
                self.facing = "R"
            else:
                self.facing = "L"
            def change_y(self,change):
                self.movement[1] = change

            def save(self):
                self.image = None
                self.level = None
                self.enemies = None

            def load (self):
                self.image = pygame.image.load(self.path)

