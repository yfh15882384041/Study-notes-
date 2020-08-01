
# coding: utf-8

# # str字符串
# - str
# - 转义字符
# - 格式化
# - 内建函数
# 

# # 字符串
# - 表示文字信息
# - 用单引号，双引号，三引号括起来

# In[1]:


s = 'hahahahhahahah'
print(s)


# In[2]:


s = "hahhahhahahah"
print(s)


# In[4]:


s = """hahhaha
ha
h
ah
aha"""
print(s)


# # 转义字符
# - 用一个特色的方法表示出一系列不方便写出的内容，不如回车键换行符
# - 借助反斜字符，一旦字符串出现反斜杠，则反斜杠后面一个或者几个字符表示已经不是以前的意思了，进行了转义
# - 在字符串里，一旦出现反斜杠就要加倍小心，可能有转义字符出现
# - 不同系统对换行操作有不同的表示
#   - windows： \n
#   - linux:  \r\n

# In[12]:


#转义字符案列
#想表达let'go

#使用双引号嵌套
s = "let's go"
print(s)
#但是我用单引号的话
a = 'let\'s go'
print(a)

#输出反斜杠\:即用\\输出一个\
#比如：C:\User\dadanank
s = "C:\\User\\dadanank；"
print(s)

#回车换行\n
#想表达的效果是：
#aha
#jdoado
#djaodjao
s = "aha\njdoado\ndjaodjao"
print(s)


# # 格式化
# - 把字符串按照一定的格式进行打印或者填充
# - 格式化的分类：
#   - 传统格式使用%
#   - format

# # 利用%百分号格式化（传统方法）
# 
# - 在字符串中，利用%表示一个特殊的含义，表示对字符进行格式化
# - %d: 此处应该放入一个整数
# - %s: 表示此处应该放入一个字符串
# 

# In[15]:


#  %s    表示简单的字符串
#占位符可以单独使用
s = " i love %s"
print(s)

print(s%"yfh")


# In[18]:


print("i love %s"%"yfh")
#一般占位符只能被同类型替换
print("i love %s"%110)


# In[21]:


s = "今年%d岁"
print(s%22)


# In[29]:


# 如果出现多个占位符，则相应内容需要用括号括起来

s = "今年%d岁,叫%s名字,体重%.2f斤"
print(s)
print(s%(22,"yfh",64.6))


# # format 格式化
# - 使用函数进行格式化，代替以前的%

# In[41]:


#不用指定位置，按顺序读取

#方式1
s = "{},{}"
print(s.format("hello","world"))


#方式2
s = "{},{}".format("hello","world")
print(s)

#设定制定位置
s = "{1},{0}".format("hello","world")
print(s)

s = "{0},{1}".format("hello","world")
print(s)

#下面案列报错
#s = "{},{}".format("hello")
print(s)

#使用命名参数
s = "我们的学校{shool_name},我们的简称是{id},{who}最帅"
s = s.format(shool_name="四川轻化工大学",id="USUE",who="我")
print(s)


# In[46]:


#通过字典设置参数，需要解包**
#使用命名参数
s = "我们的学校{shool_name},我们的简称是{id},{who}最帅"

s_dict = {"shool_name":"四川轻化工大学","id":"USUE","who":"我"}

s = s.format(**s_dict)#解包操作
print(s)


# In[1]:


#对数字的格式化需要用到的
s = "今年高{:.2f},体重{:.4f}斤"
print(s)
print(s.format(1.74,64.54))


# # str内置函数
# - 很多语言字符串使用string，但是Python使用str表示字符串

# In[2]:


help(str)

