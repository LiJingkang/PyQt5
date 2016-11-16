import  sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,  # 网格布局类
                             QPushButton, QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid) # 创建子布局
        names = ['Cls', 'Bck', '', 'Close',  # 新建表格
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)] # 双循环放入 positions
        # 循环 创建按钮
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())