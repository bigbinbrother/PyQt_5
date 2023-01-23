import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QVBoxLayout, QCheckBox, QGroupBox
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口大小
        self.resize(300, 300)

        # 设置窗口标题
        self.setWindowTitle("熊猫电影")

        # 设置窗口图标
        self.setWindowIcon(QIcon('../img/Panda.ico'))

        # 创建一个垂直的容器
        container = QVBoxLayout()
        # container = QHBoxLayout()

        # 创建一个爱好的盒子
        hobby_box = QGroupBox('爱好')
        v_layout = QVBoxLayout()
        btn1 = QCheckBox('抽烟')
        btn2 = QCheckBox('喝酒')
        btn3 = QCheckBox('烫头')

        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)

        # 把v_layout添加到hobby_box
        hobby_box.setLayout(v_layout)

        # 创建第二个性别组
        gender_box = QGroupBox('性别')
        h_layout = QHBoxLayout()
        btn4 = QRadioButton('男')
        btn5 = QRadioButton('女')

        # 添加到h_layout
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)

        # 把h_layout添加到gender_box
        gender_box.setLayout(h_layout)

        # 把爱好盒子添加到容器
        container.addWidget(hobby_box)

        # 把性别盒子添加到容器
        container.addWidget(gender_box)

        # 设置容器的布局
        self.setLayout(container)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()

    sys.exit(app.exec_())