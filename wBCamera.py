from picamera2 import Picamera2,Preview
from picamera2.encoders import H264Encoder, Quality
from time import sleep

global photoCount
photoCount=0
#This is for when we manage photos
def takePicture(cameraObj,seconds=2,photos=4,resolution=(2592, 1944)):
    """
    cameraObj=A camera object to take a picture with 
    seconds = Must be over 2 seconds. Takes a picture. Seconds in between each photo shot.
    """
    photo_path='/home/ubnl/Documents/image%s.jpg'
    #If PhotoPath crashes just set Documents/image%s.jpg -> Documents/image1.jpg
    #Note this will overwrite the previous photo each time
    if(seconds >= 2):
        enablePreview(cameraObj)
        for i in range(photos):
            sleep(seconds)
            #check storage before taking a picture
            cameraObj.capture_file(photo_path%photoCount)
            #And replace this %i if you replace the photo_path
            #I guess I could make a function for it in case it runs out of space
            photoCount+=1
        endPreview(cameraObj)
    else:
        return "Photo not taken because seconds given is: "+str(seconds)
    #Solar Eclipse time 3 minutes 45 seconds -> 225/2 -> 112 Pictures approximately
def takeVideo(cameraObj,seconds=10,resolution=(1920, 1080),frames=30,camQuality=Quality.HIGH):
    #Note: Takes about 5GB for OS system. 16 GB for the entire SD card = 12.5GB
    #Note: Consider different Encoder
    """
    cameraObj= Camera Object
    seconds=duration of the video
    camQuality = Sets the quality
    frames=Frames of the video
    resolution = Size of the image
    """
    video_config=cameraObj.create_video_configuration(buffer_count=6,main=getMainSettings(resolution),controls=getControlSettings(frameRate=30))
    cameraObj.configure(video_config)
    video_encoder=H264Encoder(10000000)###See if this encoder thin is necessary
    video_path="/home/ubnl/Documents/create_video.h264"
    enablePreview(cameraObj)
    print("Recording soon")
    sleep(1)
    cameraObj.start_recording(video_encoder,video_path,quality=camQuality)
    sleep(seconds)
    cameraObj.stop_recording()
    endPreview(cameraObj)
    print("End preview")
def enablePreview(cam):
    """
    Creates a preview via camera passed in
    """
    cam.start_preview(Preview.QTGL)
def endPreview(cam):
    """
    Disables the preview via same camera
    """
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
    #takeVideo(camera,seconds=10,resolution=(800,500),frames=120,camQuality=Quality.HIGH)
    takePicture(camera)
def main():
    """
    Should I enable HDR?
    Note: Low RAM Amount
    """
    print("Running Code")
    playAround()
main()
#Burn wire: If the balloon is stuck at a certain altitude of x amount of seconds then cut the rope
