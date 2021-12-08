import os
import math

###########################################################################
# train 70% / valid 10% / test 20%
train_set_ratio = 70
validation_set_ratio = 10
test_set_ratio = 20
############################################################################

# file_path
file_path = 'path' # test data 경로
# 역슬래쉬가 아닌 /로 구분하기 위해 변경
file_path_as_originSlash = file_path[:-1] + "/"

file_names = os.listdir(file_path)
file_len = len(file_names)
i=0
while i<file_len:
    temp_fileName = file_names[i]
    if temp_fileName[-4:] == ".txt":
        file_names.pop(i)
        file_len = len(file_names)
        #print(str(i) + "   " + str(file_len) + "    " + temp_fileName)
    else: i += 1

# 1. Test Set 목록
print("****************** 1. Train Set 목록(비율: " + str(train_set_ratio) + "%) ******************")
for i in range(0, math.ceil(file_len * (train_set_ratio / 100))):
    print('data/' + file_path_as_originSlash + file_names[i])
final_index = math.ceil(file_len * (train_set_ratio / 100))

# 2. Validation Set 목록
print("****************** 2. Validation Set 목록(비율: " + str(validation_set_ratio) + "%) ******************")
for i in range(final_index, final_index+ math.ceil(file_len * (validation_set_ratio / 100))):
    print('data/' + file_path_as_originSlash + file_names[i])
final_index = final_index + math.ceil(file_len * (validation_set_ratio / 100))

# 3. Test Set 목록
print("****************** 3. Test Set 목록(비율: " + str(test_set_ratio) + "%) ******************")
for i in range(final_index, file_len):
    print('data/' + file_path_as_originSlash + file_names[i])
