import cv2
#3840x2160
def imageSize(size):
  if(size=="HD"):
    #1920x1080
    return (1920,1080)
  elif(size=="4K"):
    return (3840,2160)
def enlargenImages(folder_path_dir,photo_size=(3840,2160)):
  for images in os.listdir(folder_path_dir):
    img=cv2.imread(images)
    cv2.resize(img,photo_size)
#def checkStorage(folder_path)
