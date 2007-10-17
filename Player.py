import Tools

class Player:
  """
     A Player including score and coordinates
  """
  def __init__(self,pic,x,y,incx,incy):
     self.score=0
     self.incx=incx
     self.incy=incy
     self.pic,self.rect = Tools.load_image(pic)
     
     self.rect.left=x
     self.rect.top=y

  def move_leftright(self,limit1,limit2,s):

     new_x=self.rect.left+(self.incx * s)
     if new_x > limit1 and new_x < limit2 - self.rect.width:
       self.rect.left=new_x


  def move_updown(self,limit1,limit2,s):

     new_y=self.rect.top+(self.incy * s)

     if new_y > limit1 and new_y < limit2 - self.rect.height:
       self.rect.top=new_y


