import cv2
import numpy as np
import os
import mediapipe as mp

from closet_module import pose_module as pm
from closet_module import yolo_module as ym
from closet_module import cut_img_module as cim

class resize:
    def __init__(self,avatar_img,cap_img,grab_img,choice):
        self.avatar_img = avatar_img
        self.cap_img = cap_img
        self.grab_img = grab_img
        self.choice = choice
        
        
        self.avatar_coord=pm.check_landmark(self.avatar_img)
        self.cloth_coord=pm.check_landmark(self.cap_img)
        self.avatar_position=ym.detect_cloth(avatar_img)
        self.cloth_position=ym.detect_cloth(cap_img)
        
    def cal_ratio(self):
        #좌표불러오기
        avatar_land=self.avatar_coord
        cloth_land=self.cloth_coord
        
        if self.choice == 'top':
            avatar_x_len = avatar_land[3][0]-avatar_land[0][0]#아바타 가로길이
            avatar_y_len = avatar_land[1][1]-avatar_land[0][1]#아바타 세로길이

            cloth_x_len = cloth_land[3][0]-cloth_land[0][0]#옷 가로길이
            cloth_y_len = cloth_land[1][1]-cloth_land[0][1]#옷 세로길이
            
        elif self.choice == 'bottom':
            avatar_x_len = avatar_land[4][0]-avatar_land[1][0]#아바타 가로길이
            avatar_y_len = avatar_land[2][1]-avatar_land[1][1]#아바타 세로길이

            cloth_x_len = cloth_land[4][0]-cloth_land[1][0]#옷 가로길이
            cloth_y_len = cloth_land[2][1]-cloth_land[1][1]#옷 세로길이
        
        #비율
        ratio=[avatar_x_len/cloth_x_len, avatar_y_len/cloth_y_len]
        
        return ratio
        
    def resize(self):
        ratio = self.cal_ratio()
        cut_img = cv2.resize(self.grab_img, None, fx=ratio[0], fy=ratio[1])

        return cut_img

    def cut(self):
        ratio = self.cal_ratio()
        img=self.resize()

        #아바타와 옷이미지의 랜드마크와 detecting box위치정보
        a_p=self.avatar_position
        c_p=self.cloth_position
        a_c=self.avatar_coord

        #리사이즈된 옷의 좌표 구하기
        c_c=pm.check_landmark_resize(self.cap_img,ratio[0],ratio[1])

        #이미지 크기 자르기
        if self.choice == 'top':
            #오른쪽 어깨와 박스의 x길이차이
            a_x=a_c[0][0]-a_p[0]

            #오른쪽 어깨와 박스의 y길이차이
            a_y=a_c[0][1]-a_p[1]

            #cut시작좌표
            b_x=c_c[0][0]-a_x
            b_y=c_c[0][1]-a_y

            #cut 너비 (detecting 박스 길이)
            c_x=(c_p[2]-c_p[0])*ratio[0]

            #cut 폭 (detecting 박스 길이)
            c_y=(c_p[3]-c_p[1])*ratio[1]

            #cut끝좌표
            d_w=c_c[0][0]+int(c_x)
            d_h=c_c[0][1]+int(c_y)

        elif self.choice == 'bottom':
            #오른쪽 허리와 박스의 x길이차이
            a_x=a_c[0][0]-a_p[0]

            #오른쪽 허리와 박스의 y길이차이
            a_y=a_c[0][1]-a_p[1]

            #cut시작좌표
            b_x=c_c[0][0]-a_x
            b_y=c_c[0][1]-a_y

            #cut 너비 (detecting 박스 길이)
            c_x=(c_p[2]-c_p[0])*ratio[0]

            #cut 폭 (detecting 박스 길이)
            c_y=(c_p[3]-c_p[1])*ratio[1]

            #cut끝좌표
            d_w=c_c[0][0]+int(c_x)
            d_h=c_c[0][1]+int(c_y)

        #이미지 cut
        cut_img=cim.cut_img(b_x,b_y,d_w,d_h,img)

        return cut_img