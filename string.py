print("Hello \nMr.White")#換行

print("Hello\" Mr.White")

#function

phrase = "Hello Mr.White"

print(phrase.upper())#所有字串內的字母變大寫
print(phrase.lower())#所有字串內的字母變小寫

print(phrase.isupper())#檢查字串內的字母是否都是大寫
print(phrase.islower())#檢查字串內的字母是否都是小寫

print(phrase.lower().islower())#先轉小寫再判斷

print(phrase[1])#字串內的第1位的值是什麼

print(phrase.index("h"))#想找到字串中的h在哪一位

print(phrase.replace("H","h"))#在字串裡面用"h"替換"H"