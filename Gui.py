# -*- coding: utf8 -*-

import sys
import pygame
from pygame.locals import *
import Tools

class Gui:
  '''
  Screen graphics and sounds are embedded in this class
  '''
  def __init__(self,width,height,court_size): 
    resolution=width,height

    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.key.set_repeat(10,10)

#   self.screen=pygame.display.set_mode(resolution,pygame.FULLSCREEN)
    self.screen=pygame.display.set_mode(resolution)
  
    self.snd_intro=Tools.load_sound("intro.wav")
    self.snd_hit=Tools.load_sound("hit.wav")
    self.snd_point=Tools.load_sound("miss.wav")
    self.snd_applause=Tools.load_sound("applause.wav")

    self.fnt_score = pygame.font.Font(None, 80)
    self.fnt_end = pygame.font.Font(None, 50)

    self.intro,bg_rect = Tools.load_image("fourpong.png")
    self.background,bg_rect = Tools.load_image("fourpong_court.png")
    self.endscreen,bg_rect = Tools.load_image("fourpong.png")
    
    self.court=pygame.Rect(court_size)
    self.scoreboard=[]
    self.scoreboard.append(pygame.Rect(24,126,100,100))
    self.scoreboard.append(pygame.Rect(678,126,100,100))
    self.scoreboard.append(pygame.Rect(678,380,100,100))
    self.scoreboard.append(pygame.Rect(24,380,100,100))

    if pygame.joystick.get_count() > 0:
       print "Joystick OK!";
       self.js=pygame.joystick.Joystick(0)
       self.js.init()
       
# SHOW INTRO
  def show_intro(self):

    self.screen.blit(self.intro, (0, 0))
   
    pygame.display.flip()
    self.snd_intro.play()
    pygame.time.delay(3000)

# SHOW COURT
  def show_court(self):

    for n in range(4):
      self.background.fill((255,255,255),self.scoreboard[n])
    self.screen.blit(self.background, (0, 0))
    
    pygame.display.flip()
    pygame.time.delay(1000)


# MOVE BALL
  def move_ball(self,b): 

    self.screen.blit(self.background,b.rect,b.rect)
    b.move()
    self.screen.blit(b.pic, b.rect)

    pygame.display.flip()


#SHOW PLAYERS
  def show_player(self,p):
    self.screen.blit(p.pic, p.rect)
#ERASE PLAYERS
  def erase_player(self,p):
    self.screen.blit(self.background,p.rect,p.rect)
 
# MOVE PLAYERS
  def move_player(self,player):

            event=pygame.event.pump()

# KEYS SECTION
            keys_state=pygame.key.get_pressed()
            if keys_state[K_ESCAPE]:
               sys.exit(0)
            if keys_state[K_c]:
               player[0].move_leftright(self.court.left,self.court.right,-1)
            if keys_state[K_v]:
               player[0].move_leftright(self.court.left,self.court.right,1)
            if keys_state[K_p]:
               player[1].move_updown(self.court.top,self.court.bottom,-1)
            if keys_state[K_l]:
               player[1].move_updown(self.court.top,self.court.bottom,1)
            if keys_state[K_n]:
               player[2].move_leftright(self.court.left,self.court.right,-1)
            if keys_state[K_m]:
               player[2].move_leftright(self.court.left,self.court.right,1)
            if keys_state[K_q]:
               player[3].move_updown(self.court.top,self.court.bottom,-1)
            if keys_state[K_a]:
               player[3].move_updown(self.court.top,self.court.bottom,1)
                
# GOAL !!!
  def goal(self,player,i,ball):
    self.snd_point.play()
    if i >= 0:
      player.score=player.score + 1
      self.screen.blit(self.background,self.scoreboard[i],self.scoreboard[i])
      text = self.fnt_score.render(str(player.score), 1, (0,0,0))
      width,height=text.get_size()
      x=self.scoreboard[i].centerx-width/2
      y=self.scoreboard[i].centery-height/2
 
      self.screen.blit(text, (x,y))
      
      pygame.display.flip();

    pygame.time.delay(2000)
    self.screen.blit(self.background,ball.rect,ball.rect)
    pygame.display.flip()

# SHOW_END
  def show_end(self,player):

    self.snd_applause.play()
   
    text = self.fnt_end.render(unicode("PULSA ESPACIO PARA JUGAR DE NUEVO",'utf-8'), 1, (250,200, 0))
    width,height=text.get_size()
    x=self.court.centerx-width/2
    y=self.court.centery-height/2
    self.screen.blit(text, (x,y))
    pygame.display.flip()

    pygame.event.clear()

    while 1:
      event=pygame.event.wait()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          sys.exit(0)
        if event.key == K_SPACE: 
          break               
   
   
