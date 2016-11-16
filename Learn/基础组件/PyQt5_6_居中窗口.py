import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()
    def center(self):
        qr = self.frameGeometry()  # 获得主窗口的一个矩形特定几何图形
        cp = QDesktopWidget().availableGeometry().center() # 算出相对于显示器的绝对值。 并且获得屏幕中心点
        qr.moveCenter(cp) # 设定好了宽高  诺到中心点去
        self.move(qr.topLeft()) #应用窗口的左上方的点到qr矩形的左上方的点
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.initUI()
    ex.center()
    sys.exit(app.exec_())