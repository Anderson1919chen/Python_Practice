# 猜數字遊戲

import random
answer = random.randint(1,10)
num1 = int(input("請輸入數字:"))
i = 1

while num1 != answer and i < 3:
    if num1 < answer:
        print("太小了")
        num1 = int(input("請輸入數字:"))
        i = i + 1 
        if i >= 3:
            print("你輸了")   
    elif num1 > answer:
        print("太大了")
        num1 = int(input("請輸入數字:"))
        i = i + 1
        if i >= 3:
            print("你輸了")
if i < 3:        
    print("恭喜答對")
    

