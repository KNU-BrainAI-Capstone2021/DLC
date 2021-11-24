import cv2
import os

def cap():
    i=1
    save_path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\Avatar\\'
    #이미지캠쳐 과정
    print("q=캡쳐 후 종료,w=종료")
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('MediaPipe Pose', frame)
        #q누르면 캡쳐 후 종료    
        if cv2.waitKey(10) & 0xFF == ord('q'):
            while(True):
                file = save_path + f'Avatar{i}.png'
                if os.path.isfile(file):
                    i+=1
                    continue
                cv2.imwrite(save_path + f'Avatar{i}.png',frame)
                break
            break
        #w누르면 바로 종료
        elif cv2.waitKey(10) & 0xFF == ord('w'):
            break

    cap.release()
    cv2.destroyAllWindows()