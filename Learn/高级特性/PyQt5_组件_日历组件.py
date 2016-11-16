# 日历组件 QCalendarWidget类
import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication)
from PyQt5.QtCore import QDate

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 日历组件
        cal = QCalendarWidget(self)
        # 可选择
        cal.setGridVisible(True)
        # 移动的位置
        cal.move(20, 20)
        #
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        # selectedDate()方法检索被选中的日期
        # 转化成字符串显示在标签组件上。
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
