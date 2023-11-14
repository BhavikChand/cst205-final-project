#Author: Michael Conley
#Class: CST 205
#Date: 11/8/2023
#Description: Creates a window that takes 2 file names, an xy coordinate, and blend strengths and manipulations for both images, then places the second image on the first according to the information given.
import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QComboBox, QPushButton)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap


my_app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()

        self.bg_le_lbl = QLabel('Enter background image file name:')
        self.my_bg_le = QLineEdit("")
        self.my_bg_le.minimum_width = 250
        
        self.s_le_lbl = QLabel('Enter subject image file name:')
        self.my_s_le = QLineEdit("")
        self.my_s_le.minimum_width = 250

        self.x_le_lbl = QLabel('Enter subject image x coordinate:')
        self.my_x_le = QLineEdit("")
        self.my_x_le.minimum_width = 250

        self.y_le_lbl = QLabel('Enter subject image y coordinate:')
        self.my_y_le = QLineEdit("")
        self.my_y_le.minimum_width = 250

        self.bg_blend_le_lbl = QLabel('Enter background blend strength:')
        self.my_bg_blend_le = QLineEdit("")
        self.my_bg_blend_le.minimum_width = 250

        self.s_blend_le_lbl = QLabel('Enter subject blend strength:')
        self.my_s_blend_le = QLineEdit("")
        self.my_s_blend_le.minimum_width = 250

        self.bg_cb_lbl = QLabel('Select background manipulation:')
        self.my_list = ["None", "Sepia", "Negative", "Grayscale", "Thumbnail"]
        self.my_bg_combo_box = QComboBox()
        self.my_bg_combo_box.add_items(self.my_list)

        self.s_cb_lbl = QLabel('Select subject manipulation:')
        self.my_s_combo_box = QComboBox()
        self.my_s_combo_box.add_items(self.my_list)

        my_btn = QPushButton("Submit")

        my_btn.clicked.connect(self.on_submit)

        vbox.add_widget(self.bg_le_lbl)
        vbox.add_widget(self.my_bg_le)
        vbox.add_widget(self.s_le_lbl)
        vbox.add_widget(self.my_s_le)
        vbox.add_widget(self.x_le_lbl)
        vbox.add_widget(self.my_x_le)
        vbox.add_widget(self.y_le_lbl)
        vbox.add_widget(self.my_y_le)
        vbox.add_widget(self.bg_blend_le_lbl)
        vbox.add_widget(self.my_bg_blend_le)
        vbox.add_widget(self.s_blend_le_lbl)
        vbox.add_widget(self.my_s_blend_le)
        vbox.add_widget(self.bg_cb_lbl)
        vbox.add_widget(self.my_bg_combo_box)
        vbox.add_widget(self.s_cb_lbl)
        vbox.add_widget(self.my_s_combo_box)

        vbox.add_widget(my_btn)

        self.set_layout(vbox)

        self.show()

    @Slot()
    def on_submit(self):
        bg = "finalimages/"+self.my_bg_le.text
        subject = "finalimages/"+self.my_s_le.text
        bg_manip = self.my_bg_combo_box.current_text
        s_manip = self.my_s_combo_box.current_text
        x = int(self.my_x_le.text)
        y = int(self.my_y_le.text)
        place_image(bg,subject,bg_manip,s_manip,x,y)



class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel()
        my_pixmap = QPixmap('finalimages/result.jpg')
        label.pixmap = my_pixmap
        self.layout = QVBoxLayout()
        self.layout.add_widget(label)
        self.set_layout(self.layout)
        self.show()

def place_image(bg,subject,bg_manip,s_manip,x,y):
    return


        

my_win = MyWindow() 
sys.exit(my_app.exec())
