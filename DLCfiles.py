from PIL import Image
import os
temp_path="testhahaha.png"
import PIL.ImageShow
#3840x2160
def imageSize(size):
  if(size=="HD"):
    #1920x1080
    return (1920,1080)
  elif(size=="4K"):
    return (3840,2160)
def alterImage(image_path,size):
  """
  Purpose: Alters an image and adds "_" to indicate that it was copied
  """
  img=Image.open(image_path)
  changed_img=img.resize((size))
  changed_img.save("_"+image_path)
def changeImages(folder_path_dir,photo_size=(3840,2160)):
  """
  Given a directory of images change based on quality
  """
  for images in os.listdir(folder_path_dir):
    alterImage(images,photo_size)
#alterImage("rasberryPI_img_2.jpg",imageSize("4K"))
changeImages("ImageFolder")
#def checkStorage(folder_path)
