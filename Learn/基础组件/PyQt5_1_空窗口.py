import sys
# QWidget 组件导入
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == '__main__':
    # sys.argv 来自命令行的参数列表
    # PyQt5 都必须创建一个 Application 对象
    app = QApplication(sys.argv)
    # 所有用户界面的基础类  提供默认的构造方法  没有父类的 Widget 组件将当作一个窗口使用
    w = QWidget()
    # 宽 高
    w.resize(250, 150)
    # 移动 QWidget 组件到一个位置
    w.move(300, 300)
    # 设置标题
    w.setWindowTitle('Simple')
    # 显示  先在内存中创建 再在屏幕上显示
    w.show()
    # 进入主循环
    # 主循环用于接收来自窗口触发的事件，并且转发他们到widget应用上处理
    # 如果我们调用exit()方法或主widget组件被销毁，主循环将退出
    sys.exit(app.exec_())
