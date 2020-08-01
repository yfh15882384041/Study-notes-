
# coding: utf-8

# # 主要内容
# - tuple （元组）
# - set(集合）
# - dict（）

# # tuple （元组）
# - 可以理解成一个不允许更改的列表

# In[9]:


# tuple的创建
# 1.直接使用小括号
ta = ()
print(type(ta))

#当用一个小括号创建一个元素的tuple的时候
tb = (100)
print(type(tb))
#加上逗号，
ts = (100,)
print(type(ts))

# 2.直接使用逗号，

ta = 100,
print(type(ta))

# 3. 使用tuple的定义

ta = tuple()
print(ta)



li = [1,2,3,"wangxiaojing"]
tb = tuple(li)  #要求tuple参数可迭代
print(li)
print(tb)


# ### tuple其余特征跟list基本一致
# - 有序
# - 可以访问，不可以被修改
# - 元素可以是任意类型

# In[14]:


# tuple索引操作
la = ["i","love","wangxiaojing",22,33,44,555]
print(la)
ta =  tuple(la)
print(ta[2])


# In[20]:


#tuple的分片操作
print(ta[:])
print(ta[:3])
print(ta[-1:-5:-1])
print(ta[-4::1])


# In[22]:


# 元组的相加
ta = 100,200,300
tb = ("i","love","wangxiaojing")
tc = ta + tb
print(tc)


# In[23]:


# 元组的乘法
tc = ta * 2
print(tc)


# In[26]:


# 元组成员检测

print(tb)
if "wangxiaojing" in tb:
    print("对的")
    
if "wangxiaojing"   not in tb:
    print("错了")


# In[28]:


#元组的遍历


for i in tb:
    print(i)


# In[31]:


# 嵌套元组的访问
# 1. 双层循环访问

ta = ((100,200,300),("i","love","wangxiaojing"),(12,13,14))
for i in ta:
    print(i)
    for j in i:
        print(j)
        
# 2. 单层循环:特殊规定 i，j，k要跟元组个数对应 
for i, j ,k in ta :
    print(i,j,k)


# In[35]:


#常见元组函数
# len：长度
ta = (21,34,5235,654,72254)
print(len(ta))

#max: 最大值

print(max(ta))


# In[38]:


# count:对某一元素进行计数

ta = (1,1,1,1,23,31,32,421,2)
print(ta.count(1))


# In[40]:


#元组的特殊用法
a = 100
b = "dakdadn"

#现在要求对a，b进行互换
#此法是Python的独门笔记
a , b = b , a
print(a)
print(b)


# # 集合（set）
# - 跟数学集合概念一致
# - 内容无序 + 内容不重复
# - 

# In[46]:


# 集合的定义

# 1. 通过set关键字
sa = set()
print(sa)

sb = [1,2,3,4,3,6,7,8,9,10,1,1,1,1,1,1]
li = set(sb)
print(li)

# 2. 使用大括号
sc = {1,2,3,4,3,6,7,8,9,10,1,1,1,1,1,1}
print(sc)


# In[51]:


# in 操作

if 2 in sc :
    print("duid ")
    
for j in sc:
    print(j)


# In[55]:


# 集合的生成式
sa = {1,2,3,4,3,6,7,8,9,10}
# 利用sa 生成一个 sb

sb = {i for i in sa}
print(sb)

sc = { i for i in sa  if i % 2 == 0}
print(sc)

# 双重for 循环
# 1.用一个for
# 把集合里的数平方生成一个新的集合
sd = {i **2 for i in sa }
print(sd)

# 2. 使用两个for

se = {m*n for m in sa  for n in sa}
print(se)


# In[61]:


# 集合的内置函数
# len：长度
print(len(se))

# max /min :最值
# add：向集合里添加元素

sa = {1,2,3,4,3,6,7,8,9,10}
print(sa)
sa.add(11)
print(sa)


# In[66]:


# clear:清除
# remove和 discard的区别
print(sa)
sa.discard(9)
print(sa)
#remove 删除的值如果不在集合中，报错


# In[94]:


# pop弹出集合的一个内容
# 删除的内容是随机的
# 删除内容没啥规律，随机的
sa = {1,2,3,4,5,6,7,8,9}
print(sa)
sa.pop()
print(sa)


# In[102]:


# 集合的数学操作

# intersection：交集
sa = {12,3,4,5,6,7,8,90,9}
sb = {1,2,3,4,5,6,7,8,9}
print(sa.intersection(sb))

# difference:差集
print(sa.difference(sb))
#差集的另一种表达方式
print(sa-sb)

#union:并集  
print(sa.union(sb))
#用加号+计算
#print(sa + sb)   报错


# In[104]:


help(set)


# # frozenset  冰冻集合
# - 不允许修改的集合
# 

# In[2]:


#  案列
sa = {12,3,4,5,6,7,8,90,9}
print(sa)
sb = frozenset(sa)
print(sb)


# # dict 字典
# - 字典是一种组合数据，没有顺序的组合数据，数据以键值形式出现

# In[1]:


# dict 字典的创建
#创建空字典
d = {}
print(d)

d =dict()
print(d)


#创建有值的字典，每一组之间用逗号隔开
d = {"one":1,"two":2,"three":3}
print(d)
#还可以这样创建
#利用关键字参数创建
d = dict({"one":1,"two":2,"three":3})
print(d)

d = dict({("one",1),("two",2),("three",3)})
print(d)


# # 字典的特性
# - 字典是序的类型，但是是无序序列，所以没有分片和索引
# - 字典中的数据每一个都由键值对组成，即kv对
#    - key：必须是可哈希的值，比如int，string，float，tuple。但是list，set，dict不行
#    - value：任何值

# # 字典常见操作

# In[6]:


#访问数据
d = {"one":1,"two":2,"three":3}
#注意访问格式
#中括号内是键值
print(d["one"])

d["one"] = "eins"
print(d)


#删除某个操作
#使用del操作

del d["one"]
print(d)


# In[8]:


# 成员检测： in，not in
d = {"one":1,"two":2,"three":3}

if 2 in d:
    print("value")
    
if "two" in d:
    print("key")
    
if ("two",2) in d:
    print("kv")


# In[14]:


# 遍历
# 按key来使用for循环
d = {"one":1,"two":2,"three":3}
# 使用for循环，直接按key值访问

for k in d:
    print(k, d[k])

#可以改成这样

for k in d.keys():
    print(k, d[k])
    
#只访问字典的值    
for v in d.values():
    print(v)
    
for k,v in d.items():
    print(k,'-----',v)


# # 字典生成式

# In[19]:


d = {"one":1,"two":2,"three":3}

#常规的
dd = {k:v for k,v in d.items()}
print(dd)

#加条件的
dd = {k:v for k,v in d.items() if v % 2 == 0}
print(dd)


# # 字典相关函数

# In[21]:


# 通常函数：len，max，min，dict
#str（字典）： 返回字典的字符串格式
d = {"one":1,"two":2,"three":3}
print(str(d))


# In[23]:


# clear:清空字典
# items：返回字典的键值对组成的元组格式
d = {"one":1,"two":2,"three":3}
i = d.items()
print(type(i))
print(i)


# In[25]:


# keys :返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)


# In[32]:


# get : 根据制定值返回相应的值，好处是可以设置默认值
d = {"one":1,"two":2,"three":3}
print(d.get("on333"))

#get默认值是None，可以设置
print(d.get("one",122))
print(d.get("oneww",122))
#体会以下代码和以下代码的区别

print(d["on333"])


# In[37]:


#fromkeys:使用指定的序列作为键，使用一个值作为字典的所有键的值
l = {"eins","zuhd","dav"}
#注意fromkeys两个参数的类型
#注意fromkeys的调用主体

d = dict.fromkeys(l, "hahaha")
print(d)

