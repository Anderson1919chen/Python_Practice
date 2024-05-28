#函式
def hello(name,age):
    print("hello" + name + "你今年" + str(age) + "歲")

hello("小白",87)

def add(name1,name2):
    print(name1 + name2)
    return 100

value = add(5,4)
print(value)
