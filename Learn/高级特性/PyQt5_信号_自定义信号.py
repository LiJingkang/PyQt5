from PyQt5.QtCore import QObject, pyqtSignal

# 定义了一个新的信号
# 必须是GObject 的子类
# 定义了一个 closed 信号
class Foo(QObject):
    closed = pyqtSignal()
    # 定义了一个信号，接受 int int 信号的名称为 rangeChanged
    range_changed = pyqtSignal(int, int, name='rangeChanged')