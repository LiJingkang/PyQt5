import sys
from PyQt5.QtWidgets import QHBoxLayout, QSlider, QSpinBox, QApplication, QWidget
from PyQt5.QtCore import Qt

# 创建 QApplication
app = QApplication(sys.argv)
# 创建 QWidget
window = QWidget()
window.setWindowTitle("enter your age") # 设置标题
# 创建QSpinBox
spinBox = QSpinBox()
slider = QSlider(Qt.Horizontal)
spinBox.setRange(0,130)
slider.setRange(0,130)
# 将spinBox的 valueChanged 信号和slider的 setValue 槽连接起来了
# 其中QSpinBox内置的 valueChanged 信号发射自带的一个参数就是改变后的值，
# 这个值传递给了QSlider的内置槽 setValue，从而将slider的值设置为新值。
#
# 第17行如果slider的值发生了改变，那么会发送valueChanged信号，然后又传递给了spinBox，
# 并执行了内置槽setValue，由于此时的值即为原值，这样spinBox内的值就没有发生改变了，
# 如此程序不会陷入死循环。
spinBox.valueChanged.connect(slider.setValue)
slider.valueChanged.connect(spinBox.setValue)

spinBox.setValue(35)

layout = QHBoxLayout()
layout.addWidget(spinBox)
layout.addWidget(slider)


window.setLayout(layout)
window.show()

sys.exit(app.exec_())
