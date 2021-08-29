# For static images:
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180:
        angle = 360-angle
        
    return angle            
        
IMAGE_FILES = []
BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(static_image_mode=True,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5) as pose:
    image = cv2.imread('test.jpg')
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
        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        angle = calculate_angle(shoulder,elbow,wrist)
        #각도 표시
        cv2.putText(annotated_image,str(angle),tuple(np.multiply(elbow, [500, 750]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
    except:
        pass
    
    
    # Draw pose landmarks on the image.
    mp_drawing.draw_landmarks(annotated_image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    
    # Plot pose world landmarks.
    mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)


    cv2.imshow('test.png', annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



        
'''
for lndmrk in mp_pose.PoseLandmark:
    print(lndmrk)
    
landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]    
print(landmarks)    
    
    
    
'''