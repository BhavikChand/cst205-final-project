#Author: Michael Conley
#Class: CST 205
#Date: 12/4/2023
#Description: Creates a window that takes indexes, an xy coordinate, sizes for both images, cropping for all sides of both images, edge blending style and strength, aorner style, and manipulation choice, then places the second image on the first according to the information given.
import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QPushButton)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap
from src.image_retrieval import get_image_url
from src.placeimage import place_image,resize

from PIL import Image

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()

        self.bg_le_lbl = QLabel('Enter background image ID Number:')
        self.my_bg_le = QLineEdit("")
        self.my_bg_le.minimum_width = 250
        
        self.s_le_lbl = QLabel('Enter subject image ID Number:')
        self.my_s_le = QLineEdit("")
        self.my_s_le.minimum_width = 250

        self.x_le_lbl = QLabel('Enter subject image x coordinate (0 for left, -1 for center, -2 for right):')
        self.my_x_le = QLineEdit("0")
        self.my_x_le.minimum_width = 250

        self.y_le_lbl = QLabel('Enter subject image y coordinate (0 for top, -1 for center, -2 for bottom):')
        self.my_y_le = QLineEdit("0")
        self.my_y_le.minimum_width = 250
        #The image will be placed with the top left corner on the given pixel

        self.my_list = ["None", "Sepia", "Negative", "Grayscale", "Chromatic Abberation"]

        self.bg_cb_lbl = QLabel('Select background manipulation:')
        self.my_bg_combo_box = QComboBox()
        self.my_bg_combo_box.add_items(self.my_list)

        self.s_cb_lbl = QLabel('Select subject manipulation:')
        self.my_s_combo_box = QComboBox()
        self.my_s_combo_box.add_items(self.my_list)

        self.bg_w_le_lbl = QLabel('Enter background width (0 for default):')
        self.my_bg_w_le = QLineEdit("0")
        self.my_bg_w_le.minimum_width = 250
        
        self.bg_h_le_lbl = QLabel('Enter background height (0 for default):')
        self.my_bg_h_le = QLineEdit("0")
        self.my_bg_h_le.minimum_width = 250

        self.s_w_le_lbl = QLabel('Enter subject width (0 for default):')
        self.my_s_w_le = QLineEdit("0")
        self.my_s_w_le.minimum_width = 250
        
        self.s_h_le_lbl = QLabel('Enter subject height (0 for default):')
        self.my_s_h_le = QLineEdit("0")
        self.my_s_h_le.minimum_width = 250
        #negative sizes will mean the image will be flipped

        self.blend_list = ["Linear","Outward","Inward","Wave"]

        self.blend_cb_lbl = QLabel('Enter edge blend type: ')
        self.my_blend_combo_box = QComboBox()
        self.my_blend_combo_box.add_items(self.blend_list)

        self.b_s_le_lbl = QLabel('Enter edge blend strength:')
        self.my_b_s_le = QLineEdit("0")
        self.my_b_s_le.minimum_width = 250

        self.corner_list = ["Sharp","Rounded","Diagonal"]

        self.c_s_le_lbl = QLabel('Enter corner style:')
        self.my_corner_combo_box = QComboBox()
        self.my_corner_combo_box.add_items(self.corner_list)

        self.bg_t_c_le_lbl = QLabel('Pixels to crop from top of background:')
        self.my_bg_t_c_le = QLineEdit("0")
        self.my_bg_t_c_le.minimum_width = 250

        self.bg_b_c_le_lbl = QLabel('Pixels to crop from bottom of background:')
        self.my_bg_b_c_le = QLineEdit("0")
        self.my_bg_b_c_le.minimum_width = 250

        self.bg_l_c_le_lbl = QLabel('Pixels to crop from left side of background:')
        self.my_bg_l_c_le = QLineEdit("0")
        self.my_bg_l_c_le.minimum_width = 250

        self.bg_r_c_le_lbl = QLabel('Pixels to crop from right of background:')
        self.my_bg_r_c_le = QLineEdit("0")
        self.my_bg_r_c_le.minimum_width = 250

        self.s_t_c_le_lbl = QLabel('Pixels to crop from top of subject:')
        self.my_s_t_c_le = QLineEdit("0")
        self.my_s_t_c_le.minimum_width = 250

        self.s_b_c_le_lbl = QLabel('Pixels to crop from bottom of subject:')
        self.my_s_b_c_le = QLineEdit("0")
        self.my_s_b_c_le.minimum_width = 250

        self.s_l_c_le_lbl = QLabel('Pixels to crop from left side of subject:')
        self.my_s_l_c_le = QLineEdit("0")
        self.my_s_l_c_le.minimum_width = 250

        self.s_r_c_le_lbl = QLabel('Pixels to crop from right of subject:')
        self.my_s_r_c_le = QLineEdit("0")
        self.my_s_r_c_le.minimum_width = 250
        
        my_btn = QPushButton("Submit")
        my_btn.clicked.connect(self.on_submit)

        hbox = QHBoxLayout()
        bg_box = QVBoxLayout()
        s_box = QVBoxLayout()





        bg_btn = QPushButton("Preview")
        bg_btn.clicked.connect(self.preview_bg)
        s_btn = QPushButton("Preview")
        s_btn.clicked.connect(self.preview_subject)
        
        

        


        bg_box.add_widget(self.bg_le_lbl)
        bg_box.add_widget(self.my_bg_le)
        bg_box.add_widget(bg_btn)
        s_box.add_widget(self.s_le_lbl)
        s_box.add_widget(self.my_s_le)
        s_box.add_widget(s_btn)
        vbox.add_widget(self.x_le_lbl)
        vbox.add_widget(self.my_x_le)
        vbox.add_widget(self.y_le_lbl)
        vbox.add_widget(self.my_y_le)
        bg_box.add_widget(self.bg_cb_lbl)
        bg_box.add_widget(self.my_bg_combo_box)
        s_box.add_widget(self.s_cb_lbl)
        s_box.add_widget(self.my_s_combo_box)
        bg_box.add_widget(self.bg_w_le_lbl)
        bg_box.add_widget(self.my_bg_w_le)
        bg_box.add_widget(self.bg_h_le_lbl)
        bg_box.add_widget(self.my_bg_h_le)
        s_box.add_widget(self.s_w_le_lbl)
        s_box.add_widget(self.my_s_w_le)
        s_box.add_widget(self.s_h_le_lbl)
        s_box.add_widget(self.my_s_h_le)
        vbox.add_widget(self.blend_cb_lbl)
        vbox.add_widget(self.my_blend_combo_box)
        vbox.add_widget(self.b_s_le_lbl)
        vbox.add_widget(self.my_b_s_le)
        vbox.add_widget(self.c_s_le_lbl)
        vbox.add_widget(self.my_corner_combo_box)
        bg_box.add_widget(self.bg_t_c_le_lbl)
        bg_box.add_widget(self.my_bg_t_c_le)
        bg_box.add_widget(self.bg_b_c_le_lbl)
        bg_box.add_widget(self.my_bg_b_c_le)
        bg_box.add_widget(self.bg_l_c_le_lbl)
        bg_box.add_widget(self.my_bg_l_c_le)
        bg_box.add_widget(self.bg_r_c_le_lbl)
        bg_box.add_widget(self.my_bg_r_c_le)
        s_box.add_widget(self.s_t_c_le_lbl)
        s_box.add_widget(self.my_s_t_c_le)
        s_box.add_widget(self.s_b_c_le_lbl)
        s_box.add_widget(self.my_s_b_c_le)
        s_box.add_widget(self.s_l_c_le_lbl)
        s_box.add_widget(self.my_s_l_c_le)
        s_box.add_widget(self.s_r_c_le_lbl)
        s_box.add_widget(self.my_s_r_c_le)



        hbox.add_layout(bg_box)
        hbox.add_layout(s_box)
        vbox.add_layout(hbox)
        vbox.add_widget(my_btn)

        self.set_layout(vbox)

        self.show()
    
    

    @Slot()
    def preview_bg(self):
        im = get_image_url(int(self.my_bg_le.text))
        im = im.convert("RGB")
        im.save("finalimages/preview.jpg")
        pw = PreviewWindow()
        
    @Slot()
    def preview_subject(self):
        im = get_image_url(int(self.my_s_le.text))
        im = im.convert("RGB")
        im.save("finalimages/preview.jpg")
        pw = PreviewWindow()

    @Slot()
    def on_submit(self):
        bg = get_image_url(int(self.my_bg_le.text))
        subject = get_image_url(int(self.my_s_le.text))
        bg_manip = self.my_bg_combo_box.current_text
        s_manip = self.my_s_combo_box.current_text
        x_pos = int(self.my_x_le.text)
        y_pos = int(self.my_y_le.text)
        bg_w = int(self.my_bg_w_le.text)
        bg_h = int(self.my_bg_h_le.text)
        s_w = int(self.my_s_w_le.text)
        s_h = int(self.my_s_h_le.text)
        blend_style = self.my_blend_combo_box.current_text
        blend_strength = int(self.my_b_s_le.text)
        corner = self.my_corner_combo_box.current_text
        bg_t = int(self.my_bg_t_c_le.text)
        bg_b = int(self.my_bg_b_c_le.text)
        bg_l = int(self.my_bg_l_c_le.text)
        bg_r = int(self.my_bg_r_c_le.text)
        s_t = int(self.my_s_t_c_le.text)
        s_b = int(self.my_s_b_c_le.text)
        s_l = int(self.my_s_l_c_le.text)
        s_r = int(self.my_s_r_c_le.text)
        place_image(bg,subject,bg_manip,s_manip,x_pos,y_pos,bg_w,bg_h,s_w,s_h,blend_style,blend_strength,corner,bg_t,bg_b,bg_l,bg_r,s_t,s_b,s_l,s_r)
        rw = ResultWindow()


        
class PreviewWindow(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel()
        my_pixmap = QPixmap('finalimages/preview.jpg')
        label.pixmap = my_pixmap
        self.layout = QVBoxLayout()
        self.layout.add_widget(label)
        self.set_layout(self.layout)
        self.show()



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