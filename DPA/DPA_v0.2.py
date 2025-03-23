"""
DPA v0.2
- [*] 基础框架
- [*] 图形化界面
- [ ] 历史记录
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt


class DPA(QWidget):
    __version__ = '0.2'

    def __init__(self, initial_DP=0):
        super().__init__()
        self.DP = initial_DP
        self.label = QLabel(f'DP：{self.DP}')  # DP 显示
        self.history_field = QTextEdit()      # 历史记录
        self.history_field.setReadOnly(True)  # 只读
        self.error_label = QLabel('')  # 报错显示
        self.error_label.setStyleSheet("QLabel { color: red; }")  # 报错显示红色
        self.input_field = QLineEdit()  # 输入框
        self.button = QPushButton('修改')
        self.initUI(initial_DP)

    def initUI(self, initial_value):
        self.setWindowTitle(f'DPA v{self.__version__}')
        h1, w1 = 1920, 1080  # 默认分辨率 1920 * 1080
        h2, w2 = 300, 200  # 窗口大小
        self.setGeometry((h1-h2)//2, (w1-w2)//2, h2, w2)  # 窗口位置和大小

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.history_field)
        layout.addWidget(self.error_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.update)

    def update(self):
        if not self.input_field.text():  # 如果输入框为空
            return  # 不执行任何操作
        try:
            up_value = int(self.input_field.text())
            self.DP += up_value
            self.label.setText(f'DP：{self.DP}')
            self.error_label.setText('')
        except ValueError:
            self.error_label.setText('输入类型有误，请输入整数')
        finally:
            self.input_field.clear()  # 清空输入框

    def keyPressEvent(self, event):
        # 重写keyPressEvent方法以处理键盘事件
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # 如果按下的是回车键，则模拟按钮点击
            self.button.click()


def main():
    app = QApplication(sys.argv)
    obj = DPA()
    obj.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
