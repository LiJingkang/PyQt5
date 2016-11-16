# 分割狂
# 分割框组件让我们通过拖拽分割线来控制子组件的大小。
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QHBoxLayout 布局
        hbox = QHBoxLayout(self)
        # 使用了一个样式框架，为了让框架组件之间的分割线看的明显。
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 创建一个分割框组件
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft) # 添加这个框体
        splitter1.addWidget(topright) # 添加这个框体

        # 创建一个分隔框组件
        splitter2 = QSplitter(Qt.Vertical)
        # 把第一个组件放进去
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())