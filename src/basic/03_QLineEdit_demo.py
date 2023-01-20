import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit, QLabel, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('PyQt5桌面应用')
    # 纯文本
    l = QLabel('账号：',w)
    l.setGeometry(20, 20, 30, 20)

    # 文本框
    e = QLineEdit(w)
    e.setPlaceholderText("请输入账号")
    e.setGeometry(55, 20, 200, 20)

    # 在窗口添加控件
    btn = QPushButton('注册', w)
    btn.setGeometry(50, 80, 70, 30)

    w.show()

    sys.exit(app.exec_())
