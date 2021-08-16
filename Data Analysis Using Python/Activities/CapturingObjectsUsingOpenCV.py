"""
Begin Capturing Images.
Press [y] to take electronic images and press [n] to take non-electronic images
Pressing the [ESC] button will make you leave the program...
Note: You can only take 10 images of each category!
The program is dynamic as it allows the user to capture images with dynamic labelling

#! path(s) should lead to a folder directory that already exists!
#? Improvement of program include (1) automating directory creation if the folders to store the 
#? images in don't exist yet
"""
import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python webcam app")

electronic_images = 0
non_electronic_images = 0
print(
    "Begin Capturing Images.\nPress [y] to take electronic images and press [n] to take non-electronic images"
)
print("Pressing the [ESC] button will make you leave the program...")
print("Note: You can only take 10 images of each category!\n")
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == 110 and non_electronic_images < 10:
        # 'n' is pressed pressed
        path = r"C:\Users\core i5\Desktop\GitHub\DataSci\Data Analysis and Tools\non_electronic_objects"
        # path should be a folder that has already been created.
        img_name = "nonElectronicImageNum{}.png".format(non_electronic_images + 1)
        cv2.imwrite(os.path.join(path, img_name), frame)
        print("{} taken!".format(img_name))
        non_electronic_images += 1
    elif k == 121 and electronic_images < 10:
        # 'y' is pressed pressed
        path = r"C:\Users\core i5\Desktop\GitHub\DataSci\Data Analysis and Tools\electronic_objects"
        img_name = "ElectronicImageNum{}.png".format(electronic_images + 1)
        cv2.imwrite(os.path.join(path, img_name), frame)
        print("{} taken!".format(img_name))
        electronic_images += 1
    elif electronic_images + non_electronic_images == 20:
        print("You have already captured 10 electronic and\n10 non-electronic images")
        break
    else:
        continue

cam.release()
cv2.destroyAllWindows()
