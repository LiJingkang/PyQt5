import  sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QPushButton 按钮
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        # QLineEdit 单行编辑框
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        # 设置窗口信息
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input Dialog')
        self.show()

    def showDialog(self):
        # 一个输入对话框  对话框标题，对话框的消息文本  会返回一个布尔值
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        # 扇面的判断，如果成功 显示在 le 的内容里面
        # 在单行编辑框组件上显示
        if ok:
            self.le.setText(str(text))

if  __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())