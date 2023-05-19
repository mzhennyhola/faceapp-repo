import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default .xml')

# # Initialize the webcam
# camera = cv2.VideoCapture(0)
# while True:
#     _, frame = camera.read()   #....................................... Initiate the camera
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #.................. Grayscale it using the cv grayscale library

# #   Detect the faces using the face cascade classifier
#     faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.3, minNeighbors= 5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

# #   Draw rectangles around the detected faces
#     for (x, y, width, height) in faces:
#         cv2.rectangle(frame, (x, y), (x + width, y + height), (225, 255, 0), 2)

# # Display the frames
#     cv2.imshow('Face Detection using Viola-Jones Algorithm', frame)

# # Exit the loop when 'q' is pressed
#     if cv2.waitKey(1) == ord('q'):
#         break
# # Release the webcam and close all windows
# camera.release()
# cv2.destroyAllWindows()


#....................IMPLEMENT YOUR STREAMLIT....................

st.markdown("<h1 style = 'color: #FF6000'>THE ENIOLA ODUGBESI INTERNATIONAL AIRPORT </h1> ", unsafe_allow_html = True)
st.markdown("<h6 style = 'top_margin: 0rem; color: #27E1C1'>Built by Odugbesi Nofisat </h6>", unsafe_allow_html = True)

#Add an Image to the page
st.image('face 3.jpeg', caption = 'FACE DETECTOR', width = 600)

#Create a line and space underneath
st.markdown('<hr><hr><br>', unsafe_allow_html= True)

user_name = st.text_input("Please Enter Your Full Name")
# st.button("SUBMIT")
if (st.button("SUBMIT")):
    st.write (f"Welome {user_name} to the Eniola Odugbesi International Airport!!!")

#CREATE A LINE AND A SPACE UNDERNEATH
st.markdown('<hr><hr><br>', unsafe_allow_html= True)

# Add instructions to the Streamlit app interface to guide the user on how to use the app.
# st.button("CLICK ME FOR INSTRUCTIONS")
if (st.button("CLICK ME FOR INSTRUCTIONS")):
    st.success(f'Hello {user_name}, these are the guidelines for the app usage')
    st.write('Press the camera button for our model to detect your face')
    st.write('Use the MinNeighbour slider to adjust how many persons the camera should detect')
    st.write('Use the Scaler slider to specify how much the image size is reduced at each image scale')

st.markdown('<br>', unsafe_allow_html= True)

#START THE FACE DETECTION
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default .xml')
#camera = cv2.VideoCapture(0)

#st.markdown('<br>', unsafe_allow_html= True)

Min_Neighbour = st.slider("Adjust Min Neighbour", 1, 10, 5)
Scale_factorization = st.slider("Adjust Scale Factor", 1.0, 3.0, 1.3)


if st.button("FACE DETECT"):
# INITIALIZE THE WEBCAM 
  #camera = cv2.VideoCapture(0)
#while True:
       # _, camera_view = camera.read()   #....................................... Initiate the camera
        #gray = cv2.cvtColor(camera_view, cv2.COLOR_BGR2GRAY) #.................. Grayscale it using the cv grayscale library
    #   Detect the faces using the face cascade classifier
        #faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
        #faces = face_cascade.detectMultiScale(gray, scaleFactor= Scale_factorization, minNeighbors= Min_Neighbour, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    #   Draw rectangles around the detected faces
        #for (x, y, width, height) in faces:
            #cv2.rectangle(camera_view, (x, y), (x + width, y + height), (225, 255, 0), 2)
    # Display the camera_views
        #cv2.imshow('Face Detection using Viola-Jones Algorithm', camera_view)
    # Exit the loop when 'q' is pressed
        #if cv2.waitKey(1) == ord('q'):
           # break
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


# let's assume the number of images gotten is 0
# img_counter = 0
# if k%256  == 32:
#     # the format for storing the images scrreenshotted
#     img_name = f'opencv_frame_{img_counter}'
#     # saves the image as a png file
#     cv2.imwrite(img_name, frame)
#     print('screenshot taken')
#     # the number of images automaticallly increases by 1
#     img_counter += 1