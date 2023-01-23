import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QWidget
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 创建主窗体
        self.setWindowTitle('计算器')
        self.setWindowIcon(QIcon('../img/Panda.ico'))

        # 准备数据
        data = {
            0: ['7', '8', '9', '+', '('],
            1: ['4', '5', '6', '-', ')'],
            2: ['1', '2', '3', '*', '<-'],
            3: ['0', '.', '=', '/', 'C']
        }

        # 整体垂直布局
        layout = QVBoxLayout()

        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText('请输入内容')
        # 把输入框添加到容器中
        layout.addWidget(edit)

        # 网格布局
        grid = QGridLayout()
        for line_number, number_li in data.items():
            for col_number, number in enumerate(number_li):
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)

        # 把网格布局添加到容器
        layout.addLayout(grid)

        # 设置主窗体布局
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

