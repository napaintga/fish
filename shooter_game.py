from pygame import *
from random import randint
from time import sleep

mixer.init()
mixer.music.load('Snowy.mp3')
# mixer.music.play()
# fire_sound = mixer.Sound("fire.ogg")
# win_sound = mixer.Sound("win.mp3")

wn = display.set_mode((700,500))
clock = time.Clock()
display.set_caption("Акваріум")

background = transform.scale(image.load("imgonline-com-ua-pixelizationPnjNZSa2KpnZ.jpg"),(700,500))
FPS = 60
font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,100)

fish_x = 210
fish_y = 100
orange_images = ["orangefish1.jpg", "orangefish2.jpg", "orangefish3.jpg"]
red_images = ["redfish1.jpg", "redfish2.jpg", "redfish3.jpg"]


def make_fish_list(list,img_list):
    for fish_image in img_list:
        fish_img = image.load(fish_image).convert()
        fish_img.set_colorkey((0, 0, 0))

        for _ in range(6):
            scaled_fish = transform.scale(fish_img, (fish_x, fish_y))
            list.append(scaled_fish)
    return list
        
orangefish_list = []
make_fish_list(orangefish_list,orange_images)

redfish_list = []
make_fish_list(redfish_list,red_images)
class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_x,pl_y,size_x,size_y,pl_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pl_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
        self.speed = pl_speed
        self.size_x = size_x
        self.count = 0
    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
        # draw.rect(wn,(45,78,34),self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y) 
    
    def animation(self,list):
        self.count = (self.count + 1) % len(list)  
        wn.blit(list[self.count], (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #[K_a,K_k]
        #назва списку[номер елементу]
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - self.size_x:
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 50:
            self.rect.y += self.speed
coin_count = 0    
boubles = sprite.Group()
for i in range(1):
    bouble = GameSprite("f66bb4d63b517c425adae2e4d66cd68a-removebg-preview.png",randint(0,600),210,120,90,6) 
    boubles.add(bouble)
    
coin_count = 0    
coins = sprite.Group()
for i in range(1):
    coin = GameSprite("coin.png",randint(0,600),210,120,90,6) 
    coins.add(coin)

    
fish_red = Player("redfish1.jpg",485,210,120,74,6) 
fish_orange = Player("orangefish1.jpg",485,100,120,74,6) 

fish = Player("Знімок_екрана_2024-05-05_192008-removebg-preview.png",485,210,120,74,6) 
shop_icon = GameSprite("free-icon-shop-126122.png",605,20,70,70,8)

game = True
fish_p = True
shop = False

#shop

background_shop= transform.scale(image.load("shopbg.jpg"),(700,500))
exit_icon = GameSprite("exit.jpg",605/2,420,120,120,8)
exit_icon.image.set_colorkey((0, 0, 0))  # Робимо чорний колір (RGB: 0, 0, 0) прозорим

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if shop_icon.collidepoint(x,y):
                shop = True
                fish_p = False
            elif exit_icon.collidepoint(x,y):
                shop = 0
                fish_p = 1
    if  fish_p:
        wn.blit(background,(0,0))
        shop_icon.reset()
        fish.animation(orangefish_list)
        fish.update()
        boubles.draw(wn)
        coins.draw (wn)

        polka=sprite.spritecollide(fish,boubles,True)
        if polka:
            bouble = GameSprite("f66bb4d63b517c425adae2e4d66cd68a-removebg-preview.png",randint(0,600),randint(0,210),120,90,6) 
            boubles.add(bouble)
        polka_c=sprite.spritecollide(fish,coins,True)
        if polka_c:
            coin = GameSprite("coin.png",randint(0,600),210,120,90,6) 
            coins.add(coin)

    if shop:
        wn.blit(background_shop,(0,0))
        exit_icon.reset()
        fish_red.animation(orangefish_list)
        fish_orange.animation(redfish_list)

    clock.tick(FPS)
    display.update()

