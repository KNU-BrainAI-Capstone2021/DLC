import random
import os
listdata = list(range(1,max+1))# 1~ max data file
random.shuffle(listdata) # 리스트 shuffle을 통해 랜덤하게 번호 부여, test, train, validation data 선정을 위해
#Img file
file_path1 = 'path' # 이미지 파일 경로
file_names1 = os.listdir(file_path1)
i = 0
for name in file_names1:
    a = listdata[i]
    src = os.path.join(file_path1, name)
    dst = str(a) + '.jpg'
    dst = os.path.join(file_path1, dst)
    os.rename(src, dst)
    i += 1
j = 0
##Label txt file
file_path2 = 'path' # txt 파일 경로, 이미지와 다른 곳으로 지정해야함
file_names2 = os.listdir(file_path2)
for name in file_names2:
    a = listdata[j]
    src = os.path.join(file_path2, name)
    dst = str(a) + '.txt'
    dst = os.path.join(file_path2, dst)
    os.rename(src, dst)
    j += 1

