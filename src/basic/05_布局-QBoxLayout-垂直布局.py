import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口大小
        self.resize(300, 300)
        # 设置窗口标题
        self.setWindowTitle("熊猫电影")
        # 设置窗口图标
        self.setWindowIcon(QIcon('../img/Panda.ico'))

        # 添加布局器
        layout = QVBoxLayout()

        layout.addStretch(1)
        # 添加按钮
        btn1 = QPushButton("按钮1")
        # 将按钮添加到布局器里
        layout.addWidget(btn1)

        layout.addStretch(1)

        # 添加按钮
        btn2 = QPushButton("按钮2")
        # 将按钮添加到布局器里
        layout.addWidget(btn2)
        layout.addStretch(1)

        # 添加按钮
        btn3 = QPushButton("按钮3")
        # 将按钮添加到布局器里
        layout.addWidget(btn3)

        layout.addStretch(1)
        # 让窗口使用当前布局器
        self.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

