import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label_one = QLabel('Zetcode', self) # 创建第一个label
        label_one.move(15, 10)

        label_two = QLabel('tutorials', self) # 创建第二个label
        label_two.move(35, 40)

        label_three = QLabel('programmers', self) # 创建第三个
        label_three.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())