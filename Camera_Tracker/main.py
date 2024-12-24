import cv2

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

"""while True:
    ret, frame = cam.read()"""



class ObjectTracker:

    def __init__(self, Camera_path : str = 0) -> None:
        self.cam = cv2.VideoCapture(Camera_path)

    def Show_Video(self,):
        while True:
            ret, frame = cam.read()

            # Display the captured frame
            cv2.imshow('Camera', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the capture and writer objects
        cam.release()
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
        