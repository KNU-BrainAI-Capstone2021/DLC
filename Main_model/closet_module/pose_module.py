import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

#각도계산
def calculate_angle(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    cal = np.abs(radians*180.0/np.pi)

    angle = int(cal)
    if angle > 180:
        angle = 360-angle

    return angle

#각도확인
def check_angle(a,b):
    if a-1<b and a+1>b:
        return True
    else:
        return False

def check_image_angle(img):
    global img_angle1
    global img_angle2
    global img_angle3
    global img_angle4
    global img_angle5
    global img_angle6
    global img_angle7
    global img_angle8
    
    IMAGE_FILES = []
    BG_COLOR = (192, 192, 192) # gray
    with mp_pose.Pose(static_image_mode=True,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5) as pose:
        
        image = img
        image_height, image_width, _ = image.shape
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1

        try:
            landmarks = results.pose_landmarks.landmark
            LEFT_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            LEFT_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            LEFT_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            LEFT_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            LEFT_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            LEFT_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y] 

            RIGHT_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            RIGHT_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            RIGHT_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            RIGHT_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            RIGHT_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            RIGHT_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
        except:
            pass
        
        img_angle1 = calculate_angle(LEFT_shoulder,LEFT_elbow,LEFT_wrist)
        img_angle2 = calculate_angle(LEFT_elbow,LEFT_shoulder,LEFT_hip)
        img_angle3 = calculate_angle(LEFT_shoulder,LEFT_hip,LEFT_knee)
        img_angle4 = calculate_angle(LEFT_hip,LEFT_knee,LEFT_ankle)
        img_angle5 = calculate_angle(RIGHT_shoulder,RIGHT_elbow,RIGHT_wrist)
        img_angle6 = calculate_angle(RIGHT_elbow,RIGHT_shoulder,RIGHT_hip)
        img_angle7 = calculate_angle(RIGHT_shoulder,RIGHT_hip,RIGHT_knee)
        img_angle8 = calculate_angle(RIGHT_hip,RIGHT_knee,RIGHT_ankle)
        
        
def check_landmark(check_img):
    coordinates=[]
    IMAGE_FILES = []
    BG_COLOR = (192, 192, 192) # gray
    with mp_pose.Pose(static_image_mode=True,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5) as pose:
        image = check_img
        image_height, image_width, _ = image.shape
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        try:
            landmarks = results.pose_landmarks.landmark
            LEFT_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            LEFT_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            LEFT_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            LEFT_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            LEFT_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            LEFT_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y] 

            RIGHT_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            RIGHT_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            RIGHT_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            RIGHT_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            RIGHT_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            RIGHT_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
        except:
            pass
        
        coordinates=[tuple(np.multiply(RIGHT_shoulder, [1920,1080]).astype(int)),
                     tuple(np.multiply(RIGHT_hip, [1920,1080]).astype(int)),
                     tuple(np.multiply(RIGHT_ankle, [1920,1080]).astype(int)),
                     
                     tuple(np.multiply(LEFT_shoulder, [1920,1080]).astype(int)),
                     tuple(np.multiply(LEFT_hip, [1920,1080]).astype(int)),
                     tuple(np.multiply(LEFT_ankle, [1920,1080]).astype(int)),
                     tuple(np.multiply(RIGHT_wrist, [1920,1080]).astype(int)),
                     tuple(np.multiply(LEFT_wrist, [1920,1080]).astype(int))
                    ]
                    
    return coordinates


def check_landmark_resize(check_img,fx,fy):
    coordinates=[]
    IMAGE_FILES = []
    BG_COLOR = (192, 192, 192) # gray
    with mp_pose.Pose(static_image_mode=True,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5) as pose:
        image = check_img
        image_height, image_width, _ = image.shape
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        try:
            landmarks = results.pose_landmarks.landmark
            LEFT_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            LEFT_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            LEFT_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            LEFT_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            LEFT_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            LEFT_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y] 

            RIGHT_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            RIGHT_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            RIGHT_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            RIGHT_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            RIGHT_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            RIGHT_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
        except:
            pass
        
        coordinates=[tuple(np.multiply(RIGHT_shoulder, [1920*fx,1080*fy]).astype(int)),
                     tuple(np.multiply(RIGHT_hip, [1920*fx,1080*fy]).astype(int)),
                     tuple(np.multiply(RIGHT_ankle, [1920*fx,1080*fy]).astype(int)),
                     
                     tuple(np.multiply(LEFT_shoulder, [1920*fx,1080*fy]).astype(int)),
                     tuple(np.multiply(LEFT_hip, [1920*fx,1080*fy]).astype(int)),
                     tuple(np.multiply(LEFT_ankle, [1920*fx,1080*fy]).astype(int)),
                     tuple(np.multiply(RIGHT_wrist, [1920*fx,1080*fy]).astype(int)),
                     tuple(np.multiply(LEFT_wrist, [1920*fx,1080*fy]).astype(int))
                    ]
                    
    return coordinates



def video_angle(choice):
    cap = cv2.VideoCapture(cv2.CAP_DSHOW+1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)

            #각도계산
            try:
                landmarks = results.pose_landmarks.landmark
                LEFT_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                LEFT_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                LEFT_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                LEFT_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                LEFT_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                LEFT_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y] 

                RIGHT_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                RIGHT_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                RIGHT_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                RIGHT_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                RIGHT_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                RIGHT_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y] 

                video_angle1 = calculate_angle(LEFT_shoulder,LEFT_elbow,LEFT_wrist)
                video_angle2 = calculate_angle(LEFT_elbow,LEFT_shoulder,LEFT_hip)
                video_angle3 = calculate_angle(LEFT_shoulder,LEFT_hip,LEFT_knee)
                video_angle4 = calculate_angle(LEFT_hip,LEFT_knee,LEFT_ankle)
                video_angle5 = calculate_angle(RIGHT_shoulder,RIGHT_elbow,RIGHT_wrist)
                video_angle6 = calculate_angle(RIGHT_elbow,RIGHT_shoulder,RIGHT_hip)
                video_angle7 = calculate_angle(RIGHT_shoulder,RIGHT_hip,RIGHT_knee)
                video_angle8 = calculate_angle(RIGHT_hip,RIGHT_knee,RIGHT_ankle)

                #각도 표시
                #상체
                #왼팔꿈치
                if(check_angle(img_angle1,video_angle1)):
                    cv2.putText(image,str(video_angle1),tuple(np.multiply(LEFT_elbow, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle1),tuple(np.multiply(LEFT_elbow, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)

                #왼어깨
                if(check_angle(img_angle2,video_angle2)):
                    cv2.putText(image,str(video_angle2),tuple(np.multiply(LEFT_shoulder, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle2),tuple(np.multiply(LEFT_shoulder, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)

                #오른쪽팔꿈치
                if(check_angle(img_angle5,video_angle5)):
                    cv2.putText(image,str(video_angle5),tuple(np.multiply(RIGHT_elbow, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle5),tuple(np.multiply(RIGHT_elbow, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)

                #오른쪽어깨
                if(check_angle(img_angle6,video_angle6)):
                    cv2.putText(image,str(video_angle6),tuple(np.multiply(RIGHT_shoulder, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle6),tuple(np.multiply(RIGHT_shoulder, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)    
                    
                    
                    
                    
                #하체    
                    
                #왼허리
                if(check_angle(img_angle3,video_angle3)):
                    cv2.putText(image,str(video_angle3),tuple(np.multiply(LEFT_hip, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle3),tuple(np.multiply(LEFT_hip, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
                #왼무릎
                if(check_angle(img_angle4,video_angle4)):
                    cv2.putText(image,str(video_angle4),tuple(np.multiply(LEFT_knee, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle4),tuple(np.multiply(LEFT_knee, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)

                #오른쪽허리
                if(check_angle(img_angle7,video_angle7)):
                    cv2.putText(image,str(video_angle7),tuple(np.multiply(RIGHT_hip, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle7),tuple(np.multiply(RIGHT_hip, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)

                #오른쪽무릎
                if(check_angle(img_angle8,video_angle8)):
                    cv2.putText(image,str(video_angle8),tuple(np.multiply(RIGHT_knee, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(image,str(video_angle7),tuple(np.multiply(RIGHT_hip, [1920,1080]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
                #동작일치시 캡쳐후 종료
                if choice:
                    if(all([check_angle(img_angle1,video_angle1),check_angle(img_angle2,video_angle2),check_angle(img_angle5,video_angle5),check_angle(img_angle6,video_angle6)])):
                        capture_img=frame
                        break
                
                else:
                    if(all([check_angle(img_angle3,video_angle3),check_angle(img_angle4,video_angle4),check_angle(img_angle7,video_angle7),check_angle(img_angle8,video_angle8)])):
                        capture_img=frame
                        break

            except:
                pass
            
            #웹캠영상 띄우기
            cv2.imshow('MediaPipe Pose', image)

            #q누르면 종료    
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return capture_img