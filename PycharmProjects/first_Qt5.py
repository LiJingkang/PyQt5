import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))  #字体设置
        self.setToolTip('This is a <b>QWidget</b> widget') #调用父级方法，窗口的显示文本设置

        btn = QPushButton('Botton', self)   #创建一个按钮
        btn.setToolTip('This is a <b>QPushButton</b> widget') #按钮的显示文本
        btn.resize(btn.sizeHint()) #设置按钮推荐大小
        btn.move(50, 50) #按钮在窗口的位置

        self.setGeometry(300, 300, 300, 200) #窗口的位置和大小
        self.setWindowTitle('Tooltips')  #窗口的名称
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.initUI()
    sys.exit(app.exec_())