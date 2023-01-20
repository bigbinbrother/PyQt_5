import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('PyQt5桌面程序')
    # w.resize(400, 200)

    # 添加控件label
    # l = QLabel('账号')
    # 将Label控件添加到主窗口
    # l.setParent(w)

    # 创建label控件，并添加其到主窗口
    l = QLabel('账号：', w)
    # 显示位置和大小 x,y,w,h
    # x,y 表示控件左上角位置
    # w,h 表示控件的宽和高
    l.setGeometry(0,100, 500, 50)
    w.show()

    sys.exit(app.exec_())