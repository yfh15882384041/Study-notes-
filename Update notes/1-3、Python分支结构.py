
# coding: utf-8

# # 程序结构
# - 顺序
# - 循环
# - 分支
# ## 分支结构
# - 分支结构基本语法
#   - if 条件表达式：
#        - 语句1
#        - 语句2
#        - 语句3
#        - 。。。。
# - 条件表达式的计算结果必须是布尔值
# - 表达式后面的冒号不能少
# - 注意if后面出现的语句，如果属于if语句块，则必须同一个缩进等级
# - 条件表达式结果为True执行if后面的缩进的语句块

# In[2]:


#if语句联系
#注意字符串的真假：空字符串为False，其余都为True


# # 双向分支
# - if....else....
# - 二选一

# ## input的作用
# - 在屏幕上或是键盘上输出括号内的字符串
# - 接受用户输入的内容并返回到程序（也就是说负责接受用户输入并将内容返回给变量）
# - input返回的内容一定是字符串类型
# 

# In[4]:


gender = input("请输入性别")#也就是说负责接受用户输入并将内容返回给变量
print(gender)

if gender == "man":
    print("您好")
    print("请回家")
else:
    print("美女你好")
    print("加个微信")


# In[7]:


#考试成绩判断
#成绩由用户输入
#90以上为：优秀
#80-90：良
#70-80：中
#60-70：合格
#60以下：我没有你这个学生

#输入成绩需要用到input函数
score = input("请输入成绩：")
#由于输入是字符串，需要转换
score = int(score)

if score >= 90:
    print("优秀")
if score >= 80 and score < 90:
    print("良")
if score >= 70 and  score <80:
    print("中")
if score >= 60 and score <70:
    print("合格")
if score < 60:
    print("我没有你这个学生")


# # 多路分支
# - 很多个分支，叫多路分支
#     - if  条件表达式：
#      - 语句1
#      - ...
#     - elif 条件表达式：
#      - 语句1
#      - ...
#     - elif  条件表达式：
#      - 语句1
#      - ...
#     - else:
#     - 语句1
#     - ...
# - elif 可以有好多个
# - else可选
# - 多路分支最多只会执行一种情况
# ## if语句补充
# - if语句可以嵌套，但是不推荐使用。
# - Python没有switch语句

# In[10]:


#考试成绩判断
#成绩由用户输入
#90以上为：优秀
#80-90：良
#70-80：中
#60-70：合格
#60以下：我没有你这个学生

#输入成绩需要用到input函数
score = input("请输入成绩：")
#由于输入是字符串，需要转换
score = int(score)

if score >= 90:
    print("优秀")
elif score >= 80 and score < 90:
    print("良")
elif score >= 70 and  score <80:
    print("中")
elif score >= 60 and score <70:
    print("合格")
else:
    print("我没有你这个学生")

