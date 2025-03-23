"""
DPA v0.1
- [*] 基础框架
- [ ] 图形化界面
- [ ] 历史记录
"""


class DPA:
    __version__ = '0.1'

    def __init__(self, initial_value=0):
        self.value = initial_value  # 初始值
        print(f'DPA v{self.__version__}')
        print('-' * 20)

    def update(self, value):
        self.value += value
        print(f'当前DP：{self.value}')


def main():
    obj = DPA()
    print(f'当前DP：{obj.value}')
    while True:
        try:
            up_value = int(input('输入整数以更新DP：'))
            obj.update(up_value)
        except ValueError:
            print('输入类型有误')
            break


if __name__ == '__main__':
    main()
