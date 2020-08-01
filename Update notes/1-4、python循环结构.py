
# coding: utf-8

# # 循环语句
# - 重复执行某一个固定的动作或任务
# - 分类：
#   - for循环
#   - while 循环
# # for循环
# - 语句
#       for  变量 in  序列:
#        语句1
#        语句2
#        ...

# In[3]:


#列表知识
#比如[1,2,3,4,5,6,7,8,9]
list_one = [1,2,3,4,5,6,7,8,9,]

for 数字 in list_one:
    print(数字)
    print(数字+90-20)


# In[5]:


#打印学生列表姓名

stu_list = ["AAAA","BBBBB","CCCCC"]

for stu in stu_list:
    if stu == "BBBBB":
        print("你是对的")
    else:
        print("你是错的")


# ## for-else语句
# - for循环结束的时候，有时候需要执行一些收尾工作，此时需要else语句
# - else语句是可选的

# In[3]:


# for-else语句
#打印列表
#如果没有在列表中，或者列表结束了，我们需要打印提示语句
stu_list = ["李二","张三","王五"]

for stu in stu_list:
    if stu == "张三":
        print("你是对的")
    else:
        print("你是错的")
else:
    print("都不在")


# ## break，continue，pass
# - break :无条件结束整个循环，简称循环猝死。
# - continue:继续
# - pass：只是占位符，代表这句啥也不干，没有跳过功能。

# In[7]:


#确定一个数字队列中是否包含数字7，找到一个就行了
list_one = [1,2,3,4,5,6,7,8,7,]

for 数字 in list_one:
    if 数字 == 6:
        print("找到了")
        break
    else:
        print(数字)
    


# In[12]:


#continue语句练习
#在数字1-10中，找所有偶数，找到偶数后并打印出来

dig_one = [1,2,3,4,5,6,7,8,7,]
for dig in dig_one:
    if dig % 2 ==1:
        continue
    print("找到偶数了")
    print(dig)


# In[15]:


dig_one = [1,2,3,4,5,6,7,8,7,]
for dig in dig_one:
    if dig % 2 ==0:
        print("找到偶数了")
        print(dig)
#与上段程序相同
        
        
       


# In[18]:


#pass案列1
age = 19
if age > 19:
    pass    
else:
    print("太小")


# In[22]:


#pass案列2
ages = [2,444,523,5242,242]
for age in ages:
    pass
    print(ages)
    print(age)


# # range 函数
# - 生成有序数列
# - 生成数字队列可以定制

# In[25]:


#range案列1
#生成一个1-100的数字序列
#range的生成序列的两个数（左包括，右不包括）
#一般Python中，连个表示范围的数字都是左包括，右不包括
dig_list = range(1,20)
for dig in dig_list:
    print(dig)


# In[27]:


#range案列2
#打印从1-9的数字
for i in range(1,10):
    print(i)


# # while循环
# - 一个循环语句
# - 表示当条件成立的时候，就循环，适应于不知道具体循环次数
#       
#       while 条件表达式：
#        语句块
#        
#        #另一种表达方式
#        
#        while 条件表达式：
#         语句块1
#        else：
#         语句块2

# In[30]:


#while案列1
#钱存银行,多少年可以从一万到两万块钱——11年
benjin = 10000
year = 0

while benjin < 20000:
    benjin = benjin*(1+0.067)
    year += 1
    
print(year)


# In[31]:


#while案列2
#年利率
benjin = 10000
year = 0

while benjin < 20000:
    benjin = benjin*(1+0.067)
    year += 1
    
else:
    print(year)

