# 信号对象有 emit 方法用来发射信号，然后信号对象还有 disconnect 方法断开某个信号和槽的连接。
# 一个信号可以连接多个槽，多个信号可以连接同一个槽，
# 一个信号可以与另外一个信号相连接。

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QCheckBox, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QObject, pyqtSlot

# 首先自建的信号必须是类的属性，然后这个类必须是QObject的子类，
# 这里QDialog是继承自QObject的。
class FindDialog(QDialog):
    # 通过pyqtSignal函数来自建信号 一个是字符串 一个是 QtCaseSensitivity 的枚举值
    findNext = pyqtSignal(str, Qt.CaseSensitivity)
    findPrevious = pyqtSignal(str, Qt.CaseSensitivity)

    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel(self.tr("Find &what:"))
        self.lineEdit = QLineEdit()
        label.setBuddy(self.lineEdit)

        self.caseCheckBox = QCheckBox(self.tr("Match &case"))
        self.backwardCheckBox = QCheckBox(self.tr("Search &backward"))
        self.findButton = QPushButton(self.tr("&Find"))
        self.findButton.setDefault(True)
        self.findButton.setEnabled(False)
        closeButton = QPushButton(self.tr("Close"))

        self.lineEdit.textChanged.connect(self.enableFindButton)
        # 点击之后将执行 findClicked 槽。这个 信号不带参数  所以后面的 findClicked 也可以没有参数
        self.findButton.clicked.connect(self.findClicked)
        closeButton.clicked.connect(self.close)

        topLeftLayout = QHBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(self.lineEdit)
        leftLayout = QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(self.caseCheckBox)
        leftLayout.addWidget(self.backwardCheckBox)
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.findButton)
        rightLayout.addWidget(closeButton)
        rightLayout.addStretch()
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle(self.tr("Find"))
        self.setFixedHeight(self.sizeHint().height())

    def enableFindButton(self, text):
        self.findButton.setEnabled(bool(text))

    # 自定义信号
    @pyqtSlot()
    def findClicked(self):
        # 确定了当前 QlineEdit 的 text 和 cs 也就是大小写是否检查的状态
        text = self.lineEdit.text()
        if self.caseCheckBox.isChecked():
            cs = Qt.CaseSensitive
        else:
            cs = Qt.CaseInsensitive
        # 然后根据向前或者向后是否勾选来确定接下来要发送的信号。
        if self.backwardCheckBox.isChecked():
            self.findPrevious.emit(text, cs)
        else:
            # findNext 正是我们之前定义的信号
            self.findNext.emit(text, cs)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    findDialog = FindDialog()

    # 定义了两个简单的函数
    def find(text, cs):
        print('find:', text, 'cs', cs)


    def findp(text, cs):
        print('findp:', text, 'cs', cs)

    # 将 findDialog 的这两个信号和上面的两个函数连接起来
    # 当我们点击Find按钮，首先执行FindClicked 然后发送了findNext 信号。
    # 信号又与find函数相连。
    findDialog.findNext.connect(find)
    findDialog.findPrevious.connect(findp)
    findDialog.show()
    sys.exit(app.exec_())
