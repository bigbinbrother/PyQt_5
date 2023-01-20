import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QDesktopWidget
import time

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('PyQt桌面应用')

    # 纯文本
    l1 = QLabel('账号:', w)
    l1.setGeometry(20, 20, 30, 20)

    l2 = QLabel("密码:", w)
    l2.setGeometry(20, 50, 30, 20)

    # 文本框
    e1 = QLineEdit(w)
    e1.setPlaceholderText("请输入账号")
    e1.setGeometry(55, 20, 200, 20)
    e2 = QLineEdit(w)
    e2.setPlaceholderText("请输入密码")
    e2.setGeometry(55, 50, 200, 20)

    # 添加控件
    btn1 = QPushButton("注册", w)
    btn1.setGeometry(60, 100, 70, 30)
    btn2 = QPushButton("登录", w)
    btn2.setGeometry(160, 100, 70, 30)

    # 设置窗口大小
    w.resize(300, 150)

    # 设置窗口初始位置
    w.move(0, 0)

    # 设置屏幕中点
    center_point = QDesktopWidget().availableGeometry().center()
    # print(center_point)
    x = center_point.x()
    y = center_point.y()
    print(x, y)
    w.move(x-150, y-75)


    w.show()

    sys.exit(app.exec_())