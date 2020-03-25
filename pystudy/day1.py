"""
name=input("请输入你的姓名：")
job=input("请输入你的工作：")
hobby=input("请输入你的爱好:")
a="大家好，我叫{dfg},我喜欢{ert}，工作是{vgy}" .format(dfg=name,vgy=job,ert=hobby)
print(a)




zhangsan = ("张三",23,"男","路人甲")
lisi = ("李四",23,"男","路人甲")
wangwu = ("王五",23,"男","路人甲")
a = (zhangsan,lisi,wangwu)
print(zhangsan[3])

xx = "大家好，我叫{},我今年{}岁，我性别为{}，我的职业是{}".format(zhangsan[0],zhangsan[1],zhangsan[2],zhangsan[3])
print(xx)

"""
"""

username=input("请输入你的密码位数:")
if len(username)>=5 and len(username) <=10:
    print ("注册成功")
else:
    print ("注册失败")

"""
"""
#学习
age = int(input("请输入你的年纪:"))
if age>18:
    print("成年")
    if age>30:
        print("中年")
    else:
        print("哈哈")
else:
    print("小屁孩")



  a = {"name":"张三","age":"23","hifh":"11111"}
for i in a:
    print(i) 
    """
"""
for i in range(999) :
    print(i)
"""

a=1
while a<=9:
    print("循环",a)
    a=a+1
"""


