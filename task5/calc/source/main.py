import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic 
#from PyQt6.QtCore import QLibraryInfo

""" os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = \
    '/Users/mac/Documents/edu/python/task5/.venv/lib/python3.13/site-packages/PyQt5/Qt5/plugins' """

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('/Users/mac/Documents/edu/python/task5/calc/ui/design.ui') 

        self.ui.label.setText('0')
        self.ui.clear.clicked.connect(lambda: self.clear_line())
        self.ui.zero.clicked.connect(lambda: self.add_digits('0'))
        self.ui.one.clicked.connect(lambda: self.add_digits('1'))
        self.ui.two.clicked.connect(lambda: self.add_digits('2'))
        self.ui.tree.clicked.connect(lambda: self.add_digits('3'))
        self.ui.four.clicked.connect(lambda: self.add_digits('4'))
        self.ui.five.clicked.connect(lambda: self.add_digits('5'))
        self.ui.six.clicked.connect(lambda: self.add_digits('6'))
        self.ui.seven.clicked.connect(lambda: self.add_digits('7'))
        self.ui.eigth.clicked.connect(lambda: self.add_digits('8'))
        self.ui.nine.clicked.connect(lambda: self.add_digits('9'))
        self.ui.minus.clicked.connect(lambda: self.add_digits('-'))
        self.ui.plus.clicked.connect(lambda: self.add_digits('+'))
        self.ui.rasdel.clicked.connect(lambda: self.add_digits('/'))
        self.ui.res.clicked.connect(lambda: self.get_result())
        self.ui.umnogit.clicked.connect(lambda: self.add_digits('*'))
        
    def clear_line(self) -> None:
        self.ui.lineEdit.setText('0')
        self.ui.label.setText('0')

    def add_digits(self, btn_text: str) -> None:
        if self.ui.lineEdit.text() == '0' or self.ui.lineEdit.text() == 'Err':
            self.ui.lineEdit.setText(btn_text)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn_text)
    
    def get_result(self) -> float:
        try:
            result = eval(self.ui.lineEdit.text())
        except ZeroDivisionError or SyntaxError:
            self.ui.lineEdit.setText('Err')
            return 0
        self.ui.label.setText(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(str(result))
        return result
    

app = QApplication(sys.argv)
ex2 = MyApp()
ex2.ui.show()
ex = MyApp()
ex.ui.show()
sys.exit(app.exec())

