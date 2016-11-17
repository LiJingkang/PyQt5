# 按照python格式自己定义的函数就是所谓的自定义槽了。
#
# 不过推荐用pyqt的槽装饰器来定义槽。

# 定义了一个名为 foo 的槽不接受任何参数
from PyQt4.QtCore import  pyqtSlot
    #1
    @pyqtSlot()
    def foo(self):
        pass
    #2
    # 接受两个参数
    @pyqtSlot(int, str)
    def foo(self, arg1, arg2):
        pass
    #3
    # 槽的名字叫 bar
    @pyqtSlot(int, name='bar')
    def foo(self, arg1):
        pass
    #4
    # 接受一个 int 返回一个 int
    @pyqtSlot(int, result=int)
    def foo(self, arg1):
        pass
    #5
    # 接受一个 int 类型 和QObject 类型的参数
    @pyqtSlot(int, QObject)
    def foo(self, arg1):
        pass

    # 这里定义了两个槽，一个接受 int 类型。 一个接受 QString 类型
    # Python 中不推荐这么使用
    @pyqtSlot(int)
    @pyqtSlot('QString')
    def valueChanged(self, value):
    pass