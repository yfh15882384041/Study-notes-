
# coding: utf-8

# # 文件
# - 长久保存信息的一种数据信息集合
# - 常规操作：
#   - 打开关闭（文件一旦打开，需要关闭操作）
#   - 读写内容
#   - 查找
# # open 函数
# - open函数负责打开文件，带有很多参数
# - 第一个参数： 必须有，文件的路径和名称
# - mode： 表明文件用什么方式打开
#   - r： 只以读方式打开
#   - w： 写方式打开，会覆盖以前的内容
#   - x： 创建方式打开，如文件已经存在，会报错
#   - a： append方式，以追加的方式对文件内容进行写入
#   - r： 文本方式打开
#   - +： 可读写

# In[4]:


# 打开文件，用写的方式
# f称之为文件句柄
# r表示后面字符串内容不需要转义
f = open(r"test01.txt","w")
f.close()

#此案例说明，以写方式打开文件，默认如果没有文件，则创建


# # with 语句
# - with语句使用的技术是一种成为上下文管理协议的技术（ContexManagementProtocal)
# - 自动判断文件的 作用域，自动关闭不在使用的文件句柄

# In[8]:


#with 语句 案列
with open(r"test01.txt","r") as f:
    pass
    #下面语句块开始对文件 f 进行操作
    #在本模块中不需要使用close关闭文件 f


# In[18]:


# with 案列
with open(r"test01.txt","r") as f:
    # 按 行 读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件知道结束
    while strline:
        print(strline)
        strline = f.readline()


# In[17]:


# read 是按字符读取文件内容
#允许输入参数决定读取几个字符，如果没有制定，从当从位置读取到结尾
# 否则，从当前位置读取指定个数字符
with open(r"test01.txt","r") as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)


# # seek(offset,from)
# - 移动文件的读取位置，也叫读取指针
# - from的取值范围：
#   - 0 ：从文件头开始偏移
#   - 1 ：从文件当前位置开始偏移
#   - 2 ：从文件末尾开始偏移
#   
# - 移动的单位是字节（byte）
# - 一个汉字由若干个字节构成
# - 返回文件只针对 当前位置

# In[19]:


# seek案列
#打开文件后，从第五个字节开始读取
# 打开读写指针在0 处，即文件的开头
with open(r"test01.txt","r") as f:
    # seek移动单位是字节
    f.seek(6, 0)
    strChar = f.read()
    print(strChar)


# In[20]:


# 关于读取文件的练习
# 打开文件，三个字符一组读取出内容，然后显示在屏幕上
# 每读一次，休息一秒钟

# 让程序暂停，可以使用time下的sleep函数
import time
with open(r"test01.txt","r") as f:
    # read 参数是字符，可以理解成一个汉字是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        #sleep 参数单位是秒
        time.sleep(1)
        strChar = f.read(3)


# In[21]:


# tell函数： 用来显示文件读取指针的当前位置
with open(r"test01.txt","r") as f:
    strChar = f.read(3)
    pos = f.tell()
     
    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()
#以上结果说明
#tell的返回数字的单位是byte
#read的是以字符为单位


# # 文件的写操作   write
# - write（str）：把字符串写入文件
# - writelines（str）：把字符串按行写入文件
# - 区别：
#   - write函数参数只能是字符串
#   - writelines函数参数可以是字符串，也可以是字符序列

# In[26]:


# write案列
# 1.想文件追加一句诗
# a 代表追加方式打开
with open(r"test01.txt","w") as f:
    # 注意字符串内含有换行符
    f.write("生活不仅有眼前的苟且， \n  还有远方的苟且")


# In[25]:


# 可以直接写入行，用writelines
with open(r"test01.txt","w") as f:
    f.writelines("生活不仅有眼前的苟且")
    f.writelines("还有远方的苟且")


# In[27]:


l = ["i","love","wangxiaojing"]

# a代表追加方式打开
with open(r"test01.txt","w") as f:
    # 注意字符串内含有换行符
    f.writelines(l)


# # 持久化- pickle
# - 序列化（持久化，落地）： 把程序运行中的信息保存在磁盘上
# - 反序列化： 序列号的逆过程
# - pickle：Python提供的序列化模块
# - pickle.dump:序列化
# - pickle.load: 反序列化

# In[29]:


#序列化案列1
import pickle

age = 19

with open(r"test02.txt","wb") as f:
    pickle.dump(age,f)


# In[31]:


#反序列化案列1
import pickle
with open(r"test02.txt","rb") as f:
    age = pickle.load(f)
    print(age)


# In[33]:


#序列化案列2
import pickle

a = [19,'liudadak','dada','ddqwq',[123,64]]

with open(r"test02.txt","wb") as f:
    pickle.dump(a,f)


# In[34]:


#反序列化案列2
import pickle
with open(r"test02.txt","rb") as f:
    a = pickle.load(f)
    print(a)


# # 持久化 shelve
# - 持久化工具
# - 类似字典， 用kv对保存数据，存取方式跟字典因为类似
# - open，close

# In[35]:


# 使用shelve 创建文件并使用
import shelve
#打开文件
#shv相当于一个字典
shv = shelve.open(r'shv.db')

shv['one'] = 1
shv['two'] = 2
shv['three'] = 3

shv.close()
#通过以上案列发现，shelve自动创建的不仅仅是shv.db文件，还包括其他格式文件


# In[41]:


# shelve 读取案列
shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['two'])
    print(shv['three'])
    print(shv['threefff'])
    
except Exception as e:
    print("有错误")
    

finally:
    shv.close()


# # shelve 特性
# - 不支持多个应用并行写入
#   - 为了解决这个问题，open的时候可以使用flag=r
# - 写回答问题：
#   - shelve恶魔人情况下不会等待持久化对象进行任何修改
#   - 解决方案： 强制写回，writeback= Ture

# In[42]:


# shelve     读写打开
import shelve

shv = shelve.open(r'shv.db',flag='r')

try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()


# In[48]:


import shelve

shv = shelve.open(r'shv.db')

try:
    shv['one'] = {"eins":1, "zwei":2, "drei":3} 
finally:
    shv.close()
    
    
shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()    


# In[52]:


# shelve 忘记写会，需要使用强制写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    #此时，一旦shelve关闭，则内容还是存于内存中，没有写回数据库
    k1["eins"] = 1000
    
finally:
    shv.close()
    
shv = shelve.open(r'shv.db')
try:
    k2 = shv['one']
    print(k2)
    
    
finally:
    shv.close()


# In[58]:


# shelve 忘记写会，需要使用强制写回
shv = shelve.open(r'shv.db',writeback=True)
try:
    k1 = shv['one']
    print(k1)
    #此时，一旦shelve关闭，则内容还是存于内存中，没有写回数据库
    k1["eins"] = 100
    
finally:
    shv.close()
    
shv = shelve.open(r'shv.db')
try:
    k2 = shv['one']
    print(k2)
    
    
finally:
    shv.close()


# In[59]:


# shelve 使用with管理上下文环境
with shelve.open(r'shv.db',writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    k1["eins"] = 1000
    
with shelve.open(r'shv.db') as shv:
    print(shv['one'])

