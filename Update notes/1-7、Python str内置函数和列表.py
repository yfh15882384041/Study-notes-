
# coding: utf-8

# # 主要内容
# - str内置函数
# - 列表

# ## str内置函数
# - 字符串查找类：find，index
# - find：查找字符串中是否包含一个子串
# - index:跟find的唯一区别是index如果找不到会引发异常
# - rfind：从右查找，lfind：从左边查找

# In[2]:


help(str.find)


# In[13]:


s = "wo ai wangxiaojing and  zhangxiaojing"
s1 = "xiaojing"
s2 = "sda"
#返回第一次发现这个字符串的位置
s.find(s1,11)

#index 会报错
#s.index(s1)


# In[14]:


help(str.index)


# ### 判断类函数
# - 此类函数的特点是一般都用is开头，比如islower
# - isalpha：判断是否是字母，需要注意的两点：
#   - 前提是字符串至少包含一个字符，如果没有，同样返回False
#   - 汉字被认为是alpha，所以，函数不能作为区分英语字母还是汉字，所以区分要加上Unicode码
#   - 使用时注意区分，
# - isdigit, is numeric, isdecimal 三个判断数字的函数（尽量不用，后期爬虫中，判断数字建议使用正则表达的方式）
# - islower：判断字符串是否为小写
# 

# In[17]:


# 以下三个都不是因为除了字母还有空格
s1 = "大哭大闹，  但看到那肯定"
s2 = "dadkn adndk dadnak "
s3 = " andda   amsdkak  dadka.sadp"

print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())


# ### 内容判断类
# - startswitch、endswitch：是否以cc开头或者结尾
#   - 检查某个字符串是否以某个子开头，常用三个参数
#   - suffix：被检查的字符串，必须有
#   - start：
#   - end：
# - islower/issupper:判断字符串是否小/大写(汉字字符串无大小写概念）

# In[22]:


dana = "liu dana"
xiaojing = "Xiao jing"
s = "liu dana love xiaojing"

print(s.startswith(dana))
print(s.endswith(xiaojing))


# In[25]:


s1 = "KDnkdakd"
s2 = "dladlandadna"
print(s1.islower())
print(s2.islower())


# ### 操作类函数
# - format：格式化用的
# - strip：这个函数的主要作用是删除字符串两边的空格，其实这个函数允许你定义删除字符串两边的哪个字符，只是如果不指定的话默认hi空格。同样lstrip和rstrip从左边和右边删除，默认为空格，需要注意的是，此处的删除不是删除一个，而是删除从头开始符合条件的连续字符。

# In[38]:


c = " DDDDDda dad dada"
#是否成功删除两边空格不能观察出来
print(c)
print(c.strip())
print()
print(c.strip(),end="----")
print()
print(c.strip("a"),end="---")


# # list列表
# - 一组有序数据做成的序列
#   - 数据有先后顺序
#   - 数据可以不是一类数据
# - list的创建：
#   - 直接创建：比如：[1,5dda,2,大户]
#   - 列表包含一个字符串的时候就是一个特例

# In[45]:


#list创建的特例演示

s = "dada"
#打印只包含s的一个字符串列表
l = list(s)

print(type(l))
print(l)


# # 内置函数
# - help：帮助函数
# - type：显示变量的类型
# - id;显示变量的id
# - print

# # 列表的常见操作
# - 访问
#   - 使用下标操作，也叫作索引 
#   - 列表的元素索引是从0开始的
# - 切片操作
#   - 对列表进行任意一段的截取[数字：数字],[ : ]:全列表,[ : 数字]： 从头开始到数字。
#   - 截取之后，创建一个新的列表

# In[50]:


L1 = [31,312,443,52,41]
#使用下标访问
print(L1[0])


# In[55]:


#切片操作需要注意取值范围，左包括右边不包括

L1 = [1,2,3,4,5,6,7,8,9,10]
#对比打印结果

print(L1[3:6])
print(L1[ :6])
print(L1[ : ])


# In[59]:


# 分片可以控制增长幅度，默认增长幅度为1
print(L1[ ::1])#等价于print(L1[ : ])
print(L1[ ::3])


# In[61]:


#下标可以超出范围，超出后不再考虑多余下标内容
print(L1[ :100])


# In[71]:


#下标值，增长幅度可以为负值
#下标为负值，表明顺序是从右往左
#规定：数组最后一个数字的下标是-1


#下面例子为空，因为默认是从左向右移动
print(L1[-2:-5])

#打印9,8,7
print(L1[-2:-5:-1])


#打印7,8,9
print(L1[-4:-1:1])


# # 关于列表的函数

# In[8]:


#append 插入一个内容 注意是在末尾

l = ['a',"i love   wangxiaoli",22,33,4+3j]

print(l)
print("*"  * 20)
a =[i for i in range(1,5)]
print(a)
a.append(100)
print(a)


# In[17]:


#  insert  制定位置插入
# insert（index，data） 插入位置是index前面


a.insert(1,2333)
print(a)


# In[22]:


#删除
#del
#pop，从对位拿出一个元素，即把最后一个元素取出来
b =[i for i in range(1,10)]
print(b)
tsg = b.pop()
print(tsg)
print(b)


# In[27]:


# remove   删除制定的元素
#如果list上没有指定元素，就会报错，
# 所以应该先进行try。。。expect语句，或者现行判断
# if x in list：
#########      list.remove(x)
print(b)
b.remove(7)
print(b)


# In[29]:


#clear:清除
print(b)
print(id(b))
b.clear()
print(b)
print(id(b))

# 如果 不需要list地址不变，只是清空list可以使用以下方式
# a = list()
# a =[]


# In[31]:


# reverse:  原地翻转，地址不变

a = [1,2,3,4,5,6,7,8,9]
print(a)
a.reverse()
print(a)


# In[33]:


#extend：延长列表

a =[1,2,3,4,5]
b =[6,7,8,9]
a.extend(b)
print(a)


# In[35]:


# count:  查找列表中指定值或者元素的个数
print(a)
a.append(5)
print(a)
a.insert(6,5)
print(a)

hh = a.count(5)
print(hh)


# In[39]:



a = [1,3,4,5,6,7,8,9,10]
b = a

b[3] = 989779
print(b)
print(a)
#list 变量赋值操作，是传地址操作
print("*"*30)
#为了让a 的值不变，，，采用copy :拷贝，浅拷贝
b =a.copy()
print(a)
print(id(a))
print(b)
print(id(b))
print("*"*30)

b[4] =100000
print(a)
print(b)


# In[43]:


# 深拷贝与浅拷贝的区别

a =[1,2,3,[44,55,66,33]]
c =a.copy()
print(id(a))
print(id(c))
print("*"*20)
print(id(a[3]))
print(id(c[3]))
print("*"*20)
a[3][2] =7777
print(a)
print(c)
#以上就是浅拷贝


# 
# 
# 

# In[44]:




