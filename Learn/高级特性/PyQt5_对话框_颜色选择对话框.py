import  sys
from  PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                              QColorDialog, QApplication) # QColorDialog 用于颜色选择
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 初始化一个颜色
        col = QColor(0, 0, 0)
        # 一个按钮
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)
        # 颜色选择框
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s}"
                               % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        # 弹出一个颜色选择框
        col = QColorDialog.getColor()
        # 如果返回一个有效的颜色值。  改变颜色。 使用样式表来定义背景颜色
        if col.isValid():
            self.frm.setStyleSheet("QWiget { backgroud-color: %s}"
                                   % col.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())