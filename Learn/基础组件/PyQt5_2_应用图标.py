import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class Example(QWidget): #创建新类  继承父类 QWideget
    def __init__(self): #构造函数  第一个 是 Example 的构造方法
        super().__init__() #继承父类  这个是  被继承的父类的 构造方法
        self.initUI() #调用内部静态方法。调用下面这个方法  GUI 的创建授予 initUI() 方法完成
    def initUI(self): #定义方法
        self.setGeometry(300, 300, 300, 300) #调用父类里面的方法调试窗口大小和位置
        self.setWindowTitle('Icon') #窗口名称
        self.setWindowIcon(QIcon('web.png')) #引入图片
        self.show() #执行显示
if __name__ == "__main__":
    app = QApplication(sys.argv)  #创建应用
    ex = Example() # 设置函数
    ex.initUI()  # 调用函数
    sys.exit(app.exec_()) #进入主循环