import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import uic 

""" os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = \
    '/Users/mac/Documents/edu/python/task5/.venv/lib/python3.13/site-packages/PyQt5/Qt5/plugins' """


class Dialog(QDialog):
    def __init__(self, opt: str):
        super().__init__()
        self.ui = uic.loadUi('/Users/mac/Documents/edu/python/task5/text_editor/ui/form.ui', self)
        #self.__path = __file__[:-7] + 'untitled.txt'  # Значение по умолчанию
        self.ui.pushButton.setText(opt)
        self.ui.pushButton.clicked.connect(self.__set_path)  # Лямбда не нужна, если нет аргументов

    def __set_path(self):
        """Вызывается при клике на кнопку, обновляет путь и закрывает диалог."""
        self.__path = self.ui.lineEdit.text()  # Ваша логика выбора пути (например, через QFileDialog)
        self.accept()  # Закрывает диалог с кодом QDialog.Accepted

    def get_path(self) -> str:
        """Возвращает выбранный путь."""
        return self.__path


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('/Users/mac/Documents/edu/python/task5/text_editor/ui/mainWindow.ui')

        self.ui.saveButton.clicked.connect(lambda: self.__save("Save"))
        self.ui.openButton.clicked.connect(lambda: self.__open("Open"))

    def __save(self, opt: str) -> None:
        path = self.__call_dialog(opt)
        if path == '':
            path = __file__[:-7] + 'untitled.txt'
        try:
            try:
                with open(path, 'w') as file:
                    file.write(self.ui.textEdit.toPlainText())
            except FileNotFoundError:
                messange = QMessageBox()
                messange.setText('Ошибка в пути файла')
                messange.exec_()

        except IsADirectoryError:
            messange = QMessageBox()
            messange.setText('Ошибка В пути файла')
            messange.exec_()

    def __call_dialog(self, opt: str) -> str:
        dialog = Dialog(opt)
        dialog.exec_()
        res = dialog.get_path()
        return res
        
    def __open(self, opt: str): 
        path = self.__call_dialog(opt)
        try:
            with open(path, 'r') as file:
                self.ui.textEdit.setText(file.read())
        except FileNotFoundError:
            messange = QMessageBox()
            messange.setText('Файл не найден')
            messange.exec_()



app = QApplication(sys.argv)
ex = Main()
ex.ui.show()
sys.exit(app.exec_())