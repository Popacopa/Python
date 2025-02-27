from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys 

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      uic.load_ui('./window.py')


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__": main()