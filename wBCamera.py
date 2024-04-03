from picamera2 import Picamera2,Preview
from picamera2.encoders import H264Encoder, Quality
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
def takeVideo(cameraObj,seconds=10,resolution=(1920, 1080),frames=30,camQuality=Quality.HIGH):
    #Note: Takes about 5GB for OS system. 16 GB for the entire SD card = 12.5GB
    #Note: Consider different Encoder
    """
    cameraObj= Camera Object
    camQuality = Sets the quality
    """
    video_config=cameraObj.create_video_configuration(buffer_count=6,main=getMainSettings(resolution),controls=getControlSettings(frameRate=30))
    cameraObj.configure(video_config)
    video_encoder=H264Encoder(10000000)###See if this encoder thin is necessary
    video_path="/home/ubnl/Documents/create_video.mp4"
    enablePreview(cameraObj)
    print("Recording soon")
    sleep(1)
    cameraObj.start_recording(video_encoder,video_path)#,quality=camQuality)
    sleep(seconds)
    cameraObj.stop_recording()
    endPreview(cameraObj)
    print("End preview")
def enablePreview(cam):
    cam.start_preview(Preview.QTGL)
def endPreview(cam):
    cam.stop_preview()
def getControlSettings(frameRate=30):
    """
    Returns back a dictionary of controls to be set
    Refer to: "Camera Controls" in the PiCamera2 documentation
    frameRate=30(default)
    """
    return {"FrameRate":frameRate}
def getMainSettings(size=(1440,1080)):
    """
    Returns the settings used in main
    Appendix B: Camera configuration parameters
    
    """
    return {"size":size}
    
def playAround():
    camera=Picamera2()
    takeVideo(camera,20,(1536,864),15)
    
def main():
    """
    Should I enable HDR?
    Note: Low RAM Amount
    """
    print("E")
    playAround()
main()
    #takePicture(camera,seconds=2,photos=5)
    #takeVideo(camera,seconds=10)=
#Burn wire: If the balloon is stuck at a certain altitude of x amount of seconds then cut the rope
    
