import sys
import random

card_list = ['神吕布','神关羽','赵云','关羽','张飞']    # 卡片列表
my_cards = {}   # 我的卡片和数量

def pickcards():    # 随机抽取卡片
    card = card_list[random.randint(0, 4)]
    if my_cards.get(card):
        my_cards[card] += 1
    else:
        my_cards[card] = 1
    print('得到卡片：{}'.format(card))

def backpack():
    print(my_cards)

if __name__ == '__main__':
    while True:
        signal = input('''冲值能让你变强:
             请选择指令：
             1.抽卡
             2.查看背包
             \r输入指令：''')
        if signal == '1':
            try:                # 检测代码
                times = int(input('输入抽取次数：'))
            except ValueError:  # 如果捕获到这个异常
                print('Parameter Error')
                exit()
            else:               # 否则
                for i in range(times):
                    pickcards()
        elif signal == '2':
            backpack()
        else:
            print('Parameter Error')
            break
