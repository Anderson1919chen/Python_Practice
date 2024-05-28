#檔案的讀取、寫入

# open("檔案路徑", mode="開啟模式")
# 絕對路徑  ex:C:/Users/User/Desktop/python/123.txt
# 相對路徑  以程式的位子去做延伸 ex:123.txt

# mode="r"讀取
# mode="w"覆寫
# mode="a"在原先的資料後寫東西

file = open("123.txt", mode="w", encoding="utf-8")
# for line in file:
#    print(line) 把file裡的依次列出來
# print(file.readline()) 讀一行
# print(file.readlines()) 把檔案放入列表內
file.write("你好")
file.close()

with open("123.txt", mode="a", encoding="utf-8") as file: # 不用寫file.close()的方法
    file.write("\n哈哈")