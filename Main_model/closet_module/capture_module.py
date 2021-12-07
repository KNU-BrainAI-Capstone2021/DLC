import cv2
import os

running = True
picture = 0

def cap():
    global running
    global picture
    i=1
    save_path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\Avatar\\'
    cap = cv2.VideoCapture(cv2.CAP_DSHOW+0)
    while running:
        ret, frame = cap.read()
        cv2.imshow('Avatar_cap', frame)
        #q누르면 캡쳐 후 종료    
        if cv2.waitKey(3) & picture == 1:
            while(True):
                file = save_path + f'Avatar{i}.png'
                if os.path.isfile(file):
                    i+=1
                    continue
                cv2.imwrite(save_path + f'Avatar{i}.png',frame)
                picture = 0
                break
            break

    cap.release()
    cv2.destroyAllWindows()