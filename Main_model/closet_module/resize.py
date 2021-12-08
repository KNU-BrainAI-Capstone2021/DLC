import cv2
import numpy as np
import os
import mediapipe as mp

from closet_module import pose_module as pm
from closet_module import yolo_module as ym
from closet_module import cut_img_module as cim

class resize:
    def __init__(self,avatar_img,cap_img,grab_img,choice):
        self.cap_img = cap_img
        self.grab_img = grab_img
        self.choice = choice
        
        self.avatar_coord=pm.check_landmark(avatar_img)
        self.cloth_coord=pm.check_landmark(self.cap_img)
        
    def cal_ratio(self):
        #좌표불러오기
        avatar_land=self.avatar_coord
        cloth_land=self.cloth_coord
        
        if self.choice:
            avatar_x_len = avatar_land[3][0]-avatar_land[0][0]#아바타 가로길이
            avatar_y_len = avatar_land[1][1]-avatar_land[0][1]#아바타 세로길이

            cloth_x_len = cloth_land[3][0]-cloth_land[0][0]#옷 가로길이
            cloth_y_len = cloth_land[1][1]-cloth_land[0][1]#옷 세로길이
            
        else:
            avatar_x_len = avatar_land[4][0]-avatar_land[1][0]#아바타 가로길이
            avatar_y_len = avatar_land[2][1]-avatar_land[1][1]#아바타 세로길이

            cloth_x_len = cloth_land[4][0]-cloth_land[1][0]#옷 가로길이
            cloth_y_len = cloth_land[2][1]-cloth_land[1][1]#옷 세로길이
        
        #비율
        ratio=[avatar_x_len/cloth_x_len, avatar_y_len/cloth_y_len]
        
        return ratio
        
    def resize(self):
        ratio = self.cal_ratio()
        resize_grab_cut_img = cv2.resize(self.grab_img, None, fx=ratio[0], fy=ratio[1])

        return resize_grab_cut_img

    def cut(self,var):
        ratio = self.cal_ratio()
        img=self.resize()

        #아바타와 옷이미지의 랜드마크와 detecting box위치정보
        a_land=self.avatar_coord

        #리사이즈된 옷의 좌표 구하기
        c_land=pm.check_landmark_resize(self.cap_img,ratio[0],ratio[1])

        #이미지 크기 자르기
        if self.choice:
            x=c_land[6][0]-50
            y=c_land[0][1]-80
            w=c_land[7][0]+50
            h=int(var*ratio[1])
        else:
            x=c_land[2][0]-50
            y=c_land[1][1]-80
            w=c_land[5][0]+50
            h=img.shape[0]
        #이미지 cut
        
        src = img
        cut_img = src[y:h, x:w].copy()

        return cut_img
