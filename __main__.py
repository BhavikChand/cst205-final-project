#Github: https://github.com/BhavikChand/cst205-final-project.git
import sys
from src.final import MyWindow
from PySide6.QtWidgets import QApplication

my_app = QApplication([])
my_win = MyWindow()
sys.exit(my_app.exec())