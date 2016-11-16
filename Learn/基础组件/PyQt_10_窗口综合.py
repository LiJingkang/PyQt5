import sys
from  PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 这是一个文本框
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)  # 设置为中心组件

        exitAction = QAction(QIcon('eixt.bmp'), 'Exit', self)
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Main Window')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())