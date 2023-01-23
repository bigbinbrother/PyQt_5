import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QFormLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 禁止改宽高
        self.setFixedSize(250, 150)
        self.setWindowTitle('登录')
        self.setWindowIcon(QIcon('../img/Panda.ico'))

        # 外层容器
        container = QVBoxLayout()

        # 表单容器
        form_layout = QFormLayout()

        # 创建第一个输入框
        edit1 = QLineEdit()
        edit1.setPlaceholderText('请输入账号')
        form_layout.addRow("账号:", edit1)

        # 创建第2个输入框
        edit2 = QLineEdit()
        edit2.setPlaceholderText('请输入密码')
        form_layout.addRow("密码:", edit2)

        # 将表单容器添加到外层容器中
        container.addLayout(form_layout)

        # 按钮
        login_btn = QPushButton("登录")
        login_btn.setFixedSize(100, 30)
        # 将按钮添加到容器中并设置对其方式
        container.addWidget(login_btn, alignment=Qt.AlignRight)

        # 设置主窗口的布局
        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())