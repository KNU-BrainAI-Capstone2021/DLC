import pandas as pd
import os

def recommend_outer(cloth):
    colors = ['beige','black','blue','brown','green','grey','khaki','navy','orange','pink','purple','red','yellow','white']
    keywords = ['dress','skirt','hoody','knit','long sleeve','shirts','short sleeve','sweat shirts','boots','dress shoes','running shoes','sandal','slip on','sneakers','blazer','blouson','cardigan','coat','field jumper','fleece','leather jacket','mustang','padding','trucker','vest','jean','shorts','sweat pants','trouser','wide jean','wide trouser']
    keys = []
    for j in range(0,len(keywords)):
        for i in range(0,len(colors)):
            keys.append(colors[i]+" "+keywords[j])
    sumsave=[]
    data = pd.read_csv('class_clothes.txt',sep='\n', header=None)[0].str.split('\t', expand=True)

    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'blazer',path+'cardigan',path+'vest',path+'coat',path+'field jumper',path+'fleece',path+'leather jacket',path+'mustang',path+'padding',path+'trucker']
    file_list=[]
    for i in range(len(path_list)):
        list_num=os.listdir(path_list[i])
        for j in range(len(list_num)):
            file_list.append(list_num[j].replace('.png',''))
            file_list.append(list_num[j].replace('.jpg',''))
    print(file_list)
    my_clothes =file_list
    my_clothesf = my_clothes.copy()
    for i in range(0,len(my_clothes)):
        my_clothesf[i] = my_clothesf[i].replace('0','')
        my_clothesf[i] = my_clothesf[i].replace('1','')
        my_clothesf[i] = my_clothesf[i].replace('2','')
        my_clothesf[i] = my_clothesf[i].replace('3','')
        my_clothesf[i] = my_clothesf[i].replace('4','')
        my_clothesf[i] = my_clothesf[i].replace('5','')
        my_clothesf[i] = my_clothesf[i].replace('6','')
        my_clothesf[i] = my_clothesf[i].replace('7','')
        my_clothesf[i] = my_clothesf[i].replace('8','')
        my_clothesf[i] = my_clothesf[i].replace('9','') ########내 옷장에 숫자 필터

    # my_clothes= [] 로 놔두고 검출된 의상 하나씩 append해서 받기
    answer = [] #추천할 의상 담는 곳
    detected_clothes = cloth # <----------------- 선택된 의상
    dc = detected_clothes.split()
    dc_type = dc[0] 
    dc_color = dc[1]
    if len(dc) ==3:
        dc_color = dc[1] + ' ' + dc[2]

    for loop in range(len(keywords)):

        a=[0 for i in range(len(keys))]
        for j in range(0,9) :
            cnt=0


            df = data[data[j].str.contains(dc_type,na=False)]
            df = df[df[j].str.contains(dc_color,na=False)]
        #    print(df[j]) # 선택한 의상이 포함된 코디맵 행/열 검출
            sumc=[[],[],[],[],[],[],[],[]]
            ii = 0

            for i in range(0,9): # i 열 돌리면서 j열이랑 일치확인

                if i==j:
                    continue
                else:

                    df_filter = df[df[i].str.contains(keywords[loop],na=False)]
                    for color in colors:

                        df_filter2 = df_filter[df_filter[i].str.contains(color,na=False)]
                        count = df_filter2[i].count()
                        sumc[ii].append(count)

                ii=ii+1    
            k=[0 for i in range(len(colors))]
            for cc in range(0,len(colors)):
                for c in range(0,8):
                    k[cc] +=sumc[c][cc]

            for h in range(0,len(colors)) :
                a[h]=a[h]+k[h]

        for i in range(0,14):
            sumsave.append(a[i]) #언급된 횟수 계산
    df1 = pd.DataFrame(keys, index=sumsave, columns=['name'])
    df2 = df1.sort_index(ascending=False) #나온 횟수대로 내림차순 정렬.

    for i in range(0,len(df2.values)):
        if df2.index[i]!=0: #언급횟수 0회 제외시키기
            #print(df2.values[i], df2.index[i])
            for j in range(0,len(my_clothes)):
                if df2.values[i] == my_clothesf[j]:
                    if df2.values[i] != detected_clothes:   
                        answer.append(my_clothes[j])

    if answer == []:
        print('추천할 의상이 없습니다')
    else :
        return answer# <-------------- 의상 추천, 이 결과값을 토대로 실제로 입은것처럼 구현
    
def recommend_top(cloth):
    colors = ['beige','black','blue','brown','green','grey','khaki','navy','orange','pink','purple','red','yellow','white']
    keywords = ['dress','skirt','hoody','knit','long sleeve','shirts','short sleeve','sweat shirts','boots','dress shoes','running shoes','sandal','slip on','sneakers','blazer','blouson','cardigan','coat','field jumper','fleece','leather jacket','mustang','padding','trucker','vest','jean','shorts','sweat pants','trouser','wide jean','wide trouser']
    keys = []
    for j in range(0,len(keywords)):
        for i in range(0,len(colors)):
            keys.append(colors[i]+" "+keywords[j])
    sumsave=[]
    data = pd.read_csv('C:\\Users\\lky\\Desktop\\class_clothes.txt',sep='\n', header=None)[0].str.split('\t', expand=True)
    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'dress',path+'hoody',path+'knit',path+'long sleeve',path+'shirts',path+'short sleeve',path+'sweat shirts',path+'blouson']
    file_list=[]
    for i in range(len(path_list)):
        list_num=os.listdir(path_list[i])
        for j in range(len(list_num)):
            file_list.append(list_num[j].replace('.png',''))
            file_list.append(list_num[j].replace('.jpg',''))
    print(file_list)
    my_clothes =file_list
    my_clothesf = my_clothes.copy()
    for i in range(0,len(my_clothes)):
        my_clothesf[i] = my_clothesf[i].replace('0','')
        my_clothesf[i] = my_clothesf[i].replace('1','')
        my_clothesf[i] = my_clothesf[i].replace('2','')
        my_clothesf[i] = my_clothesf[i].replace('3','')
        my_clothesf[i] = my_clothesf[i].replace('4','')
        my_clothesf[i] = my_clothesf[i].replace('5','')
        my_clothesf[i] = my_clothesf[i].replace('6','')
        my_clothesf[i] = my_clothesf[i].replace('7','')
        my_clothesf[i] = my_clothesf[i].replace('8','')
        my_clothesf[i] = my_clothesf[i].replace('9','') ########내 옷장에 숫자 필터

    # my_clothes= [] 로 놔두고 검출된 의상 하나씩 append해서 받기
    answer = [] #추천할 의상 담는 곳
    detected_clothes = cloth # <----------------- 선택된 의상
    dc = detected_clothes.split()
    dc_type = dc[0] 
    dc_color = dc[1]
    if len(dc) ==3:
        dc_color = dc[1] + ' ' + dc[2]
        
    for loop in range(len(keywords)):

        a=[0 for i in range(len(keys))]
        for j in range(0,9) :
            cnt=0


            df = data[data[j].str.contains(dc_type,na=False)]
            df = df[df[j].str.contains(dc_color,na=False)]
        #    print(df[j]) # 선택한 의상이 포함된 코디맵 행/열 검출
            sumc=[[],[],[],[],[],[],[],[]]
            ii = 0

            for i in range(0,9): # i 열 돌리면서 j열이랑 일치확인

                if i==j:
                    continue
                else:

                    df_filter = df[df[i].str.contains(keywords[loop],na=False)]
                    for color in colors:

                        df_filter2 = df_filter[df_filter[i].str.contains(color,na=False)]
                        count = df_filter2[i].count()
                        sumc[ii].append(count)

                ii=ii+1    
            k=[0 for i in range(len(colors))]
            for cc in range(0,len(colors)):
                for c in range(0,8):
                    k[cc] +=sumc[c][cc]

            for h in range(0,len(colors)) :
                a[h]=a[h]+k[h]

        for i in range(0,14):
            sumsave.append(a[i]) #언급된 횟수 계산
    df1 = pd.DataFrame(keys, index=sumsave, columns=['name'])
    df2 = df1.sort_index(ascending=False) #나온 횟수대로 내림차순 정렬.

    for i in range(0,len(df2.values)):
        if df2.index[i]!=0: #언급횟수 0회 제외시키기
            #print(df2.values[i], df2.index[i])
            for j in range(0,len(my_clothes)):
                if df2.values[i] == my_clothesf[j]:
                    if df2.values[i] != detected_clothes:   
                        answer.append(my_clothes[j])

    if answer == []:
        print('추천할 의상이 없습니다')
    else :
        return answer# <-------------- 의상 추천, 이 결과값을 토대로 실제로 입은것처럼 구현
    
def recommend_bottom(cloth):
    colors = ['beige','black','blue','brown','green','grey','khaki','navy','orange','pink','purple','red','yellow','white']
    keywords = ['dress','skirt','hoody','knit','long sleeve','shirts','short sleeve','sweat shirts','boots','dress shoes','running shoes','sandal','slip on','sneakers','blazer','blouson','cardigan','coat','field jumper','fleece','leather jacket','mustang','padding','trucker','vest','jean','shorts','sweat pants','trouser','wide jean','wide trouser']
    keys = []
    for j in range(0,len(keywords)):
        for i in range(0,len(colors)):
            keys.append(colors[i]+" "+keywords[j])
    sumsave=[]
    data = pd.read_csv('C:\\Users\\lky\\Desktop\\class_clothes.txt',sep='\n', header=None)[0].str.split('\t', expand=True)

    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'jean',path+'shorts',path+'sweat pants',path+'trouser',path+'wide jean',path+'wide trouser']
    file_list=[]
    for i in range(len(path_list)):
        list_num=os.listdir(path_list[i])
        for j in range(len(list_num)):
            file_list.append(list_num[j].replace('.png',''))
            file_list.append(list_num[j].replace('.jpg',''))
    print(file_list)
    my_clothes =file_list
    my_clothesf = my_clothes.copy()
    for i in range(0,len(my_clothes)):
        my_clothesf[i] = my_clothesf[i].replace('0','')
        my_clothesf[i] = my_clothesf[i].replace('1','')
        my_clothesf[i] = my_clothesf[i].replace('2','')
        my_clothesf[i] = my_clothesf[i].replace('3','')
        my_clothesf[i] = my_clothesf[i].replace('4','')
        my_clothesf[i] = my_clothesf[i].replace('5','')
        my_clothesf[i] = my_clothesf[i].replace('6','')
        my_clothesf[i] = my_clothesf[i].replace('7','')
        my_clothesf[i] = my_clothesf[i].replace('8','')
        my_clothesf[i] = my_clothesf[i].replace('9','') ########내 옷장에 숫자 필터

    # my_clothes= [] 로 놔두고 검출된 의상 하나씩 append해서 받기
    answer = [] #추천할 의상 담는 곳
    detected_clothes = cloth # <----------------- 선택된 의상
    dc = detected_clothes.split()
    dc_type = dc[0] 
    dc_color = dc[1]
    if len(dc) ==3:
        dc_color = dc[1] + ' ' + dc[2]

    for loop in range(len(keywords)):

        a=[0 for i in range(len(keys))]
        for j in range(0,9) :
            cnt=0


            df = data[data[j].str.contains(dc_type,na=False)]
            df = df[df[j].str.contains(dc_color,na=False)]
        #    print(df[j]) # 선택한 의상이 포함된 코디맵 행/열 검출
            sumc=[[],[],[],[],[],[],[],[]]
            ii = 0

            for i in range(0,9): # i 열 돌리면서 j열이랑 일치확인

                if i==j:
                    continue
                else:

                    df_filter = df[df[i].str.contains(keywords[loop],na=False)]
                    for color in colors:

                        df_filter2 = df_filter[df_filter[i].str.contains(color,na=False)]
                        count = df_filter2[i].count()
                        sumc[ii].append(count)

                ii=ii+1    
            k=[0 for i in range(len(colors))]
            for cc in range(0,len(colors)):
                for c in range(0,8):
                    k[cc] +=sumc[c][cc]

            for h in range(0,len(colors)) :
                a[h]=a[h]+k[h]

        for i in range(0,14):
            sumsave.append(a[i]) #언급된 횟수 계산
    df1 = pd.DataFrame(keys, index=sumsave, columns=['name'])
    df2 = df1.sort_index(ascending=False) #나온 횟수대로 내림차순 정렬.

    for i in range(0,len(df2.values)):
        if df2.index[i]!=0: #언급횟수 0회 제외시키기
            #print(df2.values[i], df2.index[i])
            for j in range(0,len(my_clothes)):
                if df2.values[i] == my_clothesf[j]:
                    if df2.values[i] != detected_clothes:   
                        answer.append(my_clothes[j])

    if answer == []:
        print('추천할 의상이 없습니다')
    else :
        return answer# <-------------- 의상 추천, 이 결과값을 토대로 실제로 입은것처럼 구현
    
def recommend_shoes(cloth):
    colors = ['beige','black','blue','brown','green','grey','khaki','navy','orange','pink','purple','red','yellow','white']
    keywords = ['dress','skirt','hoody','knit','long sleeve','shirts','short sleeve','sweat shirts','boots','dress shoes','running shoes','sandal','slip on','sneakers','blazer','blouson','cardigan','coat','field jumper','fleece','leather jacket','mustang','padding','trucker','vest','jean','shorts','sweat pants','trouser','wide jean','wide trouser']
    keys = []
    for j in range(0,len(keywords)):
        for i in range(0,len(colors)):
            keys.append(colors[i]+" "+keywords[j])
    sumsave=[]
    data = pd.read_csv('C:\\Users\\lky\\Desktop\\class_clothes.txt',sep='\n', header=None)[0].str.split('\t', expand=True)

    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'boots',path+'dress shoes',path+'running shoes',path+'sandal',path+'slip on',path+'sneakers']
    file_list=[]
    for i in range(len(path_list)):
        list_num=os.listdir(path_list[i])
        for j in range(len(list_num)):
            file_list.append(list_num[j].replace('.png',''))
            file_list.append(list_num[j].replace('.jpg',''))
    my_clothes =file_list
    my_clothesf = my_clothes.copy()
    for i in range(0,len(my_clothes)):
        my_clothesf[i] = my_clothesf[i].replace('0','')
        my_clothesf[i] = my_clothesf[i].replace('1','')
        my_clothesf[i] = my_clothesf[i].replace('2','')
        my_clothesf[i] = my_clothesf[i].replace('3','')
        my_clothesf[i] = my_clothesf[i].replace('4','')
        my_clothesf[i] = my_clothesf[i].replace('5','')
        my_clothesf[i] = my_clothesf[i].replace('6','')
        my_clothesf[i] = my_clothesf[i].replace('7','')
        my_clothesf[i] = my_clothesf[i].replace('8','')
        my_clothesf[i] = my_clothesf[i].replace('9','') ########내 옷장에 숫자 필터

    # my_clothes= [] 로 놔두고 검출된 의상 하나씩 append해서 받기
    answer = [] #추천할 의상 담는 곳
    detected_clothes = cloth # <----------------- 선택된 의상
    dc = detected_clothes.split()
    dc_type = dc[0] 
    dc_color = dc[1]
    if len(dc) ==3:
        dc_color = dc[1] + ' ' + dc[2]
        
    for loop in range(len(keywords)):

        a=[0 for i in range(len(keys))]
        for j in range(0,9) :
            cnt=0


            df = data[data[j].str.contains(dc_type,na=False)]
            df = df[df[j].str.contains(dc_color,na=False)]
        #    print(df[j]) # 선택한 의상이 포함된 코디맵 행/열 검출
            sumc=[[],[],[],[],[],[],[],[]]
            ii = 0

            for i in range(0,9): # i 열 돌리면서 j열이랑 일치확인

                if i==j:
                    continue
                else:

                    df_filter = df[df[i].str.contains(keywords[loop],na=False)]
                    for color in colors:

                        df_filter2 = df_filter[df_filter[i].str.contains(color,na=False)]
                        count = df_filter2[i].count()
                        sumc[ii].append(count)

                ii=ii+1    
            k=[0 for i in range(len(colors))]
            for cc in range(0,len(colors)):
                for c in range(0,8):
                    k[cc] +=sumc[c][cc]

            for h in range(0,len(colors)) :
                a[h]=a[h]+k[h]

        for i in range(0,14):
            sumsave.append(a[i]) #언급된 횟수 계산
    df1 = pd.DataFrame(keys, index=sumsave, columns=['name'])
    df2 = df1.sort_index(ascending=False) #나온 횟수대로 내림차순 정렬.

    for i in range(0,len(df2.values)):
        if df2.index[i]!=0: #언급횟수 0회 제외시키기
            #print(df2.values[i], df2.index[i])
            for j in range(0,len(my_clothes)):
                if df2.values[i] == my_clothesf[j]:
                    if df2.values[i] != detected_clothes:   
                        answer.append(my_clothes[j])

    if answer == []:
        print('추천할 의상이 없습니다')
    else :
        return answer# <-------------- 의상 추천, 이 결과값을 토대로 실제로 입은것처럼 구현
    
    
def find_outer_path(outer):
    var=[]
    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'blazer',path+'cardigan',path+'vest',path+'coat',path+'field jumper',path+'fleece',path+'leather jacket',path+'mustang',path+'padding',path+'trucker']
    for j in range(len(outer)):
        for a in range(len(path_list)):
            list_num=os.listdir(path_list[a])
            for i in range(len(list_num)):
                if outer[j] in list_num[i]:
                    var.append(path_list[a]+'\\'+list_num[i])
    return var

def find_top_path(top):
    var=[]
    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'dress',path+'hoody',path+'knit',path+'long sleeve',path+'shirts',path+'short sleeve',path+'sweat shirts',path+'blouson']
    for j in range(len(top)):
        for a in range(len(path_list)):
            list_num=os.listdir(path_list[a])
            for i in range(len(list_num)):
                if top[j] in list_num[i]:
                    var.append(path_list[a]+'\\'+list_num[i])
    return var

def find_bottom_path(bottom):
    var=[]
    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'jean',path+'shorts',path+'sweat pants',path+'trouser',path+'wide jean',path+'wide trouser']
    for j in range(len(bottom)):
        for a in range(len(path_list)):
            list_num=os.listdir(path_list[a])
            for i in range(len(list_num)):
                if bottom[j] in list_num[i]:
                    var.append(path_list[a]+'\\'+list_num[i])
    return var

def find_shoes_path(shoes):
    var=[]
    path='C:\\Users\\lky\\DeepLearning\\smart_closet\\img_lib\\cut_img\\'
    path_list=[path+'boots',path+'dress shoes',path+'running shoes',path+'sandal',path+'slip on',path+'sneakers']
    for j in range(len(shoes)):
        for a in range(len(path_list)):
            list_num=os.listdir(path_list[a])
            for i in range(len(list_num)):
                if shoes[j] in list_num[i]:
                    var.append(path_list[a]+'\\'+list_num[i])
    return var