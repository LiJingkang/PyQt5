import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # QPushButton
        btn1 = QPushButton('Button-1', self)  #创建按钮
        btn1.move(30, 50)  #定位X,Y

        btn2 = QPushButton('Button-2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked) #鼠标点击出发函数
        btn2.clicked.connect(self.buttonClicked)

        # 状态栏
        self.statusBar() #状态栏添加

        # 大小
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

        # 点击函数  点击后触发 self 函数
    def buttonClicked(self):  #被出发的函数，触发后执行该函数
        sender = self.sender()  #创建sender对象
        # 调用sender()方法判断发送信号的信号源是哪一个。
        # 然后在应用的状态栏上显示被按下的按钮的标签内容。
        self.statusBar().showMessage(sender.text() + 'was pressed') #状态栏消息传递

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex =Example()
    sys.exit(app.exec_())