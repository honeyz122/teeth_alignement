import os
import cv2

picture1_dir = os.path.join("C:/Users/HONEYZ/Desktop/teeth_edge_compare/iterate_50/1")
picture2_dir = os.path.join("C:/Users/HONEYZ/Desktop/teeth_edge_compare/iterate_50/2_edge")

picture1_name = os.listdir(picture1_dir)
picture2_name = os.listdir(picture2_dir)


for i in range(len(picture1_name)):
    picture1 = cv2.imread(picture1_dir + "/" + picture1_name[i])
    picture2 = cv2.imread(picture2_dir + "/" + picture2_name[i])

    rows, colmns, channel = picture1.shape
    picture2 = cv2.resize(picture2, (colmns, rows))
    img = cv2.addWeighted(picture1, 0.4, picture2, 0.6, 0)

    cv2.imwrite(f"C:/Users/HONEYZ/Desktop/teeth_edge_compare/iterate_50/3/{picture1_name[i]}", img)

    print(f'处理第{i + 1}张')

