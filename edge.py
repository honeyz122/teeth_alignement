import cv2
import os

def read_path(file_pathname):

    for filename in os.listdir(file_pathname):
        print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        img = cv2.Canny(img, 80, 255)
        img2 = cv2.bitwise_not(img)
        cv2.imwrite('C:/Users/HONEYZ/Desktop/teeth_edge_compare/2_edge'+"/"+filename, img2)
read_path("C:/Users/HONEYZ/Desktop/teeth_edge_compare/2")

