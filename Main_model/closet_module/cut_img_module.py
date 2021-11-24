import cv2
def cut_img(x,y,w,h,img):
    
    src = img
    dst = src[y:h, x:w].copy()
    
    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    return dst