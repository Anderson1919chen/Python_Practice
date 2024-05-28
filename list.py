scores = [90,70,60,50,80]
friends = ["小黑","小黃","小綠"]
things = [90,"小黑",True]
#print(scores[1:])變為[70,60,50,80]
#函式 [extend,append,insert,remove,clear,pop,sort,reverse]
scores.extend(friends)
print(scores)

scores.append(30)
print(scores)

scores.insert(2,30)#在第幾位插入，其餘順移下去
print(scores)

scores.remove(90)#移除指定值
print(scores)

scores.pop()#移除列表的最後一位
print(scores)

#scores.sort()#把數值排序

scores.reverse()#把列表整個反轉
print(scores)

print(scores.index(60))#告訴我們所傳入的值在列表中的位置，60就是在列表中的第5位

print(scores.count(60))#告訴我們所傳入的值在列表中有幾個