num1 = input("請輸入一個數:")
num2 = input("請輸入另一個數:")
symbal = input("請輸入加減乘除:")

if symbal == "+":
    print(int(num1) + int(num2))
elif symbal == "-":
    print(int(num1) - int(num2))
elif symbal == "*":
    print(int(num1) * int(num2))
elif symbal == "%":
    print(int(num1) / int(num2))
else:
    print("Can't calculator")
