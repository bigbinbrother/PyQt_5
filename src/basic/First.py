import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

if __name__ == '__main__':
    # 使用QApplication创建类
    app = QApplication(sys.argv)
    # # 创建一个窗口
    # w = QWidget()
    # # 设置窗口大小
    # w.resize(400, 200)
    # # 移动窗口
    # w.move(300, 300)
    # # 设置标题
    # w.setWindowTitle('第一个基于PyQt5的桌面应用')
    # # 显示窗口
    # w.show()
    ui = uic.loadUi('../designer/demo.ui')
    ui.show()

    # 程序进入主循环
    sys.exit(app.exec_())