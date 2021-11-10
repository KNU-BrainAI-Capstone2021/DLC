import cv2
def cut_img(box_x,box_y,box_w,box_h,path):
    global dst_cut
    
    src = cv2.imread(path)
    dst_cut = src[box_y:box_h, box_x:box_w].copy()
    
    cv2.imshow("dst", dst)
    cv2.imwrite("cut_cloth.png", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()