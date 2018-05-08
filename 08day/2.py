import random

YuQiLin_secret=random.randint(1,99)#生成随机数
YuQiLin_time=1#猜数字的次数
YuQiLin_guess=0#输入的数字
YuQiLin_minNum=0#最小随机数
YuQiLin_maxNum=99#最大随机数

while YuQiLin_guess != YuQiLin_secret and YuQiLin_time>=0:#条件
    YuQiLin_guess = int(input("*数字区间0-99，请输入你猜的数字:"))
    print("你输入数字是：",YuQiLin_guess)
    if YuQiLin_guess == YuQiLin_secret:
        print("猜对了，真厉害")
    else:

        if YuQiLin_guess < YuQiLin_secret:
            YuQiLin_minNum = YuQiLin_guess
            print("你的猜数小于正确答案")            
            print("现在的数字区间是：",YuQiLin_minNum,"-",YuQiLin_maxNum)
        else:
            YuQiLin_maxNum = YuQiLin_guess
            print("你的猜数大于正确答案")
            print("数字区间是：",YuQiLin_minNum,"-",YuQiLin_maxNum)
        print("太遗憾了，你猜错了，你用",YuQiLin_time,"次")
    YuQiLin_time+=1
print("游戏结束")
print("你用",YuQiLin_time,"次")