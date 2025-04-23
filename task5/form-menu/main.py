import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox, QMenuBar, QAction)
from PyQt5.QtCore import Qt


class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простое приложение")
        self.setGeometry(100, 100, 400, 300)
        
        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Основной layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Создаем меню
        self.create_menu()
        
        # Добавляем элементы интерфейса
        self.label = QLabel("Введите число и нажмите кнопку:")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите число здесь...")
        layout.addWidget(self.input_field)
        
        self.button = QPushButton("Вычислить квадрат числа")
        self.button.clicked.connect(self.calculate_square)
        layout.addWidget(self.button)
        
        self.result_label = QLabel("Результат появится здесь")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
        
        # Добавляем растягивающий элемент для выравнивания элементов вверху
        layout.addStretch()
    
    def create_menu(self):
        menubar = self.menuBar()
        
        # Меню "Файл"
        file_menu = menubar.addMenu("Файл")
        
        exit_action = QAction("Выход", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Меню "Помощь"
        help_menu = menubar.addMenu("Помощь")
        
        about_action = QAction("О программе", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def calculate_square(self):
        try:
            # Получаем текст из поля ввода
            input_text = self.input_field.text()
            
            # Проверяем, что поле не пустое
            if not input_text:
                raise ValueError("Поле ввода не должно быть пустым")
            
            # Пробуем преобразовать в число
            number = float(input_text)
            
            # Вычисляем квадрат
            result = number ** 2
            
            # Показываем результат
            self.result_label.setText(f"Квадрат числа {number} равен {result:.2f}")
            
        except ValueError as e:
            # Обрабатываем ошибки преобразования или пустое поле
            self.show_error_message(str(e))
            self.input_field.clear()
            self.result_label.setText("Ошибка ввода")
    
    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Ошибка")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def show_about(self):
        about_text = """
        <b>Простое приложение</b><br><br>
        Это пример простого Windows-приложения на PyQt5.<br>
        Введите число, и программа вычислит его квадрат.<br><br>
        Версия 1.0
        """
        QMessageBox.about(self, "О программе", about_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Устанавливаем стиль для более современного вида
    app.setStyle('Fusion')
    
    window = SimpleApp()
    window.show()
    
    sys.exit(app.exec_())