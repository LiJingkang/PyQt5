# QLineEdit 单行文本编辑框 允许输入单行的 纯文本数据
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QLabel
        self.lbl = QLabel('Zetcode', self)
        # QLineEdit 单行文本编辑框
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        # 如果单行文本编辑框内的文本被改变，调用 这个方法。
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        # 调用这个方法来调整标签显示相对文本的长度
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())