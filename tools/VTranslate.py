"""

translator='bing' - TOP !!!
translator='yandex' - через время (ограниченно по запросам в *минуту
google it's shiiit
alibaba медленный и ошибочный
itranslate медленный, но рабочий, есть просечки

"""
from PyQt5 import QtCore, QtGui, QtWidgets
import translators as ts
from PIL import Image


# def photo_translate(dir_file):
#     img = Image.open(f"{dir_file}")
#     pytes.pytesseract.tesseract_cmd = r"tesseract\tesseract.exe"
#     text = pytes.image_to_string(img, lang='eng')
#     return text


def transla(text, a2='en', a3='ru', a1='bing'):
    if a2 == "Английский":
        a2 = "en"
    else:
        a2 = "ru"
    if a3 == "Русский":
        a3 = "ru"
    else:
        a3 = "en"
    try:
        tx = ts.translate_text(text, translator=a1, from_language=a2, to_language=a3)
        return tx
    except:
        return "Переводчик оказался пид"


class Ui_VTranslate(object):
    def setupUi(self, VTranslate):
        VTranslate.setObjectName("VTranslate")
        VTranslate.resize(820, 420)
        VTranslate.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(VTranslate)
        self.centralwidget.setObjectName("centralwidget")
        self.one_Edit = QtWidgets.QTextEdit(self.centralwidget)
        self.one_Edit.setGeometry(QtCore.QRect(0, 20, 381, 400))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.one_Edit.setFont(font)
        self.one_Edit.setStyleSheet("QTextEdit {background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(255, 215, 0);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}")
        self.one_Edit.setObjectName("one_Edit")
        self.toolButton_one = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_one.setGeometry(QtCore.QRect(350, 0, 31, 20))
        self.toolButton_one.setStyleSheet("border: none;\n"
"background-color: rgb(240, 240, 240);")
        self.toolButton_one.setObjectName("toolButton_one")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 0, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.toolButton_two = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_two.setGeometry(QtCore.QRect(440, 0, 31, 20))
        self.toolButton_two.setStyleSheet("border: none;\n"
"background-color: rgb(240, 240, 240);")
        self.toolButton_two.setObjectName("toolButton_two")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(469, 0, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.one_Edit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.one_Edit_2.setGeometry(QtCore.QRect(439, 20, 381, 400))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.one_Edit_2.setFont(font)
        self.one_Edit_2.setStyleSheet("QTextEdit {background-color: rgba(255, 255, 255);\n"
"border: 3px solid rgb(255, 215, 0);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}")
        self.one_Edit_2.setObjectName("one_Edit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(383, 0, 54, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 215, 0);\n"
"border-radius: 55;color: black")
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(383, 20, 54, 20))
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("background-color: rgb(255, 99, 71);\n"
                                      "border-radius: 55;color: black")
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setText("X")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(383, 40, 54, 20))
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("background-color: rgb(64, 224, 208);\n"
                                       "border-radius: 55;color: black")
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setText("clear")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(383, 60, 15, 20))
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("background-color: rgb(64, 224, 0);\n"
                                       "border-radius: 55;color: black")
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.setText("<")

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(422, 60, 15, 20))
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("background-color: rgb(64, 224, 0);\n"
                                       "border-radius: 55;color: black")
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.setText(">")

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(383, 80, 54, 20))
        self.pushButton5.setFont(font)
        self.pushButton5.setStyleSheet("background-color: rgb(147, 112, 219);\n"
                                       "border-radius: 55;color: black")
        self.pushButton5.setObjectName("pushButton")
        self.pushButton5.setText("фото")

        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(383, 100, 54, 20))
        self.pushButton6.setFont(font)
        self.pushButton6.setStyleSheet("background-color: rgb(240, 230, 140);\n"
                                       "border-radius: 55;color: black")
        self.pushButton6.setObjectName("pushButton")
        self.pushButton6.setText("микрофон")

        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(383, 120, 54, 20))
        self.pushButton7.setFont(font)
        self.pushButton7.setStyleSheet("background-color: rgb(0, 220, 140);\n"
                                       "border-radius: 55;color: black")
        self.pushButton7.setObjectName("pushButton")
        self.pushButton7.setText("голос")

        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(398, 60, 24, 20))
        font.setPointSize(7)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(20, 200, 255);")
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_22.setText("14")

        VTranslate.setCentralWidget(self.centralwidget)

        self.retranslateUi(VTranslate)
        QtCore.QMetaObject.connectSlotsByName(VTranslate)

    def retranslateUi(self, VTranslate):
        _translate = QtCore.QCoreApplication.translate
        VTranslate.setWindowTitle(_translate("VTranslate", "MainWindow"))
        self.one_Edit.setHtml(_translate("VTranslate", "Hello World !!!"))
        self.toolButton_one.setText(_translate("VTranslate", "..."))
        self.label_1.setText(_translate("VTranslate", "Английский"))
        self.toolButton_two.setText(_translate("VTranslate", "..."))
        self.label_2.setText(_translate("VTranslate", "Русский"))
        self.one_Edit_2.setHtml(_translate("VTranslate", ""))
        self.pushButton.setText(_translate("VTranslate", "Перевести"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VTranslate = QtWidgets.QMainWindow()
    ui = Ui_VTranslate()
    ui.setupUi(VTranslate)
    VTranslate.show()
    sys.exit(app.exec_())
