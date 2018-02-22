import random
secret = random.randint(1,10)
print("-----------试炼习---------")
temp = input("让我来猜猜")
guess = int(temp)
while guess != secret:
    temp = input("错了吧。再来一次")
    guess = int(temp)
    if guess == secret:
        print("算你狠")
        print("知道就知道呗")
    else:
        if guess >secret:
            print("哥哥，大了")
        if guess <8:
            print("嘿嘿，小了小了")
print("结束")    
 
