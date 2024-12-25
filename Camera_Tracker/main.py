"""from picamera.array import PiRGBArray
from picamera import PiCamera"""
import time
import cv2

class ObjectTracker:

    def __init__(self, Camera_path : str = 0) -> None:
        self.cam = cv2.VideoCapture(Camera_path)


    def Show_Video(self):

        """# initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()

        rawCapture = PiRGBArray(camera)
        # allow the camera to warmup
        time.sleep(0.1)

        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array

        # display the image on screen and wait for a keypress
        cv2.imshow("Image", image)
        cv2.waitKey(0)"""

        while True:
            ret, frame = self.cam.read()

            # Display the captured frame
            cv2.imshow('Camera', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the capture and writer objects
        self.cam.release()
        cv2.destroyAllWindows()

    def Track(self, alorithm: str = 'haar-cascade'):

        while True:
            ret, img = self.cam.read()

            # Check if the frame was successfully captured
            if not ret:
                print("Error: Failed to grab frame from camera")
            else:
                # Converting image to grayscale
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            
            # Loading the required haar-cascade xml classifier file 
            haar_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml') 
            
            # Applying the face detection method on the grayscale image 
            faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 
            
            # Iterating through rectangles of detected faces 
            for (x, y, w, h) in faces_rect: 
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 
            
            cv2.imshow('Detected faces', img) 
            
            cv2.waitKey(0) 




test = ObjectTracker()
test.Show_Video()