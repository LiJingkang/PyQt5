import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建文本编辑对象
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit) #设置文本编辑的核心组件
        self.statusBar()

        # 创建一个文件打开行为，配置图片路径
        openFile = QAction(QIcon('eixt.bpm'), 'Open', self)
        openFile.setShortcut('Ctrl+O') #快捷方式
        openFile.setStatusTip('Open new File')  #状态提示
        openFile.triggered.connect(self.showDialog) #点击时调用函数

        # 创建菜单对象
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File') #添加文件菜单并命名
        fileMenu.addAction(openFile) #文件菜单添加行为

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '\d:') #获取文件名，路径
        # 选中文件后，读出文件的内容，并设置成文本编辑框组件的显示文本。
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())