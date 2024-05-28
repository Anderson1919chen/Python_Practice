#if 判斷句

#hungry = False
#if hungry:
#    print("eating")
#else:
#    print("sleeping")

score = 60
if score == 100:
    print("+1000")
elif score >= 80:
    print("+500")
elif score >= 60:
    print("+60")
else:
    print("-300")

#且:and,或:or
score = 90
rainy = True
if score == 100 and rainy:
    print("給1000")
else:
    print("給100")

#假如沒有考100分 或 沒有下雨
#要給1000

score = 90
rainy = True
if score != 100 or not(rainy):
    print("給1000")
else:
    print("給100")

#max_num要傳入三個參數，回傳哪個是最大的
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2
    
    else:
        return num3

print(max_num(1,2,2))