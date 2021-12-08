
import glob

# 0[Empty] + 1 ~ 31
class_name = ['wide trouser','dress','skirt','hoody','knit',
              'long sleeve','shirts','short sleeve','sweat shirt'
              ,'boots','dress shoes',
              'running shoes','sandal','slip on','sneakers'
              ,'blazer','blouson','cardigan','coat'
              ,'field jumper','fleece','leather jacket','mustang'
              ,'padding','trucker','vest','jean'
              ,'shorts','sweat pants','trouser','wide jean'
              ]


output_names = glob.glob('*.txt')




# 2)
 
split_names = []
split_names_to_class = []

for i in range(len(output_names)):
    
    texts = output_names[i][:-7] #blazer, sandle 등으로 바로 나옴
    split_names.append(texts)
    split_names_to_class.append(class_name.index(texts))
    




# 3)

for i in range(len(output_names)):

    with open(output_names[i],'r') as f:
        lines = f.read() # lines = '15 0.502941 0.533824 0.647059 0.832353' (str)        
        lines = lines.split(" ")
        lines[0] = str(split_names_to_class[i])
        lines = ' '.join(lines) #4)

    with open(output_names[i],'w') as f:
        f.write(lines)