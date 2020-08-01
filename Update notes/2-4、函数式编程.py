
# coding: utf-8

# # log模块资料
# - https://www.cnblogs.com/yyds/p/6901864.html

# # python 语言的高级特性

# ## 函数式编程（function programming）
# - 基于lambda演算的一种编程方式
#   - 程序中只有函数
#   - 函数可以作为参数，同样可以作为返回值
#   - 纯函数编程语言： LISP   Haskell
#   
# - Python 函数式编程只是借鉴函数式编程的一些特点，可以理解成一半函数式一半Python
# - 需要讲述
#   - 高阶函数
#   - 返回函数
#   - 匿名函数
#   - 装饰器
#   - 偏函数

# ### lambda表达式
# - 函数： 最大程度复用代码
#   - 存在问题： 如果函数很小，很短，则会造成啰嗦
#   - 如果函数被调用次数很少，则会造成浪费
#   - 对于阅读者来说，会造成阅读流程的被迫中断
#   
# - lambda 表达式（匿名函数）：
#   - 一个表达式，函数相对简单
#   - 不是一个代码块，仅仅是一个表达式
#   - 可以有参数，有多个参数，用逗号隔开
#   - 用法：
#   
#         1. 以lambda开头
#         2. 紧跟一定的参数（如果由的话）
#         3. 参数后用冒号和表达式主体隔开
#         4. 只是一个表达式，所有，没有return

# In[1]:


# “小”函数举例
def p():
    print("dadadada")
    
p()


# In[2]:


#        1. 以lambda开头
#        2. 紧跟一定的参数（如果由的话）
#       3. 参数后用冒号和表达式主体隔开
#      4. 只是一个表达式，所有，没有return


#计算一个数字100倍数
# 因为就是一个表达式，所以没有return

slm = lambda n:100 * n
# 使用跟函数调用一样
slm(9)


# In[3]:


ss = lambda x,y,z:x + y * 10 + z * 20
ss(1,2,3)


# ### 高阶函数
# - 把函数作为参数使用的函数，叫做高阶函数

# In[5]:


# 变量可以赋值
# 函数名称就是一个变量
def kk():
    print("哈哈")
    
    
ss = kk
ss()


# ### 以上代码得出的结论
# - 函数名变量
# - ss和kk只是名称不一样而已
# - 既然函数名称是变量，则应该可以被当做参数传入另一函数

# In[12]:


# 高阶函数举例
# funa是一个普通函数，返回一个传入数字的100倍

def funa(n):
    return n * 100


# 在写一个函数，把传入参数乘以300倍，利用高阶函数

def funb(n):
    # 最终返回300n
    return funa(n) * 3

print(funb(2))
# 写一个高阶函数
def func(n, f):
    # 假定函数把n扩大100倍
    return f(n) * 3
print(func(2,funa))

# 比较func和funb，显然func的写法优于funb
#例如：

def fund(n):
    return n * 10

# 需求变化，需要把你当大30倍，此时funb无法实现
print(func(7,fund))


# ###   系统高阶函数-map（映射）
# - 把集合或者列表里的元素，每一个元素都按一定规则进行操作，生成一个新的集合或者列表
# - map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象

# In[4]:


help(map)


# In[11]:


# map举例
# 有一个列表，想对列表里的每一个元素乘以10，并得到新的列表

l1 = [i for i in  range(11)]
print(l1)
l2 = []
l3 = []
for i in l1:
    l2.append(i * 10)
    
print(l2)
print("*"*30)

# 利用map实现

def mm(n):
    return n * 10

l3 = map(mm,l1)
# map类型是一个迭代的结构，所有可以使用for遍历
print(l3)
print(type(l3))
for i in l3:
    print(i)

l4 = [i for i in l3]    
print(l4)


# ### reduce 
# - 意思是归并，缩减
# - 把一个可迭代对象最后归并成一个结果
# - 对于函数参数由要求： 必须有两个参数，必须由返回结果
# - reduce([1,2,3,4,5,]) == f(f(f(f(1,2)3)4)5)
# - reduce 需要导入functools包

# In[13]:


# from functools import reduce

#定义一个操作函数
#加入操作函数只是相加
def myadd(x,y):
    return x + y

# 对于列表[1,2,3,4,5,6] 执行myadd的reduce操作
kk = reduce(myadd, [1,2,3,4,5,6])# 两个两个的加
print(kk)


# ### filter 函数
# - 过滤函数： 对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
# - 跟map相比较：
#   - 相同： 都对列表的每一个元素逐一进行操作
#   - 不同：
#     - map会生成一个跟原来数据相对应的新列表
#     - filter不一定，只要符合条件的才会进行新的数据集合
#   - filter函数怎么写：
#     - 利用给的函数进行判断
#     - 返回值一定是个布尔值
#     - 调用格式： filter（f， date），f是过滤函数，date是数据

# In[15]:


# filter案列
# 对于一个列表，对其进行过滤，偶数组成一个新的列表

# 需要定义过滤函数
# 过滤函数要求有输入， 返回布尔值
def iseven(a):
    return a % 2 == 0

l = [1,2,3,4,5,6,7,8,9,44,223,312]
kk = filter(iseven,l)
print(type(kk))
print(kk)
print("*"* 30)
print([i for i in kk])


# ### 高级函数——排序
# - 把一个序列按照给定算法进行排序
# - key： 在排序线对每一个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排序
# 

# In[16]:


# 排序的案例1

a = [23,2343,54,63,43,1,42,0,31,23214,0.1]
al = sorted(a, reverse=True)
print(al)


# In[18]:


# 排序案例2
b = [-2,-3,31,3,12,0,1,-0.231,2222]
#按照绝对值进行排序
# abs是求绝对值的意思
al = sorted(b, key= abs,reverse=True)
print(al)


# In[20]:


# sorted 案例
dd = ["dann","Dann","wangdadal","dahkd"]

str1 = sorted(dd)
print(str1)

str2 = sorted(dd, key=str.lower)
print(str2)


# # 返回函数
# - 函数可以返回具体的值
# - 也可以返回一个函数作为结果
# 

# In[22]:


# 定义一个普通函数
def mya(a):
    print("kkakd")
    return None

a = mya(8)
print(a)


# In[27]:


# 函数作为返回值返回，被返回的函数在函数体内定义

def my1():
    def my2():
        print("in my2")
        return 3
    return my2

f3 = my1()
print(type(f3))
print(f3)
f3()


# In[29]:


# 负责一点的返回函数的列子
# args： 参数列表
# 1. my4定义函数，返回内部定义的函数my5
# 2. my5使用了外部变量，这个变量是my4 的参数

def my4(*args):
    def my5():
        ll = 0 
        for n in args:
            ll += n
        return ll
    return my5

f5 = my4(1,2,3,4,5,6,7,8,9,0)
# f5 调用方式
f5()


# ## 闭包
# - 当一个函数在内部定义函数，并且内部的函数应用外部函数的参数或者局部变量，当内部函数 被作为返回值的时候，相关参数和变量保存在返回值的函数中，这种结果，叫闭包
# - 上面定义的my4是一个标准的闭包结构

# In[47]:


# 闭包常见的坑

def count():
    # 定义一个列表
    fk = []
    for i in range(1,4):
        #定义一个函数
        def f():
            return i * i
        fk.append(f)
    return fk

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())


# ### 出现的问题：
# - 造成上述状况的原因是，返回函数引用了变量i，i非立即执行，而是等到三个函数都返回的时候才统一使用，此时i已经变成3了，最终调用的时候，都返回的是3 * 3
# - 此问题描述成：返回闭包时，返回函数不能引用任何循环变量
# - 解决方案： 在创建一个函数， 用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数不在改变。

# In[48]:


# 闭包常见的坑

def count1():
    def f(j):
        def kk():
            return j * j
    return kk
    fk = []
    for i in range(1,4):
        fk.append(f(i))
    return fk
h1, h2, h3 = count1()
print(h1())
print(h2())
print(h3())


# ### 装饰器
# - 在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数
# - 装饰器的使用，使用@语法，即在每次要扩展到函数定义前使用@+函数名

# In[50]:


def hello():
    print("hello world")
    
hello()


# In[52]:


f = hello
f()


# In[59]:


# f 和hello是一个函数
print(id(f))
print(id(hello))

print(f.__name__)
print(hello.__name__)


# In[61]:


# 限制有新的需求
# 对hello功能扩展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# ==>使用装饰器

import time

# 高阶函数，以函数作为参数
def printtime(f):
    def wrapper(*args, **kwargs):
        print("time: ", time.ctime())  #很固定的写法
        return f(*args, **kwargs)
    return wrapper
# 上面定义一个装饰器，使用的时候需要用到@
@printtime
def hello():
    print("hello world")
    
hello()


# In[67]:


# 装饰器的好处，，，一点定义，则可以装饰任意函数
# 一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上
# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始动手执行下装饰器
# 首先定义函数

def hello1():
    print("手动执行")
    
hello1()

hello1 = printtime(hello1)
hello1()
print("*"*20)

l = printtime(hello1)
l()


# ### 偏函数

# In[70]:


# 把字符串转化成十进制数
int("12345")
# 求八进制的字符串12345，表示成十进制数是多少
int("12345", base=8)


# In[72]:


# 新建一个函数，此函数是默认输入的字符串是16进制数字
# 把此字符串返回十进制的数字

def int16(x, base=16):
    return int(x, base)
int16("12345")


# ### 偏函数
# - 参数固定的函数， 相当于一个由特定参数的函数体
# - functools.partial的作用是：一个函数某个函数固定，返回一个新的函数

# In[73]:


import functools

# 实现上面的int16的功能

int16 = functools.partial(int, base=16)
int16("12345")

