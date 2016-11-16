import  sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):  # 状态栏由QMainWindow组件帮助创建完成
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('这里是状态栏')   # 得到状态栏
        self.setGeometry(300, 300, 250, 150)  #  设置窗口信息
        self.setWindowTitle('StatusBar')  # 设置窗口标题
        self.show()  # 显示窗口

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())