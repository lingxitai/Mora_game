import random
from random import randint
x=0
y=0
z=0
while True:
    a=input('请输入内容：石头，剪刀，布\n')
    c=random.choice(['石头','剪刀','布'])
    print(c)
    if a==c:
        print('平手')
        z+=1
    elif a =='石头' and c =='剪刀':
        print('恭喜你赢了')
        x=x+1
        z += 1
    elif a =='石头'and c =='布':
        print('完蛋输了')
        y+=1
        z += 1
    elif a == '剪刀' and c == '布':
        print('恭喜你赢了')
        x = x + 1
        z += 1
    elif a == '剪刀' and c == '石头':
        print('完蛋输了')
        y += 1
        z += 1
    elif a == '布' and c == '石头':
        print('恭喜你赢了')
        x = x + 1
        z += 1
    elif a == '布'and  c == '剪刀':
        print('完蛋输了')
        y += 1
        z += 1
    else:
        break
print('游戏结束')
try:
    print('总计游戏{0}局，胜出{1}局，胜出率为{2}'.format(z,x,round(x/z,2)))
except ZeroDivisionError as e:
    print('一局都没开始，怎么统计，请认真输入')
