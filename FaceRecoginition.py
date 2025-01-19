# Author : Samridhi Gupta
# Date : 19/01/2025

import cv2

# Load the face detection model
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Start video capture
video_cap = cv2.VideoCapture(0)

if not video_cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = video_cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to grayscale
    col = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the video feed
    cv2.imshow("Video_live", frame)

    # Check for key presses
    key = cv2.waitKey(1)
    if key == ord("a"):
        break

    # Check if the window is closed
    if cv2.getWindowProperty("Video_live", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release resources
video_cap.release()
cv2.destroyAllWindows()
