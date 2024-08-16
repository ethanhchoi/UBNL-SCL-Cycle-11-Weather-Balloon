from PIL import Image
import os
temp_path="testhahaha.png"
import PIL.ImageShow
#3840x2160
def imageSize(size):
  if(size=="XGA+"):
    #1920x1080
    return (1152,864)
  elif(size=="QXGA"):
    return (2048,1536)
  elif(size=="QUXGA"):
    return (3200,2400)
  elif(size=="HXGA"):
    return (4096,3072)
  elif(size=="HUXGA"):
    return (6400,4800)
def alterImage(image_path,size):
  """
  Purpose: Alters an image and adds "_" to indicate that it was copied
  """
  img=Image.open(image_path)
  changed_img=img.resize((size))
  changed_img.save("_"+image_path)
def increaseRatio(image_path,ratio_increase):
  img=Image.open(image_path)
  width,height=img.size
  changed_img=img.resize((width*ratio_increase,height*ratio_increase))
  changed_img.save("_"+image_path)
def changeImages(folder_path_dir,photo_size=(3840,2160)):
  """
  Given a directory of images change based on quality
  """
  for images in os.listdir(folder_path_dir):
    alterImage(images,photo_size)
alterImage("rasberryPI_img_0.jpg",imageSize("HUXGA"))
#increaseRatio("rasberryPI_img_2.jpg",4)
#(640,480)
#changeImages("ImageFolder")
#def checkStorage(folder_path)
