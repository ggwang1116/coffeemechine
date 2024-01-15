me = int(input("請出拳 [0]剪刀 [1]石頭 [2]布"))
import random
com = random.randint(0, 2)

trans = ["剪刀", "石頭", "布" ]
#清單名字[號碼牌]
print('你出的拳：', trans[me])
print('電腦出的拳：', trans[com])

if me == com:
    print("平手")

elif me == (com + 1) % 3 :
    print("you win")

else :
    print("電腦贏了")
