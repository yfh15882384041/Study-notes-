
# coding: utf-8

# # 模块
# - 一个模块就是一个包含pytho代码的文件，后缀名是.py  模块就是个python文件
# - 为什么我们要用模块
#   - 程序太大，编写维护非常不方便，需要拆分
#   - 模块可以增加代码重复利用的方式
#   - 当做命名空间使用，避免命名冲突
# - 如何定义模块
#   - 模块就是一个普通文件，所有任何代码可以直接书写
#   - 不过根据模块的规范，最好在模块中编写以下内容
#     - 函数：单一功能
#     - 类：相关功能的组合，或者类似业务模块
#     - 测试代码
# - 如何使用模块
#   - 模块直接导入
#     - 加入模块名称直接以数字开头，需要借助importlib帮助
#   - 语法
#     - import module_name(也就是文件名）
#     - module_name.function_name
#     - module_name.class_name
#     - 案列：p01.py，p02.py ,01.py
#    
#   - import 模块 as 别名
#     - 导入的同时给模块起一个别名
#     - 其余用法跟一种相同
#     - 案列p03.py
#     
#   - from module_name import func_name, class_name
#     - 上述方法是有选择性的导入
#     - 使用的时候可以直接导入的内容，不需要前缀
#     - 案列p04.py
#     
#   - from module_name import *
#     - 导入模块所有内容
#     - 案列p05.py
#     
#   - if __name__ == "__main__"的使用
#     - 可以有效避免模块代码被导入的时候被动执行的问题
#     - 建议所有程序的入口都已此代码为入口
#     
# ### 
# - 模块的搜索路径和储存
#   - 什么是模块的搜索路径
#     - 加载模块的时候，系统会在那些地方寻找此模块
# - 系统默认的模块搜索路径
#   - import sys
#   - sys.path  属性可以获取路径列表
# - 添加搜索路径
#   - sys.path.append(dir)
# - 模块的加载顺序
#   - 1.上搜索内存中已经加载好的模块
#   - 2.搜索Python的内置模块
#   - 3.搜索sys.path路径
# 
# 
# ### 
# - 包 : 是一种组织管理代码的方式，包里面存放的是模块。
#   - 用于将模块包含在一起的文件就是包
#   - 自定义包的结构：
#            
#            /、、、包
#            /、、、/、、、__init__.py  包的标志文件
#            /、、、/、、、模块1
#            /、、、/、、、模块2
#            /、、、/、、、字包（子文件）
#            /、、、/、、、/、、、__init__.py  包的标志文件
#            /、、、/、、、/、、、子包模块1
#            /、、、/、、、/、、、子包模块2
#  
# - 包的导入操作 
#   - import package_name
#     - 直接导入一个包，可以使用__init__.py中的内容
#     - 使用方法是：
#              
#              package_name.func_name
#              package_name.class_name.func_name()
#     - 此种方式的访问内容是
#     - 案列 pkg01，p07.py
#   - import package_name as p
#     - 具体用法跟作用方式，跟上述简单导入一致
#     - 注意的是此种方法是默认对__init__.py内容的导入
#   - import package.module
#     - 导入包中某个具体的模块
#     - 使用方法
#     
#            package.module.func_name
#            package.module.class.fun()
#            package.module.class.var
#     - 看案列p08.py文件
#   - import package.module as pm
#     - 同上述不在做说明
# - from ... import 导入
#   - from package import module
#   - 此种导入方法不执行__init__的内容
#   
#           from pkg01 import p01
#           p01.say()
#   - from package import *
#     - 导入当前包"__init__.py"文件中所有的函数和类
#     - 使用方法
#     
#             func_name()
#             class_name.func_name()
#             class_name.var
#     - 案列p09.py文件
# - from package.module import *
#   - 导入包中指定的模块的所有内容
#   - 使用方法：
#   
#              func_name()
#              class_name.func_name()
#              
# - 在开发环境中经常会用到其他模块，可以在当前包中直接导入其他模块中的内容
#   - import 完整的包或者模块的路径
# - "__all__"的用法
#   - 在使用from package import *的时候  *可以导入的内容
#   - "__init__.py"中如果文件为空，或者没有"__all__"    那么只把"__init__"中的内容
#   - __init__ 如果设置了 __all__ 的值，那么则按照 __all__ 指定的字包或者模块进行，如此则不会载入 __init__ 中的内容
#   - __all__=["module1", "module2","package1".....]
#   
# ###
# - 命名空间
# - 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
# - 作用是防止命名冲突
#       
#          setname()
#          Student.setname()
#          Dog.setname()

# In[2]:


# 定义一个类
# 一个sayhello函数
#一个打印语句
#p01.py文件
class Student():
    def __init__(self,name="yfh",age=22):
        self.name = name
        self.age = age
        
    def say(self):
        print("你的名字是[0],年龄{1}".format(name,age))
        
def kk(self):
    print("欢迎你")

#此判断语句建议一直作为程序的入口   编程习惯
if __name__ ==  "__main__":    
    print("我是p01.py文件")    
# 假设以上代码组成一个.py的文件名称为p01    我要在另一个文件中使用  




#  操作如下.py文件中的代码
#本文件命名为p02.py
import p01

stu = p01.Student("xiaojing",22)
stu.say()
stu.kk()

# 当加入模块名称直接以数字开头  例如  01.py，需要借助importlib帮助
#如下：
import importlib
tuling = importlib.import_module("01")  #相当于导入了一个叫01的模块并把导入模块赋值给了tuling
stu = tuling.Student()
stu.say()


# In[3]:


#import 模块 as 别名
#将本文件命名为p03.py
import p01 as p
stu = p.Student("yueyue",18)
stu.say()


# In[4]:


#from module_name import func_name, class_name案列
#上述方法是有选择性的导入
#使用的时候可以直接导入的内容，不需要前缀
from p01 import Student
stu.Student()
say()


# In[1]:


#from module_name import *  案列
from module_name import *
say()

stu = Student("yueyu",21)
stu.say()


# In[4]:


#案列p06.py

import sys
for p in sys.path:
    print(p)


# In[5]:


#  包
# 定义一个文件名为：__init__.py  内容如下：
def inInit():
    print("我是一个包")


#import package.module的使用案列
#案列 pkg01，p07.py
import pkg01.p01

stu = pkg01.p01.Student()
stu.say()


# In[ ]:


#案列
#下面文件为p08.py
__all__=["p01"]

def inInt():
    print("dada")
    
#下面文件为p09.py
from pkg02 import *

stu = p01.Student()
stu.say()

