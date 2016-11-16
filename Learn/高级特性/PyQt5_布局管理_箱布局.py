import  sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout,  # 两个布局管理类
                             QApplication) # 主窗口
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建了两个按钮
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 水平 箱布局
        hbox = QHBoxLayout()
        hbox.addStretch(1) # 一个拉伸因子  在两个按钮之间增加了一个可拉伸空间
        hbox.addWidget(okButton) # 两个按钮
        hbox.addWidget(cancelButton)

        # 垂直 箱布局
        vbox = QVBoxLayout()
        vbox.addStretch(1) # 拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边。
        vbox.addLayout(hbox)

        # 设置一下主窗口的布局
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Button')
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())