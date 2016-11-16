# QComboBox 下拉列表框
# 允许用户从列表中选择一个列表项
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # QLabel
        self.lbl = QLabel("Ubuntu", self)
        # QComboBox
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)
        # 一旦被选中，会调用 onActivated方法
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()


    def onActivated(self, text):
        # 显示文字
        self.lbl.setText(text)
        # 调整大小
        self.lbl.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())