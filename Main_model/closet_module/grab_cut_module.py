import cv2
import numpy as np
import os


#의상저장과정
BLUE, GREEN, RED, BLACK, WHITE = (255,0,0),(0,255,0),(0,0,255),(0,0,0),(255,255,255)
DRAW_BG = {'color':BLACK,'val':0}
DRAW_FG = {'color':WHITE,'val':1}

rect = {0,0,1,1}
drawing =False
rectangle = False
rect_over = False
rect_or_mask = 100
value = DRAW_FG
thickness =3

def onMouse(event,x,y,flags,param):
    global ix, iy, contour_img, contour_img2, drawing, value, mask, rectangle
    global rect, rect_or_mask, rect_over
    global box_x,box_y,box_w,box_h

    if event == cv2.EVENT_RBUTTONDOWN:
        rectangle = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if rectangle:
            contour_img=contour_img2.copy()
            rect = (min(ix,x),min(iy,y),abs(ix-x),abs(iy-y))
            rect_or_mask=0
            
    elif event == cv2.EVENT_RBUTTONUP:
        rectangle = False
        rect_over = True
        cv2.rectangle(contour_img,(box_x, box_y), (box_w, box_h),RED,2)
        
        rect = (min(box_x,box_w),min(box_y,box_h),abs(box_x-box_w),abs(box_y-box_h))
        rect_or_mask=0
        print('n:적용하기')

    if event == cv2.EVENT_LBUTTONDOWN:
        if not rect_over:
            print('마우스 왼쪽 버튼을 누른채로 전경이 되는 부분을 선택하세요')
        else:
            drawing = True
            cv2.circle(contour_img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(contour_img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            drawing = False
            cv2.circle(contour_img,(x,y),thickness,value['color'],-1)
            cv2.circle(mask,(x,y),thickness,value['val'],-1)
    return

def grabcut(det_img,p_x,p_y,p_w,p_h):
    global ix, iy, contour_img, contour_img2, drawing, value, mask, rectangle
    global rect, rect_or_mask, rect_over
    global box_x,box_y,box_w,box_h

    box_x=p_x
    box_y=p_y
    box_w=p_w
    box_h=p_h
    
    contour_img = det_img
    contour_img = cv2.resize(contour_img, None, fx=1.0, fy=1.0)
    contour_img2 = contour_img.copy()

    mask = np.zeros(contour_img.shape[:2], dtype=np.uint8)
    output = np.zeros(contour_img.shape,np.uint8)

    cv2.namedWindow('output', cv2.WINDOW_NORMAL)
    cv2.namedWindow('input', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('input',onMouse, param=(contour_img,contour_img2))


    print('오른쪽 마우스 버튼을 누르고 영역을 지정한 후 n을 누르세요')

    while True:
        cv2.imshow('output',output)
        cv2.imshow('input',contour_img)

        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        if k == ord('0'):
            print('왼쪽 마우스로 제거할 부분을 표시한 후 n을 누르세요')
            value = DRAW_BG
        elif k == ord('1'):
            print('왼족 마우스로 복원할 부분을 표시한 후 n을 누르세요')
            value = DRAW_FG
        elif k == ord('r'):
            print('리셋합니다.')
            rect = (0,0,1,1)
            drawing =False
            rectangle = False
            rect_over = False
            rect_or_mask = 100
            value = DRAW_FG
            contour_img = contour_img2.copy()
            mask = np.zeros(contour_img.shape[:2], dtype=np.uint8)
            output = np.zeros(contour_img.shape,np.uint8)
            print('0:제거배경선택 1:복원전경선택 n:적용하기 r:리셋 s:저장 q:종료')

        elif k == ord('n'):
            bgdModel = np.zeros((1,65), np.float64)
            fgdModel = np.zeros((1,65), np.float64)

            if rect_or_mask == 0:
                cv2.grabCut(contour_img2, mask, rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
                rect_or_mask = 1
            elif rect_or_mask == 1:
                cv2.grabCut(contour_img2, mask, rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)
            print('0:제거배경선택 1:복원전경선택 n:적용하기 r:리셋 s:저장 q:종료')

        elif k == ord('s'):
            gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
            
            
            # 임계값 조절
            mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)[1]
            
            # morphology 적용
            # borderconstant 사용
            kernel = np.ones((3,3), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            # anti-alias the mask
            # blur alpha channel
            mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)

            # linear stretch so that 127.5 goes to 0, but 255 stays 255
            mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

            # put mask into alpha channel
            result = output.copy()
            result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
            result[:, :, 3] = mask
            
            grab_cut_img=result
            
            print('0:제거배경선택 1: 복원전경선택 n:적용하기 r:리셋 s:저장 q:종료')
            
        elif k == ord('q'):
            #종료
            break
            
        mask2= np.where((mask==1)+(mask==3),255,0).astype('uint8')
        output = cv2.bitwise_and(contour_img2, contour_img2, mask=mask2)

        
    cv2.destroyAllWindows()
    return grab_cut_img