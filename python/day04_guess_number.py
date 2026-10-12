from random import randint
secret_number = randint(1,100)
attempts = 0
while True:
    
    number = int(input("what's your number"))
    attempts +=1
    if number == secret_number:
        print(f"恭喜你猜对了！目标数字就是 {secret_number}，你一共猜了 {attempts} 次！")
        break
    elif number > secret_number:
        print("太大了，再猜猜看！")
    else:
        print("太小了，再大胆点！")

