import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                QSizePolicy, QLabel, QFontDialog,QApplication) # 用于选择字体的对话框组件

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lb1 = QLabel("Knowledge only matters", self)
        self.lb1.move(130, 20)

        vbox.addWidget(self.lb1)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font Dialog')
        self.show()

    def showDialog(self):
        # getFont()方法返回字体名字和布尔值
        font, ok = QFontDialog.getFont()
        if ok:
            self.lb1.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())