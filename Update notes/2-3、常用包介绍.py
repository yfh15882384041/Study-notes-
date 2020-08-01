
# coding: utf-8

# # 常用模块
# - calendar   日历
# - time      时间
# - datetime
# - timeit
# - os
# - shutil
# - zip
# - math
# - string
# - 上述所有模块使用理论上都应该先导入，string是特例

# # calendar 日历
# - 跟日历相关的模块

# In[2]:


#使用前先导入
import calendar


# In[7]:


# calendar： 获取一年的日历字符串
#参数
# w = 每个日期之前的间隔字符串
# t = 每周所占用的行数
# c = 每个月之间的间隔字符串
cal = calendar.calendar(2020)
print(type(cal))
print(cal)


# In[8]:


cal = calendar.calendar(2020,l=0,c=5)
print(type(cal))
print(cal)


# In[10]:


# isleap: 判断某一年是否是闰年
calendar.isleap(2020)


# In[12]:


# leapdays: 获取指定年份之间的闰年个数
calendar.leapdays(2010,2020)


# In[14]:


help(calendar.leapdays)


# In[16]:


# month()  获取某个月的日历字符串
# 格式： calendar。month(年，月)
# 回值：月日历的字符串
m3 = calendar.month(2020,7)
print(m3)


# In[3]:


# monthrange()  获取一个月的周几开始和天数
# 格式：calendar。onthrange(年，月)
# 回值： 元组（周几开始，总天数）
# 注意： 周默认 0-6 表示周一到周天
help(calendar.monthrange(2020,7))
w,t = calendar.monthrange(2020,7)
print(w)
print(t)


# In[7]:


# monthcalendar()  返回一个月每天的矩阵列表
# 格式： calendar.monthcalendar（年，月）
# 回值：二级列表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2020,8)
print(type(m))
print(m)


# In[10]:


# prcal : print calendar 直接打印日历
calendar.prcal(2020)
help(calendar.prcal)


# In[14]:


# promonth()   直接打印整个月的日历
# 格式：calendar.prmonth(年，月)
#返回值 ： 无
calendar.prmonth(2020,9)


# In[19]:


# weekday()   获取周几 周一到周日对应 0 - 6
# 格式： calendar.weekday(年，月，日)
# 返回值： 周几对应的数字
calendar.weekday(2020,7,27)


# # time模块
# ### 时间戳
#       - 一个时间表示，根据不同语言，可以试着整数或者是浮点数
#       - 是从1970年到现在
#       - 如果时间是在1970年以前或者太远，肯能出现错误
#       - 32位操作系统能够支持到2030年
#       
#       
# ### UTC时间
#       - UTC又称为世界协调时间，以英国的格林威治地区的时间作为参考，也叫世界标准时间
#       - 中国时间是UTC+8  东八区
#       
# ### 夏令时
#       - 夏令时就是在夏天的时候将时间调快一个小时，本意是督促大家早睡早起省蜡烛，每天变成25个小时，本质没变还是24个小时
#       
#       
# ### 时间元组
#       - 一个包时间内容的普通元组
#       
#       索引      内容       属性       值
#       
#       0         年       tm_year     2015
#       1         月       tm_month     1-12
#       2         日       tm_mday      1-31 
#       3         时       tm_hour      0-23
#       4         分       tm_min       0-59
#       5         秒       tm_sec      0-61  60表示闰秒  61保留值
#       6         周几     tm_wday      0-6
#       7         第几天    tm_yday     1-366
#       8         夏令时    tm_isdst     0,1，-1（表示夏令时）

# In[5]:


# 需要单独导入
import time


# In[24]:


# 时间模块的属性
# timezone： 当前时区和UTC时间差的秒数，在没有夏令时的情况下的间隔，东八区是   -28800
# altzone   获取当时时区与UTC时间相差的秒数，在有夏令时的情况下
#daylight   测当前是否是夏令时时间状态  ，0   表示是

print(time.timezone)
print(time.daylight)


# In[26]:


#  得到时间戳

time.time()


# In[29]:


#   测当前时间
# 可以通过点操作符得到相应的属性元素的内容
t = time.localtime()
print(t.tm_min)
print(t)


# In[31]:


# asctime()   返回元组的正常字符串化之后的时间格式
# 格式： time.asctime(时间元组)
#  返回值： 字符串 Tue  Jun  6  11:11:00  2017
t = time.localtime()
tt = time.asctime(t)
print(type(tt))
print(tt)


# In[32]:


# mktime()  使用时间元组获取对应的时间戳
# 格式： time.mktime(时间元组)
# 返回值： 浮点数时间戳

aa = time.localtime()
ss = time.mktime(aa)
print(type(ss))
print(ss)


# In[ ]:


# clock   获取cpu时间    3.0-3.3 版本直接使用   3.6 调用有问题


# In[35]:


# sleep：  是程序进入睡眠   n秒后继续
for i in range(10):
    print(i)
    time.sleep(1)


# In[37]:


#
def p():
    time.sleep(2.5)
    
t1 = time.clock()
print(t1)
p()
t2 = time.clock()
print(t2)
print("*"*39)
print(t1-t2)


# In[8]:


# strftime:  将时间元组转化为自定义的字符串格式
'''
百度  太多了   难得打
'''
# 把时间表示成     2020 年7月27日   17:35
t = time.localtime()
print(t)
tt = time.strftime("%Y 年 %m 月 %d 日  %H:%M",t)
print(tt)


# # datetime 模块
# - datetime模块提供日期和时间的运算和表示
# -

# In[1]:


import datetime


# In[3]:


# datetime 常见属性
# datetime。date()： 一个理想和的日期，提供year，month，day属性

dt = datetime.date(2020,7,28)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)

#datetime.time: 提供一个理想和的时间，居于hour，minute，sec，microsec等
#datetime.datetime： 提供日期跟时间的组合
#datetime.timedelta： 提供一个时间差，时间长度


# In[4]:


#datetime.datetime： 提供日期跟时间的组合
from datetime import datetime
# 常用方法：
#today()：
#now()：
#utcnow
#fromtimestamp： 从时间戳中返回本地时间

dt = datetime(2020,7,28)
print(dt.today())
print(dt.now())


# In[14]:


#  datetime.timedelta
#  表示一个时间间隔
from datetime import datetime, timedelta

t1 = datetime.now()
print(t1.strftime("%Y-%m-%d  %H:%M:%S"))
print(t1)
print("*"*30)
#  t2表示以小时的时间长度
t2 = timedelta(hours=1)
print((t1+t2).strftime("%Y-%m-%d  %H:%M:%S"))


# In[16]:


# timeit: 时间测量工具

#测量程序运行时间间隔实验


def p():
    time.sleep(3)
    
t1 = time.time()
p()
t2 = time.time()
print(t2 - t1)


# In[14]:


import timeit
def c():
    num = 3
    for i in range(num):
        pass
      
    
# 生成列表的两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
# 利用timeit调用代码，执行100000次，查看运行时间
t1 = timeit.timeit(stmt="[i for i in range(1000)]",number=100000)

# 测量代码c执行100000次运行结果
t = timeit.timeit(stmt=c,number=100000)

print(t1)
print(t)


# In[8]:


help(timeit.timeit)


# In[15]:


# timeit   可以执行一个函数，来测量一个函数的执行时间

def do():
    num = 3
    for i in range(num):
        print("repeat for {}".format(i))
        
# 代码执行10次

t = timeit.timeit(stmt=do,number=10)
print(t)


# In[16]:


s = '''
def do(num):
    num = 3
    for i in range(num):
        print("repeat for {}".format(i))

'''

# 执行do(num)
# setup负责把环境变量准备好
# 实际相当于给timeit创造一个小环境
# 在创作的小环境中，代码执行的顺序大致是
#
'''
def do(num):
    ....
    
num =3

do(num)
'''
t1 = timeit.timeit(stmt="do(num)",setup=s+"num=3",number=10)
print(t1)


# # datetime.datetime 模块
# - 提供比较好用的时间而已
# - 类定义
# 
#        class datetime.datetime(year,month,day[,huor
#               [,minute
#               [,second
#               [,microsecnd
#               [,tzinfo]]]]])
#               
#        # the year  month and day   argument  are  required.
#        MINYEAR <= year <= MAXYEAR
#        1 <= month <= 12
#        1 <= day  <= n
#        0 <= hour <= 24
#        0  <= minute <= 60
#        0 <= second <= 60
#        0 <= microsecond <= 10**
# - 类方法 
#      -   使用手上有

# In[17]:


from datetime import datetime as  dt
print(dt.now())


# # os - 操作系统相关
# - 跟操作系统相关，主要是文件操作
# - 于系统相关的操作系统，主要包括在三个模块里
#   - os，操作系统目录相关
#   - os.path   系统路径相关操作
#   - shutit   高级文件操作，目录树的操作，文件赋值，删除，移动。
# - 路径：
#   - 绝对路径： 总是从根目录上开始
#   - 相对路径： 基本以当前环境为开始的一个相对的地方
#   

# # os 模块

# In[19]:


import os
# getcwd()   获取当前的工作目录
# 格式： os.getcwd()
#返回值： 当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
mydir = os.getcwd()
print(mydir)


# In[20]:


# chdir   改变当前的工作目录
# change directory
# 格式： os.chdir(路径)
#  返回值： 无

os.chdir('/home/tlxy')#  t填个正确的路径即可
mydir = os.getcwd()
print(mydir)


# In[22]:


# listdir   获取一个目录中国所有字目录和文件的名称列表
# 格式： os.listdir(路径)
# 返回值： 所有子目录额文件名称的列表
h = os.listdir()
print(h)


# In[23]:


# makedirs()   递归创建文件夹
# 格式： os.makedirs(递归路径)
# 返回值： 无
#  递归路径： 多个文件夹层包含的路径就是递归路径    例如 a/b/c...
rst = os.makedirs("danna")

print(rst)


# In[25]:


# system()   运行系统shell命令
#格式：   os.system(系统命令)
# 返回值： 打开一个shell或者终端界面
# 一般推荐使用subprocess代替
# ls是列出当前文件和文件夹的系统命令
rst = os.system("ls")
print(rst)


# In[30]:


# getenv()    获取指定的系统环境变量值
# 相应的还有putenv
# 格式： os.getenv("环境变量名")
# 返回值: 指定环境变量名对应的值
gg = os.getenv("PATH")
print(gg)

print("*"*40)
for i in os.getenv("PATH"):
    print(i)


# In[ ]:


# exit()     推出当前值
# 格式： exit()
# 返回值： 无


# # 值部分  
# - os.curdir: 当前目录
# - os.pardir:父亲目录
# - os.sep： 当前系统的路径分隔符
#   - Windows："\"
#   - linux:"/"
# - os.linesep：当前系统的换行符
#   - Windows："\r\n"
#   -  linux:,macos,unix:"\n"
#       
# - os.name：当前系统名称
#   - Windows： nt
#   - mac，unix，Linux： posix

# In[32]:


print(os.pardir)
print(os.curdir)


# In[34]:


print(os.sep)
print(os.linesep)


# In[ ]:


# 在路径相关的操作中，不要手动拼写地址，因为手动拼写的路径可能不具有移植性


# In[37]:


#windows系统名称是posix
print(os.name)

