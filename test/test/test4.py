age=int(input("请输入狗狗的名字:"))
if age<0:
    print("你该不会是个傻子吧？")
elif age==1:
    print("相当于14岁的人")
elif age==2:
    print("相当于22岁的人")
elif age>2:
    human=22+(age-2)*5
    print("对应人类的年龄:",human)

