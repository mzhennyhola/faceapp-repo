import cv2
import streamlit as st




# Detect the faces using the face cascade classifier
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

# Initialize the webcam
camera = cv2.VideoCapture(0)
while True:
    _, frame = camera.read()   #....................................... Initiate the camera
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #.................. Grayscale it using the cv grayscale library

#   Detect the faces using the face cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

#   Draw rectangles around the detected faces
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (225, 255, 0), 2)

# Display the frames
    cv2.imshow('Face Detection using Viola-Jones Algorithm', frame)

# Exit the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break
# Release the webcam and close all windows
camera.release()
cv2.destroyAllWindows()