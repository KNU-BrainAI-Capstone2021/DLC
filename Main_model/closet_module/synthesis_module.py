import cv2
#합성과정
def synthesis(hpos,vpos,path1,path2):
    src1=cv2.imread(path1)
    src1 = cv2.resize(src1, None, fx=1.5, fy=1.5)
    src2=cv2.imread(path2)
    
    #합성영역지정하기
    rows,cols,channels = src2.shape
    roi = src1[vpos:rows+vpos, hpos:cols+hpos]
    
    #마스크와 역마스크 생성
    img2gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
    ret,mask = cv2.threshold(img2gray,0,255,cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    #로고를 검정색으로 만들기
    img1_bg = cv2.bitwise_and(roi,roi, mask=mask_inv)
    
    #로고이미지에서 로고부분만 추출하기
    img2_fg = cv2.bitwise_and(src2,src2, mask=mask)
    
    #합성하기
    dst = cv2.add(img1_bg,img2_fg)
    src1[vpos:rows+vpos, hpos:cols+hpos]= dst
    
    cv2.imshow('syntesis_test.png',src1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()