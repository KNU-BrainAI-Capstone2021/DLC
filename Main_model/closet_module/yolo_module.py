import cv2
import numpy as np
import os

class yolo:
    def __init__(self,capture_img,show):
        self.capture_img=capture_img
        self.show=show
        
    def show_category(img):
        cv2.imshow("Image", img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    
    def detect_cloth(self):
        landmark=[]
        # Load Yolo
        net = cv2.dnn.readNet("yolov3-df2_15000.weights", "yolov3-df2.cfg")
        classes = [] 
        with open("df2.names", "r") as f: classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()] 
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        # Loading image
        #input 이미지 불러오기
        img = self.capture_img
        #이미지 크기 조절
        img = cv2.resize(img, None, fx=1.0, fy=1.0)
        height, width, channels = img.shape
        # Detecting objects 
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False) 
        net.setInput(blob) 
        outs = net.forward(output_layers)
        # Showing informations on the screen 
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores) 
                confidence = scores[class_id]
                if confidence > 0.5: #confidence 값이 1에 가까우면 정확도가 높아지고, 0에 가까우면 정확도가 떨어지지만 검출되는 개체 수가 많아진다.
                    # Object detected 
                    center_x = int(detection[0] * width) 
                    center_y = int(detection[1] * height) 
                    w = int(detection[2] * width) 
                    h = int(detection[3] * height) 
                    # Rectangle coordinates 
                    x = int(center_x - w / 2) 
                    y = int(center_y - h / 2) 
                    boxes.append([x, y, w, h]) 
                    confidences.append(float(confidence)) 
                    class_ids.append(class_id)
        p=''
        #중복박스제거코드            
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN 
        for i in range(len(boxes)): 
            if i in indexes:
                x, y, w, h = boxes[i] 
            label = str(classes[class_ids[i]])
            p=p+f'{i}번:'+label+' '
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
        
        if self.show == True:
            self.show_category(img)
        
        print('추출을 원하는 옷의 종류를 선택하여 주십시요:\n'+p)
        num=int(input())
        category=str(classes[class_ids[num]])

        position_x=boxes[num][0]-30
        position_y=boxes[num][1]-30
        position_w=boxes[num][0]+boxes[num][2]+30
        position_h=boxes[num][1]+boxes[num][3]+20
        landmark=[position_x,position_y,position_w,position_h,category]
        
        return landmark
    
