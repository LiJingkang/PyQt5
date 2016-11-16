# 事件
# 所有的GUI应用都是事件驱动的
# 但是事件可能由其他条件触发，比如：一个网络连接，一个窗口管理器，一个定时器，这些动作都可能触发事件的产生。
# 当我们调用应用的exec_()方法时，应用进入了主循环。
# 主循环用于检测事件的产生并且将事件送到用于处理的对象中去。

# 事件源
# 事件对象
# 事件目标

# PyQt5有一个独一无二的信号和槽机制来处理事件。
# 信号和槽用于对象之间的通信。
# 当指定事件发生，一个事件信号会被发射。
# 槽可以被任何Python脚本调用。
# 当和槽连接的信号被发射时，槽会被调用。
import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                    QLCDNumber, QSlider, QVBoxLayout)
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd = QLCDNumber(self)     #创建LCD数字对象
        sld = QSlider(Qt.Horizontal,self)  #创建水平滑动轴对象

        vbox = QVBoxLayout()   #创建垂直盒子布局
        vbox.addWidget(lcd)  #组件添加
        vbox.addWidget(sld)  #组件添加

        self.setLayout(vbox)  #窗口中添加布局

        # 将滑块条的 valueChanged 信号和 lcd 数字显示的 display 槽连接在一起
        sld.valueChanged.connect(lcd.display) #当滑动时，数字随之变化

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Signal & slot')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())