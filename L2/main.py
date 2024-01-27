from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QListWidget
import os
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ImageProcessor():
    def __init__(self):
        self.dir = None
        self.image = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)
    
    def showImage(self, path):
        lbl_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lbl_image.width(), lbl_image.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
        lbl_image.setPixmap(pixmapimage)
        lbl_image.show()
    
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
    
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_UD(self):
        self.image = self.image.transpose(Image.ROTATE_180)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_Blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_Contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_Emboss(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_EE(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_Detail(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_FE(self):
        self.image = self.image.filter(ImageFilter.FIND_EDGES)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_Smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    


    

app = QApplication([])
win = QWidget()

win.resize(700, 500)
win.setWindowTitle('Easy Editor')



    




btn_dir = QPushButton("Open Folder")
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_bw = QPushButton("B/W")
btn_sharp = QPushButton("Sharp")
btn_flip = QPushButton("Flip")
btn_UD = QPushButton("U/D")
btn_Blur = QPushButton("Blur")
btn_Contour = QPushButton("Contour")
btn_Emboss = QPushButton("Emboss")
btn_EE = QPushButton("E_E")
btn_Detail = QPushButton("Detail")
btn_FE = QPushButton('F_E')
btn_Smooth = QPushButton('Smooth')


lbl_image = QLabel()
lw_files = QListWidget()

row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

row_1.addWidget(btn_left)
row_1.addWidget(btn_right)
row_1.addWidget(btn_sharp)
row_1.addWidget(btn_bw)
row_1.addWidget(btn_flip)
row_1.addWidget(btn_UD)
row_1.addWidget(btn_Blur)
row_1.addWidget(btn_Contour)
row_1.addWidget(btn_Emboss)
row_1.addWidget(btn_EE)
row_1.addWidget(btn_Detail)
row_1.addWidget(btn_FE)
row_1.addWidget(btn_Smooth)




col_1.addWidget(btn_dir)
col_1.addWidget(lw_files)

col_2.addWidget(lbl_image, 95)
col_2.addLayout(row_1)

row_2.addLayout(col_1, 20)
row_2.addLayout(col_2, 80)

win.setLayout(row_2)

win.show()



workdir = ""

def filter(files, extentions):
    result = []
    for filename in files:
        for ext in extentions:
            if filename.endswith(ext):
                result.append(filename)
    return result
    
def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    

def show_filename_list():
    extentions = [".jpg", "p.png", ".jpeg", ".gif", ".bmp"]
    choose_workdir()
    filenames = filter(os.listdir(workdir), extentions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename) 
    
workimage = ImageProcessor()

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)









btn_dir.clicked.connect(show_filename_list)       
lw_files.currentRowChanged.connect(showChosenImage)     
btn_bw.clicked.connect(workimage.do_bw)
btn_right.clicked.connect(workimage.do_right)
btn_left.clicked.connect(workimage.do_left)
btn_sharp.clicked.connect(workimage.do_sharp)
btn_flip.clicked.connect(workimage.do_flip)
btn_UD.clicked.connect(workimage.do_UD)
btn_Blur.clicked.connect(workimage.do_Blur)
btn_Contour.clicked.connect(workimage.do_Contour)
btn_Emboss.clicked.connect(workimage.do_Emboss)
btn_EE.clicked.connect(workimage.do_EE)
btn_Detail.clicked.connect(workimage.do_Detail)
btn_FE.clicked.connect(workimage.do_FE)
btn_Smooth.clicked.connect(workimage.do_Smooth)























app.exec_()








