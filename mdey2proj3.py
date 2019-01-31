# Python program to make horizontal, vertical collages and posterize pictures based on a order
# Author: Mohar Dey


class smartPicture(Picture):
  # defining the constructor variable for smart picture class
  def __init__(self, file, noOfDuplicates=1,noOfRows=1):
    Picture.__init__(self, file)
    self.noOfDuplicates=noOfDuplicates
    self.noOfRows=noOfRows
  
  #operator overloading for ==
  def __eq__(self,picture):  
    selfWidth=self.getWidth()
    selfHeight=self.getHeight()
    picWidth=picture.getWidth()
    picHeight=picture.getHeight()
    
    if (selfWidth==picWidth) and (selfHeight==picHeight):
      return true
    else:
      print false
  
  #operator overloading for +        
  def __add__(self,pic):
    
    if (self==pic):
      print "continue"
    else:
      print "exit program"
      return
    
    row=self.noOfRows+pic.noOfRows
    width=self.getWidth()
    height=self.getHeight()
    newPic=makeEmptyPicture(width,height+pic.getHeight())
  
    xpos=0
    ypos=0
    count=0
    newYpos=0
  
    while(count<2):
    
      while(xpos<width):
      
        while(ypos<height):
          # empty picture to take pixels from the two pictures depending on the row count
          if (count==0): 
           
            pixel=self.getPixel(xpos,ypos)
            newPixel=newPic.getPixel(xpos,newYpos)
        
            color=getColor(pixel)
            newPixel.setColor(color)
          
          else:
            pixel=pic.getPixel(xpos,ypos)
            newPixel=newPic.getPixel(xpos,newYpos)
        
            color=getColor(pixel)
            newPixel.setColor(color)
        
          ypos+=1
          newYpos+=1 # newYpos to increment with original ypos
           
                     
        xpos+=1
        ypos=0
        newYpos = height*count # resetting newYpos to orginal height multiplied by number of copies
          
            
      count+=1
      xpos=0 
    
    
    return smartPicture(newPic, self.noOfDuplicates, row) # returning the new smart picture
    
  #operator overloading for *
  def __mul__(self, integerValue):
    
    width=self.getWidth()
    height=self.getHeight()
    
    newDup=self.noOfDuplicates*integerValue
      
    dupPic=makeEmptyPicture(width*newDup,height)
  
    xpos=0
    ypos=0
    count=0
    newXpos=0
  
    while(count<integerValue):
    
      while(xpos<width):
      
        while(ypos<height):
          
          pixel=getPixel(self,xpos,ypos)
          newPixel=getPixel(dupPic,newXpos,ypos)
        
          color=getColor(pixel)
          newPixel.setColor(color)
        
          ypos+=1
                    
        xpos+=1
        newXpos+=1
        ypos=0
           
      count+=1
      xpos=0 
    
    return smartPicture(dupPic,newDup,self.noOfRows)  # returning the new smart picture
    
    
  #operator overloading for !=
  def __ne__(self,pic):
    
    if (self.getWidth()!=pic.getWidth) and (self.getHeight()!=pic.getHeight):
      print "exit program"
      return
    else:
      print "continue"
      
      
      
  #function to get the luminance value of a pixel
  def getLumVal(self,pix):
    
    lum=(pix.getRed()+pix.getBlue()+pix.getGreen())/3
    return lum
    
  #function to posterize based on a lum val
  def postColorOne(self, lum):
    
    if (lum<63):
      return yellow
    elif (lum<126):
      return green
    elif (lum<189):
      return(blue)
    else:
      return red
      
  def postColorTwo(self,lum):
    
    if (lum<63):
      return green
    elif (lum<126):
      return blue
    elif (lum<189):
      return white
    else:
      return black
    
  def postColorThree(self,lum):
    
    if (lum<63):
      return white
    elif (lum<126):
      return red
    elif (lum<189):
      return yellow
    else:
      return green
  
  def postColorFour(self,lum):
    
    if (lum<63):
      return white
    elif (lum<126):
      return black
    elif (lum<189):
      return orange
    else:
      return blue
      
  #function to posterize a row depending on an order value
  def posterizeRow(self, orderValue):
    
    dup=self.noOfDuplicates
    count=0
    
    width=self.getWidth()/dup
    height=self.getHeight()
    
    xpos=0
    ypos=0
    
    while(count<dup):
      
      while (xpos<width+(width*count)):
        
        while(ypos<height):
          
          if ((orderValue+count)%4==1):
            
            pixel=self.getPixel(xpos,ypos)
            lum=self.getLumVal(pixel)
            color=self.postColorOne(lum)
            pixel.setColor(color)
            
          elif((orderValue+count)%4==2):
            
            pixel=self.getPixel(xpos,ypos)
            lum=self.getLumVal(pixel)
            color=self.postColorTwo(lum)
            pixel.setColor(color)
          
          elif ((orderValue+count)%4==3):
            
            pixel=self.getPixel(xpos,ypos)
            lum=self.getLumVal(pixel)
            color=self.postColorThree(lum)
            pixel.setColor(color)
          
          else:
            
            pixel=self.getPixel(xpos,ypos)
            lum=self.getLumVal(pixel)
            color=self.postColorFour(lum)
            pixel.setColor(color)
          
          ypos+=1
        xpos+=1
        ypos=0
        
      count+=1
    
    return smartPicture(self)
      
def main():

  file=pickAFile()
  pic1=smartPicture(file,1,1)
    
  pic2=pic1*4
  pic3=pic1*4
  pic4=pic1*4
  pic5=pic1*4
  
  post1=pic2.posterizeRow(1)
  post2=pic3.posterizeRow(2)
  post3=pic4.posterizeRow(3)
  post4=pic5.posterizeRow(4)
  
    
  part1=post1+post2
  part2=post3+post4
  
  if (part1!=part2):
    print "they are not equal"
    return
  else:
    print "they are equal"
  
  final=part1+part2
  
  show(final)
  file2=pickAFile()
  writePictureTo(final,file2)
  
  
