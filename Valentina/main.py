import os
import sys
import webbrowser
import pygame as game
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation, QThread, QUrl, Qt, pyqtProperty
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from VTranslate import Ui_VTranslate, transla, photo_translate
from Valentina import UiValentina as Val
from Valentina_web import Ui_VBrowser
import speech_recognition as sr

game.init()


class Worker(QThread):
    def run(self):
        game.mixer.music.load('Audio/Hi.mp3')
        game.mixer.music.play()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.record(source, duration=5)
        try:
            text = r.recognize_google(audio, language="ru-RU").upper()
            if text == "НАЙДИ В ЯНДЕКСЕ":
                game.mixer.music.load('Audio/Hi.mp3')
                game.mixer.music.play()
                with sr.Microphone() as source:
                    audio = r.record(source, duration=5)
                    text = r.recognize_google(audio, language="ru-RU")
                    webbrowser.open(f"https://www.yandex.ru/search/?text={text}")
            elif text == "ВЫКЛЮЧИ КОМПЬЮТЕР":
                os.system("shutdown /p /f")
        except sr.UnknownValueError:
            print("Команда не распознана, попробуйте еще раз")
        except sr.RequestError as e:
            print(f"Ошибка в распознавании: {e}")
        self.thread1 = Worker1()
        self.thread1.start()


class Worker1(QThread):
    def run(self):
        while True:
            text = None
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.record(source, duration=5)
            try:
                text = r.recognize_google(audio, language="ru-RU").upper()
                if text == "ВАЛЕНТИНА":
                    self.thread0 = Worker()
                    self.thread0.start()
                    exit()
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue


class VBrowser(QtWidgets.QMainWindow, Ui_VBrowser):
    def __init__(self):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)

        self.setWindowTitle("VBrowser")

        self.back_btn.setFixedSize(25, 25)
        self.forward_btn.setFixedSize(25, 25)
        self.refresh_btn.setFixedSize(25, 25)
        self.home_btn.setFixedSize(25, 25)
        self.url_area.setMinimumHeight(25)

        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.back_btn, 0, 0, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.forward_btn, 0, 1, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.refresh_btn, 0, 2, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.home_btn, 0, 3, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.url_area, 0, 4)
        self.layout.addWidget(self.web, 1, 0, 1, 5)

        self.web.load(QUrl("https://google.com"))

        self.home_btn.pressed.connect(self.get_url)

    def get_url(self):
        if "https://" not in self.url_area.text() or "http://" not in self.url_area.text():
            a = "https://" + self.url_area.text()
            self.web.load(QUrl(f"{a}"))


class VTranslate_GUI(QMainWindow, Ui_VTranslate):
    def __init__(self, parent=None):
        super(VTranslate_GUI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.pushButton.pressed.connect(self.input_text)
        self.pushButton1.pressed.connect(self.close)
        self.pushButton2.pressed.connect(self.clear_c)
        self.pushButton3.pressed.connect(self.size_down)
        self.pushButton4.pressed.connect(self.size_up)
        self.pushButton5.pressed.connect(self.photo_trans)

    def input_text(self):
        text = transla(f"{self.one_Edit.toPlainText()}", f"{self.label_1.text()}", f"{self.label_2.text()}")
        self.one_Edit_2.setText(f"{text}")

    def clear_c(self):
        self.one_Edit_2.setText("")
        self.one_Edit.setText("")

    def font_size(self):
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(int(self.label_22.text()))
        self.one_Edit_2.setFont(font)
        self.one_Edit.setFont(font)

    def size_up(self):
        a = int(self.label_22.text()) + 1
        self.label_22.setText(f"{a}")
        self.font_size()

    def size_down(self):
        a = int(self.label_22.text())
        if a - 1 != 0:
            a -= 1
        self.label_22.setText(f"{a}")
        self.font_size()

    def photo_trans(self):
        dir_ = QtWidgets.QFileDialog.getOpenFileName(None, 'Выбрать фото:', 'C:\\')
        if dir_[0].endswith("jpg") or dir_[0].endswith("png") or dir_[0].endswith("jpeg"):
            text = photo_translate(f"{dir_[0]}")
            text = text.split()
            self.one_Edit.setText(' '.join(text))
            self.input_text()


class Valentina_main(QtWidgets.QMainWindow, Val):
    def __init__(self, parent=None):
        super(Valentina_main, self).__init__(parent)
        self.thread = None
        game.mixer.music.load('Audio/Hi.mp3')
        game.mixer.music.play()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setWindowTitle("Valentina")
        self.setWindowIcon(QIcon('img/Valentina.ico'))
        # self.setGeometry(1600, 600, 249, 400)
        self.setGeometry(0, 0, 249, 400)  # 0, 0, 249, 400
        self.setWindowOpacity(0.0)

        # Создаем анимацию появления окна
        # self.animation1 = QPropertyAnimation(self, b"geometry")
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(0.9)
        self.animation.finished.connect(self.show)
        self.animation.start()

        self.push_add.pressed.connect(self.slide_down_up)
        self.logik_slide = 0
        self.logic_help = 0

        self.thread1 = Worker1()
        self.thread1.start()

        self.but3()
        self.function()

        self.timer = QtCore.QTimer() #
        self.timer2 = QtCore.QTimer()
        self.pereliv1()

        self.center()

    def slide_down_up(self):
        self.anim = QPropertyAnimation(self.groupBox, b"pos")
        self.anim_mic = QPropertyAnimation(self.button_mic, b"pos")

        self.anim_mic.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.anim_mic.setDuration(1000)

        self.anim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.anim.setDuration(1000)
        if self.logik_slide == 0:
            self.anim_mic.setEndValue(QtCore.QPoint(70, 150)) # 70, 70
            self.anim_mic.start()

            self.anim.setEndValue(QtCore.QPoint(0, 380))
            self.anim.start()
            self.logik_slide = 1
        else:
            self.anim_mic.setEndValue(QtCore.QPoint(70, 70))  # 70, 70
            self.anim_mic.start()

            self.anim.setEndValue(QtCore.QPoint(0, 240))
            self.anim.start()
            self.logik_slide = 0

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x = screen.width() - size.width() - 70
        y = screen.height() - size.height() - 70
        self.move(x, y)

    def but3(self):
        self.pushButton_3.setArrowType(Qt.NoArrow)
        self.pushButton_3.setStyleSheet(
            "QToolButton {background-color: rgba(50, 50, 50, 150);\n"
            "color:white;\n"
            "border: none;\n"
            "margin: 0px;\n"
            "padding: 0px;}\n"
            "QToolButton::menu-indicator { image: none; }"
            "QToolButton:hover {background : rgba(50, 50, 50, 200);}"
            "QToolButton:pressed"
            "{background-color: rgba(50, 50, 50, 250);}"
        )
        menu = QtWidgets.QMenu()
        menu.addAction("VBrowser", self.valentinaW)  # БРАУЗЕР
        menu.addAction("VTranslate", self.valTrans)  # ПЕРЕВОДЧИК
        menu.addAction("VMessenger")                 # МЕСЕНДЖЕР
        menu.addAction("VRecorder")                  # ЗАПИСЬ ЭКРАНА ВИДЕО\АУДИО
        menu.addAction("VCalculator")                # КАЛЬКУЛЯТОР
        menu.addAction("VTimer")                     # СЕКУНДОМЕР\ТАЙМЕР
        menu.addAction("VMap")                       # КАРТЫ
        menu.addAction("VChat")                      # ЧАТ ГПТ
        menu.addAction("VGame")                      # ИГРЫ
        menu.addAction("VMedia")                     # МЕДИАПЛЕЕР MP3/4
        menu.addAction("Check Update")               # ОБНОВЛЕНИЯ
        menu.addAction("Help", self.help_now)        # ПОМОЩЬ\СПРАВКА
        menu.addAction("Exit", self.exit_now)        # ВЫХОД
        menu.setStyleSheet("QMenu { font-family:Arial Black;\n\
        color: white; background-color: rgba(50, 50, 50, 150);}\n\
        QMenu::item:selected { background-color: rgba(50, 50, 50, 200); }")
        self.pushButton_3.setMenu(menu)

    def function(self):
        self.thread = Worker()
        self.button_mic.clicked.connect(lambda: self.thread.start())
        self.button_mic.clicked.connect(lambda: self.thread1.exit())
        self.pushButton_2.clicked.connect(lambda: self.showMinimized())

    def valTrans(self):
        self.trans = VTranslate_GUI()
        self.trans.show()

    def help_now(self):
        size = self.geometry()
        self.anim_help = QPropertyAnimation(self, b"geometry")
        self.anim_help.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.anim_help.setDuration(1000)
        if self.logic_help == 0:
            self.anim_help.setStartValue(QtCore.QRect(size.x(), size.y(), 249, 400))
            self.anim_help.setEndValue(QtCore.QRect(size.x() - 249, size.y(), 498, 400))
            self.anim_help.start()
            self.logic_help = 1
        else:
            self.anim_help.setStartValue(QtCore.QRect(size.x(), size.y(), 498, 400))
            self.anim_help.setEndValue(QtCore.QRect(size.x() + 249, size.y(), 249, 400))
            self.anim_help.start()
            self.logic_help = 0

        # global mass_call
        # mass_call = f"{f'{self.geometry()}'[19:-1].replace(',', '')}".split()

    def exit_now(self):
        sys.exit(app.exec_())

    def valentinaW(self):
        self.web = VBrowser()
        self.web.show()

    def mousePressEvent(self, event):

        if event.button() == QtCore.Qt.LeftButton:

            x_main = window.geometry().x()
            y_main = window.geometry().y()

            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()

            if x_main <= cursor_x <= x_main + window.geometry().width():
                if y_main <= cursor_y <= y_main + window.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def set_color(self, col):
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:1\n"
                           f"rgba({col.red()}, {col.green()}, {col.blue()}, 255),\n"
                           "stop:0.427447 rgba(41, 61, 150, 235),\n"
                           f"stop:1 rgba({col.red() + 89}, {col.green() + 80}, {col.blue() - 30}, 255));\n"
                           )

    color = pyqtProperty(QColor, fset=set_color)

    def pereliv1(self):
        self.timer.start(10000)
        self.timer.timeout.connect(self.pereliv2)
        self.timer2.stop()
        self.animation0 = QPropertyAnimation(self, b'color')
        self.animation0.setDuration(10000)
        self.animation0.setStartValue(QColor(81, 0, 200))
        self.animation0.setEndValue(QColor(0, 150, 150))
        self.animation0.setLoopCount(1)
        self.animation0.start()

    def pereliv2(self):
        self.timer2.start(10000)
        self.timer2.timeout.connect(self.pereliv1)
        self.timer.stop()
        self.animation1 = QPropertyAnimation(self, b'color')
        self.animation1.setDuration(10000)
        self.animation1.setStartValue(QColor(0, 150, 150))
        self.animation1.setEndValue(QColor(81, 0, 200))
        self.animation1.setLoopCount(1)
        self.animation1.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Valentina_main()
    app.setWindowIcon(QtGui.QIcon('img/Valentina.ico'))
    window.show()
    sys.exit(app.exec_())
