import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QAction 一个用于菜单栏，工具栏或自定义快捷键的抽象动作行文
        exitAction = QAction(QIcon('exit.png'), "&Exit", self) #创建一个行为对象，添加图片、文本
        exitAction.setShortcut('Ctrl+Q')   #设置快捷方式
        exitAction.setStatusTip('Exit application')  #状态栏提示信息  鼠标悬浮于菜单栏之上时候的状态提示

        # 触发信号发射行为调用QApplication里面的quit()方法
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()  #调用状态栏对象

        # 创建菜单栏对象
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File") #在窗口中添加菜单栏
        fileMenu.addAction(exitAction)  #将创建的行为添加到对应的菜单栏
        #窗口操作
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())