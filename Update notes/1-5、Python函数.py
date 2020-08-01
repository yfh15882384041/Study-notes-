
# coding: utf-8

# 
# # 函数
# - 函数是代码的一种形式
# - 函数应该能完成一项特定的工作，而且一般一个函数完成一项工作
# - 有些语言，份函数和过程两个概念，通俗的解释是，有返回结果的叫函数，否则叫过程，但是Python不区分。
# - 函数的使用
#   - 函数的使用需要先定义
#   - 使用函数，称为调用

# In[2]:


#定义一个函数
#知识定义的话不执行
#1.def关键字，后跟一个空格
#2.函数名，自己定义，起名需要遵循便命令规则，约定俗成，大驼峰使用类用
#3.后面括号和冒号不能省，括号内可以有参数
#4.函数内所有代码缩进


def fune():
    print("我是一个函数")
    print("这是执行内容")
    
print("函数结束")


# In[3]:


#函数的调用
#直接写出函数名，后面括号不能省略，内容根据实际情况
fune()


# # 函数的参数和返回值
# - 参数：负责给函数传递一些必要的数据或者信息
#   - 形参（形式参数）：在函数定义的时候用到的参数，没有具体含义
#   - 实参（实际参数）：在调用函数的时候输入的值
# - 返回值：调用函数的时候的一个执行结果
#   - 使用return返回结果
#   - 如果没有值需要返回，我们推荐使用return None表示函数结束
#   - 如果函数没有return关键字，则函数默认返回None

# In[7]:


#形参与实参的案例
#参数person只是一个符号
#调用的时候用另一个
def hello(person):
    print("{0},你好啊".format(person))
    print("{},你看见我的玩具了吗".format(person))


p = "小奶猫"
#调用函数，需要把P作为实参传入
hello(p)


# In[9]:


p = "哈哈哈"
hello(p)


# In[14]:


pp= hello("加的你")

print(pp)
#如果函数没有return关键字，则函数默认返回None


# In[17]:


#help 负责随时为你提供服务
#比如print
help(print)
help(None)#等价于help(print())


# In[33]:


#九九乘法表

for o in range(1,10):#控制外循环，从1-9
    for i in range(1,o + 1):#控制内循环
        print(o * i,end ="  ")   #end：最后一个值后附加的字符串，默认为换行符。
    print()    # print 默认有换行符
       
    
    


# In[38]:


#尝试用函数来打印九九乘法表
def jiujiu():
    for o in range(1,10):#控制外循环，从1-9
        for i in range(1,o + 1):#控制内循环
            print(o * i,end="  ")   #end：最后一个值后附加的字符串，默认为换行符。
        print()    # print 默认有换行符
    
    return None
jiujiu()
jiujiu()#编译型语言与解释型语言的区别


# In[52]:


#改造上面函数    改成内嵌函数
def printline(line_num):
    for i in range(1,line_num + 1):
        print(line_num * i,end="")
    print()

    
def jiujiu():
    for o in range(1,10):#控制外循环，从1-9
        printline(o)
        
    
    return None

jiujiu()


# # 参数详解
# - 参数分类
#   - 普通参数
#   - 默认参数
#   - 关键字参数
#   - 收集参数

# In[55]:


#普通参数案列

def normal_para(one, two, three):
    print(one +  three)
    return None

normal_para(3,5,4)
    


# In[59]:


#默认参数案列

def default_para(one, two, three=100):
    print(one + two)
    print(three)
    return None
default_para(3,3)
default_para(3,3,1)


# In[61]:


#关键字参数

def keys_para(one, two, three):
    print(one + three)
    print(three)
    return None

keys_para(one=1, two=3, three=2)

keys_para(two=3, three=2, one=1)   


# # 收集参数
# - 把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
# - 语法
# 
#       def func(*args):
#           func_body
#          按照list使用方式访问args得到传入的参数
# 
#        调用：
#        func(p1, p2, p3, .....)
# - 参数名args不是必须这么写，但是，我们推荐直接用args，约定俗成
# - 参数名args前需要由星号
# - 收集参数可以和其他参数共存
#     

# In[63]:


# 收集参数代码
# 函数模拟一个学生进行自我介绍，但具体内容不清楚
# args把他看做一个list
def stu( *args):
    print("Hello 大家好，我自我介绍以下，简答说两句：")
    # type函数作用是检测变量的类型
    print(type(args))
    for item in args:
        print(item)


stu("liuying", 18, "北京大通州区", "wangxiaojing", "single")

stu("周大神")


# In[65]:


# 收集参数案例
# 说明收集参数可以不带任何实参调用，此时收集参数为空tuple
stu()


# In[67]:



# 如果使用关键字参数格式调用，会出现问题
stu(name="liuying")


# # 收集参数之关键字收集参数
# - 把关键字参数按字典格式存入收集参数
# - 语法：
# 
#       def func( **kwargs):
#          func_body
# 
#       调用：
#         func(p1=v1, p2=v2, p3=v3........)
# - kwargs一般约定俗成
# - 调用的时候，把多余的关键字参数放入kwargs
# - 访问kwargs需要按字典格式访问

# In[68]:


# 收集参数案例
# 自我介绍
# 调用的时候需要使用关键字参数调用
def stu( **kwargs):
    # 在函数体内对于kwargs的使用不用带星号
    print("Hello 大家好，我先自我介绍一下：")
    print(type(kwargs))
    # 对于字典的访问，python2 和python3有区别
    for k,v in kwargs.items():
        print(k, "---", v)
    
stu(name="liuying",  age=19, addr="北京大通州区", lover="王晓静", work="Teacher")

print("*" * 50)

stu(name="周大神")


# # 收集参数混合调用的顺序问题
# - 收集参数，关键字参数，普通参数可以混合使用
# - 使用规则就是，普通参数和关键字参数优先
# - 定义的时候一般找普通参数，关键字参数，收集参数tuple，收集参数dict

# In[72]:


# 收集参数混合调用案例
# stu模拟一个学生的自我介绍
def stu(name, age, *args, hobby="没有", **kwargs):
    print("Hello 大家好")
    print("我叫 {0}， 我今年{1}大了。".format(name, age))
    if hobby == "没有":
        print("我没有爱好， so sorry")
    else:
        print("我的爱好是{0}".format(hobby))
        
    print("*" * 20)   
    
    for i in args:
        print(i)
    
    print("#" * 30)
    
    for k,v in kwargs.items():
        print(k, "---", v)
        
        
# 开始调用函数
name = "liuying"
age = 19


# 调用的不同格式
stu(name, age)

stu(name, age, hobby="游泳")

stu(name, age, "王晓静", "刘石头", hobby1="游泳", hobby2="烹饪", hobby3="跟不同女生聊天")


# In[71]:


# 收集参数混合调用案例
# stu模拟一个学生的自我介绍
def stu(name, age, *args, hobby="没有", **kwargs):
    print("Hello 大家好")
    print("我叫 {0}， 我今年{1}大了。".format(name, age))
    if hobby == "没有":
        print("我没有爱好， so sorry")
    else:
        print("我的爱好是{0}".format(hobby))
        
    print("*" * 20)   
    
    for i in args:
        print(i)
    
    print("#" * 30)
    
    for k,v in kwargs.items():
        print(k, "---", v)
        
        
# 开始调用函数
name = "liuying"
age = 19


# 调用的不同格式
stu(name, age)

stu(name, age, hobby="游泳")

stu(name, age, "王晓静", "刘石头", hobby="游泳", hobby2="烹饪", hobby3="跟不同女生聊天")


# In[70]:




