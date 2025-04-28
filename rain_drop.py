import pygame
import sys
from rains import Rains
from handtracking import detect_slices,slicing_positions
from threading import Thread

class Raindrop():
    def __init__(self):
        pygame.mixer.init()
        self.w,self.h=640,480
        self.vani=[]
        self.screen=pygame.display.set_mode((self.w,self.h))
        self.rains=pygame.sprite.Group()
        self.rect=self.screen.get_rect()
        self.bg_image=pygame.image.load("D:/myProjects/rain_drop/rainy-sky-background.bmp")
        self.b_image=pygame.transform.scale(self.bg_image,(self.rect.width,self.rect.height))
        self.rndp=pygame.image.load("D:/myProjects/rain_drop/new_rain.bmp")
        self.rn=pygame.transform.scale(self.rndp,(65,65))
        self.fleet()
        self.total_rain=len(self.rains)
        self.obj=Rains(self)
        pygame.display.set_caption("INFINITE RAIN DROPS!!!")
        pygame.mixer.music.load("D:/myProjects/rain_drop/calming-rain-257596.mp3")
        pygame.mixer.music.play(-1)
        self.bubble=pygame.mixer.Sound("D:/myProjects/rain_drop/bubble-pop-2-293341.mp3")
    def update(self):
        global slicing_positions
        while True:
            self.screen.blit(self.b_image,self.rect)
            self.rains.draw(self.screen)
            for rain in self.rains.sprites():
                for sx, sy in slicing_positions:
                    if abs(rain.rect.x - sx) < 30 and abs(rain.rect.y - sy) < 30:  
                         self.vani.append((rain.rect.x,rain.rect.y))
                         self.bubble.play()
                         self.rains.remove(rain) 
                         slicing_positions.remove((sx,sy))
                for vx,vy in self.vani:
                    pygame.draw.circle(self.screen,(255,0,255),(sx,sy),10)
                self.vani.clear()
                if len(self.rains) < self.total_rain:
                    self.fleet()
                rain.update_rain()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            

            

    def fleet(self):
        rain=Rains(self)
        rain_width,rain_height=rain.rect.size
        current_x,current_y=rain_width,rain_height
        while current_y < self.h:
              while current_x < self.w:
                   new_rain=Rains(self)
                   new_rain.x=current_x
                   new_rain.y=current_y
                   new_rain.rect.x=current_x
                   new_rain.rect.y=current_y
                   self.rains.add(new_rain)
                   current_x=current_x+(2*rain_width)
              current_y=current_y+(3*rain_height)
              current_x = rain_width  # Reset to the starting x position for the new row


if __name__=="__main__":
    hand_thrd=Thread(target=detect_slices,daemon=True)
    hand_thrd.start()
    gme=Raindrop()
    gme.update()

        
