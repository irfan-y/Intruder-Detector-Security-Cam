import cv2

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id = "pic"
sampleNum = 0


def new_func(detector, img):
    return detector.detectMultiScale(img, 1.3, 5);


while (True):
    ret, img = cam.read()
    faces = new_func(detector, img)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(faces) > 0:
        sampleNum += 1
        cv2.imwrite(r"D:\Security Check\\" + Id + '.' + str(sampleNum) + ".jpg", img[y:y + h, x:x + w])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif sampleNum > 1:
        cam.release()
        cv2.destroyAllWindows()
        break
cam.release()
cv2.destroyAllWindows()  # Do not open camera window