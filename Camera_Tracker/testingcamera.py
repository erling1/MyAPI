
import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()
while True:
    image = picam2.capture_array()
    cv2.imshow("Frame", image)
    if(cv2.waitKey(1) == ord("q")):
        cv2.imwrite("test_frame.png", image)
        break

cv2.destroyAllWindows()






















"""import cv2

# Try opening the first available camera device (index 0 is typically the default)
cap = cv2.VideoCapture(0)  # You can also try other indices like 1, 2, etc.
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print(width)
print(height)
print(fps)


if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera successfully opened.")

    # Try capturing a frame
    ret, frame = cap.read()
    print(ret)
    print(frame)

    if not ret:
        print("Error: Failed to capture frame.")
    else:
        print("Frame captured successfully.")
        cv2.imshow('Camera', frame)

        # Wait and check for any key press (to close the window)
        cv2.waitKey(0)  # Wait indefinitely for a key press
        cv2.destroyAllWindows()

# Release the camera device
cap.release()

"""