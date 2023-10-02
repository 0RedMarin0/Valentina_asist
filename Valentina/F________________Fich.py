import sys
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *

class myListWidget(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet("""
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:3px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
    """)

    def Clicked(self,item):
        QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())

def main():
    app = QApplication(sys.argv)

    listWidget = myListWidget()
    listWidget.resize(300, 120)

    labels = ("Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7",
              "Item 8", "Item 9", "Item 10", "Item 11", "Item 12",   )
    listWidget.addItems(labels)

    listWidget.setWindowTitle('PyQT QListwidget Demo')
    listWidget.itemClicked.connect(listWidget.Clicked)
    listWidget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()