from PyQt5.QtCore import QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QWidget, QPushButton, QGroupBox, QListWidget, QToolButton, QTextBrowser, QApplication, \
    QMainWindow


class UiValentina(object):
    def setupUi(self, Valentina):
        Valentina.setObjectName("Valentina")
        Valentina.resize(250, 400)
        font = QFont()
        font.setFamily("Arial Black")
        Valentina.setFont(font)
        Valentina.setAutoFillBackground(False)
        Valentina.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0\n"
"rgba(81, 0, 200, 255), stop:0.427447 rgba(41, 61, 150, 235), stop:1 rgba(170, 79, 165, 255));\n"
"font-family:Arial Black;")
        self.centralwidget = QWidget(Valentina)
        self.centralwidget.setObjectName("centralwidget")
        self.button_mic = QPushButton(self.centralwidget)
        self.button_mic.setGeometry(QRect(70, 70, 110, 110))
        self.button_mic.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_mic.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 20);image: url(img/mic22.png);\n"
"    border-radius: 55;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"effect.setOffset(0, 0)\n"
"effect.setBlurRadius(20)\n"
"effect.setColor(QColor(57, 219, 255))\n"
" QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.button_mic.setText("")
        self.button_mic.setObjectName("button_mic")

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QRect(0, 240, 250, 161))
        self.groupBox.setStyleSheet("background-color: rgba(0, 0, 0, 0);border: none;")
        self.groupBox.setObjectName("groupBox")

        self.comand_list = QListWidget(self.groupBox)
        self.comand_list.setGeometry(QRect(0, 20, 251, 141))  # 0, 260, 251, 141
        self.comand_list.setStyleSheet("""
QListWidget 
{
background-color: rgba(30, 30, 30, 200);
border: none;
margin: 0px;
padding: 0px; color:white;
}
QListView::item:hover {background : rgba(255, 255, 255, 0.1);}
QListView::item:selected {background : rgba(255, 255, 255, 0.2);}
"""
)
        self.comand_list.setObjectName("comand_list")

        self.push_add = QPushButton(self.groupBox)
        self.push_add.setGeometry(QRect(0, 0, 110, 20))  # 0, 240, 110, 20
        font = QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.push_add.setFont(font)
        self.push_add.setStyleSheet(
"QPushButton {"
"background-color: rgba(50, 50, 50, 150);\n"
"color:white;\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;}\n"
"QPushButton:hover {background : rgba(50, 50, 50, 200);}")
        self.push_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.push_add.setObjectName("push_add")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QRect(139, 0, 110, 20))  # 139, 240, 110, 20
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
"QPushButton {"
"background-color: rgba(50, 50, 50, 150);\n"
"color:white;\n"
"border: none;\n"
"margin: 0px;\n"
"padding: 0px;}\n"
"QPushButton:hover {background : rgba(50, 50, 50, 200);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3 = QToolButton(self.groupBox)
        self.pushButton_3.setGeometry(QRect(110, 0, 29, 20))  # 110, 240, 29, 20
        font = QFont()
        font.setFamily("Arial Black")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setPopupMode(QToolButton.InstantPopup)

        self.pushButton_4 = QToolButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(469, 0, 29, 20))  # 110, 240, 29, 20
        font = QFont()
        font.setFamily("Arial Black")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_3")
        self.pushButton_4.setPopupMode(QToolButton.InstantPopup)

        self.help_list = QTextBrowser(self.centralwidget)
        self.help_list.setGeometry(QRect(249, 0, 249, 400))
        font = QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.help_list.setAlignment(Qt.AlignTop)
        self.help_list.setFont(font)
        self.help_list.setStyleSheet("""
            QScrollBar
{
background : lightgreen;
}
QScrollBar::handle
{
background : pink;
}
QScrollBar::handle::pressed
{
background : red;
}
        """)
        self.help_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.help_list.setObjectName("help")

        Valentina.setCentralWidget(self.centralwidget)

        self.retranslateUi(Valentina)
        QMetaObject.connectSlotsByName(Valentina)

        # self.comand_list.setCurrentRow(20)

    def retranslateUi(self, Valentina):
        _translate = QCoreApplication.translate
        Valentina.setWindowTitle(_translate("Valentina", "Valentina"))
        self.push_add.setText(_translate("Valentina", "ПАНЕЛЬ"))
        self.pushButton_2.setText(_translate("Valentina", "СКРЫТЬ"))
        self.pushButton_3.setText(_translate("Valentina", "♦"))
        with open('help.txt', 'r', encoding="UTF=8") as file:
            text = file.read()
            self.help_list.setText(f"{text}")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UiValentina()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
