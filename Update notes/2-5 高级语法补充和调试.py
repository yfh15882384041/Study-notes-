
# coding: utf-8

# # 补充几个高级函数
# ## zip
# - 把两个可迭代的内容生成一个可迭代的tuple元素类型组成的内容

# In[2]:


# zip案列
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]

z = zip(l1, l2)
print(type(z))
print(z)

for i in z:
    print(i)


# In[3]:


l1 = ["wangwang","lili","yfh"]
l2 = [96, 56, 60]
z = zip(l1, l2)
for i in z:
    print(i)


# # enumerate
# - 跟zip很像
# - 对可迭代对象的每一个元素，配上一个索引，然后索引和内容构成tuple类型

# In[4]:


l1 = [11,22,33,44,55]
em = enumerate(l1)
l2 = [i for i in em]
print(l2)


# In[5]:


em = enumerate(l1, start=100)
l2 = [i for i in em]
print(l2)


# # collection 模块
# - namedtuple
# - deque

# ### nametuple
# - tuple类型
# - 是一个可命名的tuple

# In[10]:


import collections
help(collections.namedtuple)


# In[20]:


import collections
point = collections.namedtuple("point",['x','y'])
p = point(11,22)
print(p.x)
print(p[1])
print(p)


# In[22]:


import collections
Circle = collections.namedtuple("Circle",['x','y','r'])
c = Circle(100,150,50)
print(c)
print(type(c))
# 想检测一下namedtuple到底属于谁的子类
isinstance(c, tuple)


# # dequeue
# - 比较方便的解决了频繁删除插入帮助带来的效率问题

# In[27]:


from collections import deque
q = deque(['a','b','c'])
print(q)

q.append("d")
print(q)

q.appendleft("v")
print(q)


# # defaultdict
# - 当直接读取不存在的属性时，直接返回默认值

# In[32]:


d1 = {"one":1, "two":2, "three":3}
print(d1["one"])


# In[37]:


help(defaultdict)


# In[40]:


from collections import defaultdict
# lambda表达式： 直接返回字符串
func = lambda:"刘大拿"
d2 = defaultdict(func)
d2["one"] = 1
d2["teo"] = 2
d2["three"] = 3

print(d2["one"])
print(d2["four"])


# # Counter
# - 统计字符串个数

# In[41]:


help(collections.Counter)


# In[43]:


from collections import Counter
c = Counter("dakdasdadadadafefrfvsvsvv")
print(c)
# 以上结果不是把dakdasdadadadafefrfvsvsvv当做键值，而是把其中每一个字母作为键值
# 需要括号里面的内容为可迭代的


# In[44]:


s = ["liudana", "love", "love", "love", "love", "wangxiaojing"]
c = Counter(s)
print(c)


# # 调试技术
# - 调试流程： 单元测试 > 集成测试  > 交 测试部
# - 分类： 
#   - 静态调试：
#   - 动态调试：
# ### pdb调试
# - 推荐文章
#   - 【官方网页（英文）】（https://docs.python.org/2/library/pdb.html)
#   - 【pdb模块介绍】：百度
#   - 【pdb调试技巧】：百度
#   - 【pdb详细中文介绍】：百度
#   - 【调试案列1】：https://www.cnblogs.com/dkblog/archive/2010/12/07/19800682
#   - 【调试案列2】：https://python.jobbloe.com/81184
# - pdb:python 调试库
# 
# - pychram 调试
# - run/debug模式：
#   - 断点：程序的某一行，程序造debug模式下，遇到断点
#  
# ### 单元测试
# - 推荐文章：
#   - 【官方测试文档集合】：https://wiki.python.org/moin/PythonTestingToolsTaxon
