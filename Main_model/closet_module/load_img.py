def loadImageFromFile(path,num) :
    img_list=os.listdir(path)
    
    #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
    self.qPixmapFileVar = QPixmap()
    self.qPixmapFileVar.load(path+'\\'+img_list[num])
    self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(500)
    self.lbl_picture.setPixmap(self.qPixmapFileVar)