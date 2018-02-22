print("-----------试炼习---------")
temp = input("猜数字")
guess = int(temp)
if guess == 8:
    print("你是小甲鱼心理的蛔虫吗")
    print("猜中也没奖励")
else:
    if guess > 8:
        print("大了大了")
    else:
        print("是8")
print("结束,不玩啦")    
