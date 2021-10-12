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
    if a-3<b and a+3>b:
        return True
    else:
        return False
        
#이미지에서 pose detecting
IMAGE_FILES = []
BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(static_image_mode=True,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5) as pose:
    image = cv2.imread('capture_video.png')
    image_height, image_width, _ = image.shape
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    annotated_image = image.copy()
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    annotated_image = np.where(condition, annotated_image, bg_image)
    

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
        
        img_angle1 = calculate_angle(LEFT_shoulder,LEFT_elbow,LEFT_wrist)
        img_angle2 = calculate_angle(LEFT_elbow,LEFT_shoulder,LEFT_hip)
        img_angle3 = calculate_angle(LEFT_shoulder,LEFT_hip,LEFT_knee)
        img_angle4 = calculate_angle(LEFT_hip,LEFT_knee,LEFT_ankle)
        img_angle5 = calculate_angle(RIGHT_shoulder,RIGHT_elbow,RIGHT_wrist)
        img_angle6 = calculate_angle(RIGHT_elbow,RIGHT_shoulder,RIGHT_hip)
        img_angle7 = calculate_angle(RIGHT_shoulder,RIGHT_hip,RIGHT_knee)
        img_angle8 = calculate_angle(RIGHT_hip,RIGHT_knee,RIGHT_ankle)
    except:
        pass
        
        
#웹캠에서 pose detecting
# For webcam input:
cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        #랜드마크그리기
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
            #왼팔꿈치
            if(check_angle(img_angle1,video_angle1)):
                cv2.putText(image,str(video_angle1),tuple(np.multiply(LEFT_elbow, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
            else:
                cv2.putText(image,str(video_angle1),tuple(np.multiply(LEFT_elbow, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            
            #왼어깨
            if(check_angle(img_angle2,video_angle2)):
                cv2.putText(image,str(video_angle2),tuple(np.multiply(LEFT_shoulder, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
            else:
                cv2.putText(image,str(video_angle2),tuple(np.multiply(LEFT_shoulder, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            
            #왼허리
            cv2.putText(image,str(video_angle3),tuple(np.multiply(LEFT_hip, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            
            #왼무릎
            cv2.putText(image,str(video_angle4),tuple(np.multiply(LEFT_knee, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            
            #오른쪽팔꿈치
            if(check_angle(img_angle5,video_angle5)):
                cv2.putText(image,str(video_angle5),tuple(np.multiply(RIGHT_elbow, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
            else:
                cv2.putText(image,str(video_angle5),tuple(np.multiply(RIGHT_elbow, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            
            #오른쪽어깨
            if(check_angle(img_angle6,video_angle6)):
                cv2.putText(image,str(video_angle6),tuple(np.multiply(RIGHT_shoulder, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
            else:
                cv2.putText(image,str(video_angle6),tuple(np.multiply(RIGHT_shoulder, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            
            #오른쪽허리
            cv2.putText(image,str(video_angle7),tuple(np.multiply(RIGHT_hip, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            
            #오른쪽무릎
            cv2.putText(image,str(video_angle8),tuple(np.multiply(RIGHT_knee, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            #동작일치시 캡쳐후 종료
            if (all([check_angle(img_angle1,video_angle1),check_angle(img_angle2,video_angle2),check_angle(img_angle5,video_angle5),check_angle(img_angle6,video_angle6)])):
                cv2.imwrite('test.png', frame)
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