import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My App')
        self.setGeometry(0, 0, 400, 1300)  # Устанавливаем размер окна

        self.center()  # Центрируем окно на экране


        print(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())