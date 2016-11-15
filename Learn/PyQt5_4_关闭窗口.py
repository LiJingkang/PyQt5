import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication # QtCore 对象模块
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        qbtn = QPushButton('Quit', self) # 创建了一个按钮，第一个参数是文本，第二个参数是父类
        qbtn.clicked.connect(QCoreApplication.instance().quit) # 点击事件，调用了这个方法
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.initUI()
    sys.exit(app.exec_())
