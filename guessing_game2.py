secret_num = 77
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int(input("請輸入1-100的數字:"))
        if guess > secret_num:
            print("太大了")
        elif guess < secret_num:
            print("太小了")
    else:
        out_of_limit = True

if guess_count > guess_limit:
    print("你輸了")
else:
    print("恭喜你贏了")    