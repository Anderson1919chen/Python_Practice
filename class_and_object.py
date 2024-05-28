# 類別class、物件object
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios",123,True)
print(phone1.os)
phone2 = Phone("android",124,False)
print(phone2.os)