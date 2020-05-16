import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QLabel, QColorDialog, QApplication
from PyQt5.QtGui import QPixmap, QImage, QColor, QPalette, QPainter

class Ui_ImageProcessingWindow(object):
    clicked_pixel_x = None
    clicked_pixel_y = None
    def setupUi(self, ImageProcessingWindow):
        ImageProcessingWindow.setObjectName("ImageProcessingWindow")
        ImageProcessingWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(ImageProcessingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 800, 640))
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setText("")
        pixmap = QtGui.QPixmap("img/kontrolny3.tiff")
        self.photo.setPixmap(pixmap)
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 620, 800, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(0, 640, 113, 32))
        self.loadButton.setObjectName("loadButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(0, 680, 113, 32))
        self.saveButton.setObjectName("saveButton")
        self.pathLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(10, 730, 780, 16))
        self.pathLabel.setObjectName("pathLabel")
        self.someLabel = QtWidgets.QLabel(self.centralwidget)
        self.someLabel.setGeometry(QtCore.QRect(150, 645, 71, 16))
        self.someLabel.setObjectName("someLabel")
        self.pixelPhoto = QtWidgets.QLabel(self.centralwidget)
        self.pixelPhoto.setGeometry(QtCore.QRect(290, 670, 80, 60))
        self.pixelPhoto.setObjectName("pixelPhoto")
        self.valueButton = QtWidgets.QPushButton(self.centralwidget)
        self.valueButton.setGeometry(QtCore.QRect(150, 680, 113, 32))
        self.valueButton.setObjectName("valueButton")
        ImageProcessingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageProcessingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        ImageProcessingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageProcessingWindow)
        self.statusbar.setObjectName("statusbar")
        ImageProcessingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageProcessingWindow)
        QtCore.QMetaObject.connectSlotsByName(ImageProcessingWindow)


        # click events
        self.loadButton.clicked.connect(self.open_dialog_box)
        self.saveButton.clicked.connect(self.save_dialog_box)
        self.valueButton.clicked.connect(self.essa_function)

    def retranslateUi(self, ImageProcessingWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageProcessingWindow.setWindowTitle(_translate("ImageProcessingWindow", "Image Processing"))
        self.loadButton.setText(_translate("ImageProcessingWindow", "Choose File"))
        self.saveButton.setText(_translate("ImageProcessingWindow", "Save File"))
        self.pathLabel.setText(_translate("ImageProcessingWindow", "img/kontrolny3.tiff"))
        self.someLabel.setText(_translate("ImageProcessingWindow", "SOME TEXT:"))
        self.valueButton.setText(_translate("ImageProcessingWindow", "ESSA"))

    def essa_function(self):
        print("essunia")
        
    def show_color_dialog(self):
        selected_color = QColorDialog.getColor()
        if selected_color.isValid():
            self.pixelPhoto.setStyleSheet("QLabel { background-color: %s}" % selected_color.name())

    def open_dialog_box(self):
        filter = "AllFiles (*.jpg *jpeg *.gif *.png *.bmp *.tiff *tif);;JPEG (*.jpg *jpeg);;GIF (*.gif);;PNG(*.png);;BMP (*.bmp);; TIF (*.tiff *.tif)"
        file = QFileDialog.getOpenFileName(filter=filter)
        filepath = file[0]
        pixmap = QPixmap(filepath)
        self.photo.setPixmap(pixmap)
        self.pathLabel.setText(filepath)

    def save_dialog_box(self):
        filter = "JPG (*.jpg);;JPEG (*jpeg);;GIF (*.gif);;PNG(*.png);;BMP (*.bmp);; TIF (*.tif);; TIFF(*.tiff)"
        filename = QFileDialog.getSaveFileName(caption = "Save Image", directory = os.curdir, filter=filter)
        print(filename)
        pixmap = self.photo.pixmap()
        result = pixmap.save(filename[0])
        print(result)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageProcessingWindow = QtWidgets.QMainWindow()
    ui = Ui_ImageProcessingWindow()
    ui.setupUi(ImageProcessingWindow)
    ImageProcessingWindow.show()
    sys.exit(app.exec_())
