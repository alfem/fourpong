import random
import Tools

class Ball:
  """
     A bouncing ball
  """
  def __init__(self,pic):
     self.pic,self.rect = Tools.load_image(pic)
     random.seed()

  def launch(self):
     self.left=random.randint(390,410)
     self.top=random.randint(290,310)
     self.incx=random.choice((1,0.5,-0.5,-1))          
     self.incy=random.choice((1,0.5,-0.5,-1))          
 
  def move(self):
     self.left=self.left+self.incx
     self.top=self.top++self.incy

     self.rect.left=self.left
     self.rect.top=self.top
