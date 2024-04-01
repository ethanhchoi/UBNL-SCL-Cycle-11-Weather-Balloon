from picamera import PiCamera
from time import sleep


photoCount=0
#This is for when we manage photos
def takePicture(cameraObj,seconds=2,photos=112,resolution=(2592, 1944)):
    """
    cameraObj=A camera object to take a picture with 
    seconds = Must be over 2 seconds. Takes a picture.
    """
    photo_path='/home/pi/Desktop/image%s.jpg'
    cameraObj.resolution = resolution
    cameraObj.framerate = 15
    if(seconds >= 2):
        cameraObj.start_preview()
        for i in range(photos):
            sleep(seconds)
            #check storage before taking a picture
            cameraObj.capture(photo_path%photoCount)
            #/home/pi/Desktop/image%s.jpg
            #I guess I could make a function for it in case it runs out of space
            photoCount+=1
        cameraObj.close_preview()
    else:
        return "Photo not taken because seconds given is: "+str(seconds)
    #Solar Eclipse time 3 minutes 45 seconds -> 225/2 -> 112 Pictures approximately
def takeVideo(cameraObj,seconds=225,resolution=(1920, 1080)):
    #Note: Takes about 5GB for OS system. 16 GB for the entire SD card = 12.5GB
    #
    #seconds defaults to the amount of time during the solar eclipse
    cameraObj.resolution = resolution
    cameraObj.framerate = 120
    video_path='/home/pi/Desktop/video.h264'
    cameraObj.start_preview()
    cameraObj.start_recording(video_path)
    sleep(seconds)
    cameraObj.stop_recording()
    cameraObj.stop_preview()
def main():
    camera = PiCamera()
    takePicture(camera,seconds=2,photos=5)
    takeVideo(camera,seconds=10)
#Burn wire: If the balloon is stuck at a certain altitude of x amount of seconds then cut the rope
    
