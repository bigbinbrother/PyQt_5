import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    # 在窗口中添加附控件
    btn = QPushButton()
    # 将控件添加到主窗口中
    btn.setParent(w)
    w.show()

    sys.exit(app.exec_())