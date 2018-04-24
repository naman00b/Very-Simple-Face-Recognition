import cv2
import sys

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def get_image():
 retval, im = camera.read()
 return im
for i in range(ramp_frames):
 temp = get_image()
print("Please wait,we are loading your desired image...")

del(camera)
imagePath = ('C:\\Users\\Mr.X\\Desktop\\Working Minor\\offline-images\\1.jpeg')
cascPath = ('C:\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags =cv2.CASCADE_SCALE_IMAGE
)
print("Found {0} faces!".format(len(faces)))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found", image)
cv2.waitKey(0)
