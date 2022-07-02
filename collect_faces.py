import os
import  cv2
import  sys
path='photots'
def faces_from_cam():

    userName = str(input("please enter the username for this record "))
    images_path = os.path.join(r"C:\Users\hp\PycharmProjects\face\photots", userName)
    #if not os.path.isdir(images_path):
     #   os.makedirs(images_path)
    image_counter = 0
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam.set(10,70)
    classefier = cv2.CascadeClassifier( 
        r"C:\Users\hp\Downloads\project (1)\faceRE\faceRE\harr\haarcascade_frontalface_default.xml")
    if cam.isOpened() == False:
        print("the app will close ")
        sys.exit(1)
    while True:
        succ, Image = cam.read()
        if succ:
            img_rgb = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
            faces = classefier.detectMultiScale(img_rgb)
            cv2.imshow("window", Image)
            Key = cv2.waitKey(1)
            if Key == ord("x".lower()):
                if len(faces) == 1:
                    file_name = os.path.join(path, f"{images_path}.jpg")
                    s = cv2.imwrite(file_name, Image)
                    print(file_name, s)
                    image_counter += 1
                    if image_counter == 1:
                        cv2.destroyAllWindows()
                        break
        if Key == ord("q".lower()):
            break

    cv2.destroyAllWindows()

faces_from_cam()