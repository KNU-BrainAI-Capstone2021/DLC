import pandas as pd

class color:
    def __init__(self,rgb):
        self.df=pd.read_excel('C:\\Users\\lky\\DeepLearning\\smart_closet\\color.xlsx')
        self.rgb=rgb
        
        
    def case(self,cr):
        if cr <= 30:
            return 30
        elif (cr > 30) and (cr <= 60):
            return 60
        elif (cr > 60) and (cr <= 90):
            return 90
        elif (cr > 90) and (cr <= 120):
            return 120
        elif (cr > 120) and (cr <= 150):
            return 150
        elif (cr > 150) and (cr <= 180):
            return 180
        elif (cr > 180) and (cr <= 210):
            return 210
        elif (cr > 210) and (cr <= 240):
            return 240
        else:
            return 255
        
        
    def find_color(self):
        r = self.df['r'] == self.case(self.rgb[0])
        g = self.df['g'] == self.case(self.rgb[1])
        b = self.df['b'] == self.case(self.rgb[2])
        color_df = self.df[r & g & b]
        cr=color_df['color'].iloc[0]
        return cr