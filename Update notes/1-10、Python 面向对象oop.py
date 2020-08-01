
# coding: utf-8

# # 面向对象 OOP
# - 思想：
#   - 以模块化的思想解决工程问题
#   - 面向过程 vs 面向对象 
#   - 由面向过程转向面向对象
#   - 列子：我要开一个学校，叫轻易学院，主要讲少儿编程：
#     - 讲师
#     - 学生
#     - 班主任
#     - 教师
#     - 学校
# - 常用名词：
#   - oo: 面向对象
#   - ooa： 分析
#   - ood：设计
#   - oop ：编程
#   - ool：实现
#   - ooa -> ood -> ool
#   
# - 类 vs 对象
#   - 类：抽象，描述的是一个集合，测重于共性
#   - 对象：具体的，描述的是一个个体
#   
# - 类的内容：
#   - 动作：函数
#   - 属性：变量
#   
# - is-a
# 
# - 定义类：class关键字
# - 类命名：
#   - 遵循大驼峰
#   - 第一个字母大写
#   

# In[2]:


# 定义学生类，和几个学生

class Student():
    ## 此处定义一个空类
    ## pass是关键词，表示占位用的无意义。
    pass


# In[3]:


class StudentNoPass():
    pass


# In[4]:


# 定义一个对象

xiaomig = Student()


# # 类的属性
# - 类的例子
# - 注意类的定义

# In[3]:


class PythonStudent():
    name = "yfh"
    age = 22
    course = "python"

    #定义类中的函数
    #一般需要self关键字
    #其余跟普通函数基本相同

    
    def giveMeMoney(self):
        print("haahahahha")
        return None

# self可以更换名称
    def sayhi(nana):
        print("哈喽")
        return None
    
xiaobai =  PythonStudent()
print(xiaobai.age)
print(xiaobai.name)
print(xiaobai.course)


# 
# 
# 

# In[14]:


# 实例化
#中文能否当做变量名称  ：   可以但是不建议使用
二娃 = Student()
print(二娃)


# #  self 
# - self可以用别的名称代替
# - self不是关键字
# - 作用是指代本身

# In[17]:


# self实例
# 实例调用

yaoyao = PythonStudent()

# 调用的时候居然没有输入参数
#因为默认实例（这里就是yaoyao）作为第一个参数
yaoyao.giveMeMoney()
yaoyao.sayhi()


# # 类的变量作用域的问题
# - 类变量：属于类自己的变量
# - 实例变量：属于实例的变量
# - 访问实例的属性，如果实例没有定义，则自动访问类的属性；如果类也没有定义就报错。

# In[23]:


class Student():
    
    #name、age、course是类（这里是self）的变量
    #注意类的变量的定义位置和方法
    #不需要前缀
    name = "马德拉"
    age = 18
    course = "python"

    #定义类中的函数
    #一般需要self关键字
    #其余跟普通函数基本相同




    def sayhi(self):
        print("我的名字是{},今年{},在学习{}课程".format(self.name ,self.age ,self.course))
        
        return None
    
#以下案例说明，实例变量可以借用类的变量

erjing = Student()
erjing.sayhi()
       
    


# In[6]:


class Student1():
    
    #name、age、course是类（这里是self）的变量
    #注意类的变量的定义位置和方法
    #不需要前缀
    name = "马德拉"
    age = 18
    course = "python"

    #定义类中的函数
    #一般需要self关键字
    #其余跟普通函数基本相同




    def sayhi(self,n,a,b):
        self.name = n
        self.age = a
        self.course = b
        print("我的名字是{},今年{},在学习{}课程".format(self.name ,self.age ,self.course))
        
        return None
    
#以下案例说明，实例变量可以借用类的变量

erjing = Student1()
erjing.sayhi("erjing",17,"shuxue")
print("我的名字是{},今年{},在学习{}课程".format(Student1.name ,Student1.age ,Student1.course))
print("我的名字是{},今年{},在学习{}课程".format(erjing.name ,erjing.age ,erjing.course))
# 如果访问实例的属性没有定义，则自动访问类的属性
# e如果类也没定义就报错


# # 访问类的属性
# - 在类里面如果强制访问类的属性，则需要使用用(__class__)(注意是两个下划线）
# - 类方法：
#   - 定义类的方法的时候，没有self参数
#   - 类的方法中只允许使用类的内容
#   - 两种用法：
#     - ClassName
#     - (__class__)
# 

# In[16]:


class Student3():
    
    #name、age、course是类（这里是self）的变量
    #注意类的变量的定义位置和方法
    #不需要前缀
    name = "马德拉"
    age = 18
    course = "python"

    #定义类中的函数
    #一般需要self关键字
    #其余跟普通函数基本相同




    def sayhi(self):

        print("我的名字是{},今年{},在学习{}课程".format(self.name ,self.age ,self.course))
        
        return None
    
    # sos:是类的方法
    # 如何访问类的变量
    #但是调用需要用到特殊的方法
    def sos():
        #类的方法中不允许实例的任何内容
        # 如果要访问类的内容，注意两种用法: 直接用类的名称；用__class__.
        print("我的名字是{},今年{},在学习{}课程".format(Student3.name ,__class__.age ,Student3.course))
        return None
    
# 体验类的方法
s = Student3()
s.sayhi()
# 调用绑定类方法的例子
Student3.sos()


# # 构造函数
# - 实例化的时候，执行一些基础性的初始化的工作
# - 使用特殊的名称和写法
# - 在实例化的时候自动执行
# - 是实例化的时候第一个默认被执行的函数
# - 要求：第一个参数必须有，一般推荐self
# - 一般不手动调用，实例化的时候自动调用，参数需写类名称后面的括号中
# 

# In[21]:


# 注意类的定义
 
class Student4():
    name = "yfh"
    age = 23
    
    # 构造函数名称固定，写法相对简单
    def __init__(self):
        print("我是构造函数")
    

ni = Student4()#此时已经调用构造函数了
print("___________---")
print(ni.name)
print(ni.age)


# In[42]:


#实例

class Person():
    def __init__(self,name,age):
        print(name,age)
        
p = Person("张三",22)


# In[11]:


class A():
    name = "yfh"
    age = 22
    
    def __init__(self):
        print("我是构造函数")
        self.name = "aaaaa"
        self.age = 220
        
    def hh(self):
        print(self.name)
        print(self.age)
        
        
class B():
    name = "bbbbb"
    age = 30
    
a = A()
print("*" * 20)
#系统会默认把a作为第一个参数传入函数
a.hh()
print(a.name)
print(a.age)
print(A.name)
print(A.age)
print("*" * 20)
#此时self被a替换
A.hh(B)


# # 面向对象的三大特征
# - 继承
# - 封装
# - 多态
# 

# # 继承
# - 子类可以使用父类定义的内容或者行为等
# - 继承的实现；
#   - 父类：基类，超类，被继承的类  Baste class  super class
#   - 子类：有继承行为的类
#   
#   - 所有类必须有一个父类
#    - 如果没有 ，则默认是object的子类
#    - 子类可以有多个父类
#   
# - 继承的特征
#   - 所有的类都能继承自object类，即所有的类都是object类的子类
#   - 子类一旦能继承父类，即可以使用父类中除私有成员外的所有内容
#   - 子类能继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
#   - 子类中可以定义独有的成员属性和方法
#   - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
#   - 子类如果想扩充父类的方法，可以在定义新方法的同时，访问父类成员来进行代码重用，可以使用  父类名.父类成员 的格式来调用父类成员，也可以使用 super（）.父类成员 的格式来调用
# - 继承变量函数的查找顺序问题
#   - 优先查找自己的变量
#   - 没有则查找父类
#   - 构造函数如果在本类中没有定义，则自动查找调用父类构造函数
#   - 如果本类有定义，则不再向上查找
# - super
#   - super不是关键字，而是一个类
#   - super的作用是获取MRO列表中的第一个类
#   - super于父类没有直接的实质性关系，但是通过super可以调用到父类。
# - 单继承与多继承
#   - 单继承：每个类只能继承一个类
#   - 多继承:每个类允许继承多个类
#   - 优缺点：
#     - 单继承：
#       - 优点：传承有序逻辑清晰语法简单隐患少
#       - 缺点：功能不能无限扩展，只能在当前唯一的继承链中扩展
#     - 多继承：
#       - 优点：类的功能扩展方便
#       - 缺点：继承关系混乱
# - 菱形继承/钻石继承问题
#   - 多个子类继承同一个父类，这些子类由被同一个类继承，于是继承关系图形成一个菱形图谱
#   - MRO(http://www.cnblogs.com/whatisfantasy/p/6946991.html)
#   - 关于多继承的MRO
#     - MRO就是多继承，用于保存继承顺序的一个列表
#     - Python本身采用C3算法来多继承的菱形继承进行计算的结果
#     - MRO列表的计算原则：
#       - 子类永远在父类前面
#       - 如果多个父类，则根据多继承语法中括号中类的书写顺序存放
#       - 如果多个类继承同一个父类，则孙子类中只会选取继承语法括号中第一个父类的父类
#     

# In[22]:


# 所有类必须有一个父类
# 默认是object的子类
class Person1():
    pass

class Person2(object):
    pass


# In[24]:


class Person3():
    name = "nana"
    age = 22
    
    
    #父类写在类定义的时候的括号里
class Teacher(Person3):
    pass
  
a = Teacher()
print(a.age)


# In[28]:


class Bird():
    fly = "YES.WE CAN"
    def fiying(self):
        print("okokokok")
        
        
class BirdMan(Person3,Bird):
    pass


fm = BirdMan()
fm.fiying()
print(fm.name)
print(fm.age)


# In[33]:


# 说明super
help(super)


# In[36]:


#多继承案列
#子类可以直接拥有父类的属性，私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("i am swimming")
        
class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("i am fiying")
        
class Person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("在工作中")
        
class Superman(Person,Bird,Fish):
    def __init__(self,name):
        self.name = name

s = Superman("yueyue")
s.work()
s.swim()
s.fly()


# In[2]:


# 菱形继承问题
class A():
    pass 
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(D.__mro__)
print(C.__mro__)


# ##  issubclass 检测是否是子类
# - 可以用来检测两个类的父子关系

# In[35]:


# 利用刚才定义的Bird，BirdMan，Person3，Teacher，检测父子关系

# 从第二个和第三个可以看出，正确写法为  子在前 ，父在后
print(issubclass(BirdMan,Bird))
print(issubclass(BirdMan,Person3))
print(issubclass(Person3,BirdMan))
print(issubclass(Teacher,Person3))


# # 构造函数的继承
# - 构造函数默认继承
# - 一旦子类定义了构造函数，则不能自动调用父类构造函数
# - 如果没有定义，则自动查找父类构造函数
# - 如果子类没有定义，父类的构造函数带参数，则构造对象时的参数应该按父类参数构造
# 
# 

# In[13]:


# 构造函数默认继承
class Person11():
    def __init__(self,name,age):
        print("person是{},{}".format(name,age))
class Teacher11(Person11):
    pass

t =  Teacher11("刘大拿",22)


# In[32]:


#super的使用案例
class A():
    pass
class B(A):
    pass

print(A.__mro__)
print(B.__mro__)


# # 封装
# - 封装就是对对象的成员进行访问限制
# - 封装的三个级别
#   - 公开 public
#   - 受保护的 protected
#   - 私有的 private
#   - public，protected，private不是关键字
# - 判别对象的位置
#   - 对象内部
#   - 对象外部
#   - 子类中
#   
# - 私有 private（Python的私有不是真的私有，是一种成为name  mangling 的改名策略，可以使用对象_classname_attributename访问）
#   - 私有成员是最高级别的封装，只能在当前类或对象中访问
#   - 在成员呢前面添加两个下划线即可
#   
# - 受保护的封装  protected
#   - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者子类中都可以访问，但是在外部不可以
#   - 封装方法： 在成员名称前加一个下划线即可
#   
# - 公开的 public
#   - 公共的封装实际对成员没有任何操作，任何地方都可以访问

# In[11]:


#  私有变量案列

class Person():
    #  name是共有的成员
    name = "sda"
    # __age就是私有成员
    __age = 55
    
p = Person()
#name是公有变量
print(p.name)
#age是私有变量
#注意报错信息
#print(p.__age)
# name mangling技术

print(Person.__dict__)

print("*"*30)
print(p._Person__age)


# In[2]:





# In[18]:


class Person33():
    name = "noname"
    age = 22
    __score = 0
    __petname = "sec"  #小明是受保护的，子类可以用，但是不能公用
    
    def asd(self):
        print("我在休息中。。。。")
        
class Teacher(Person33):
    name = "asdsa"
    def zxc(self):
        pass
    
h = Person33()
print(h.name)
print("*" * 30)
print(Teacher.age)
### 如何访问私有变量
print(Person33.__dict__)
print(h._Person33__score)
print(h._Person33__petname)


# In[28]:


# 子类扩充父类功能案列
# 人由工作的函数，老师也由工作的函数，但是老师的工作需要讲课
class Person33():
    name = "noname"
    age = 22
    __score = 0
    __petname = "sec"  #小明是受保护的，子类可以用，但是不能公用
    
    def work(self):
        print("上班中。。。。")
        
class Teacher(Person33):
    teacher_id = "51244"
    name = "王大"
    def make_test(self):
        print("我在挣钱")
    def work(self):
        #扩充父类的功能只需要调用父类相应的函数
        #Person33.work(self)
        #扩充的另一种方法
        #super代表得到父类
        super().work()
        self.make_test()
t = Teacher()
t.work()
t.make_test()


# # 多态
# - 多态就是同一个对象在不用情况下有不同的状态出现
# - 多态不是语法，是一种设计思路
# - 多态性：一种调用方式，不同执行的效果
# - 多态：同一事物的多种形态，动物分为人类，狗类等
# - 文章：(http://www.cnblogs.com/luchuangao/p/6739557.html)
# - Mixin设计模式
#   - 主要采用多继承方式对类的功能进行扩张
#   - Mixin的概念
#   - MRO与mixin
#   - Mixin模式
#   - Mixin MRO
#   - MRO
# - 我们使用多继承语法来实现Mixin
# - 使用ixin实现多继承的时候要多加小心
#   - 首先他必须表示某一单一功能，而不是某个物品
#   - 职责必须单一，如果由多个功能，则写多个Mixin
#   - Mixin不能依赖于子类的实现
#   - 子类及时没有继承这个Mixin类，也能照样工作，只是缺少了某个功能。
# - 优点：
#   - 使用Mixin可以在不对类进行任何修改的情况下，扩充功能。
#   - 可以方便的组织和维护不同功能类的组合。
#   - 可以根据需要任意调整功能类的组合。
#   - 可以避免创建很多新的类，导致类的继承混乱。
#   
#   
# - 类相关函数
#   - issubclass：检测一个类是否是另一个类的子类。
#   - isinstance：检测一个对象是否是一个类的实例。。
#   - hasattr：检测一个对象是否由xxx
#   - getattr：get attribute
#   - setattr：set attribute
#   - delattr：delete attribute
#   - dir：获取对象的成员列表
#  
#  ###
# - 类的成员描述符(属性）
#   - 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
#     - get:获取属性的操作
#     - set：修改或者添加属性操作
#     - delete：删除属性的操作
#     
# - 如果想使用类的成员描述符，大概有三种方法
#   - 使用类实现描述器
#   - 使用属性修改符
#   - 使用property函数：
#     - property函数很简单
#     - property（fget，fset，fdel，doc）
# 
# - 无论哪种修饰符都是为了对成员属性进行相应的控制
#   - 类的方式： 适合多个类中的多个属性共用一个描述符
#   - property: 使用当前类中使用，可以控制一个类中多个属性
#   - 属性修饰符：使用与当前类中使用，控制一个类中的一个属性
#  
# ###  
# - 类的内置属性
#   - __dict__:以字典的方式显示类的成员组成
#   - __doc__:获取类的文档信息
#   - __name__:获取类的名称，如果模式中使用，获取模块的名称
#   - __bases__: 获取某个类的所有父类，以元组的方式显示
#   
# ###
# - 类的常用魔法方法
#   - 魔法方法就是不需要人为调用，基本是在特定的时刻自动触发
#     - 魔术方法的同意特征，方法名被前后两个下滑线包裹
#     - 构造函数：__init__   直接触发
#     - __new__: 此函数特殊，一般不需要使用
#     - __call__: 对象当函数使用的时候触发
#     - __str__: 当对象被当做字符串使用的时候
#     - __repr__: 返回字符串，跟‘__str__'具体区别可以百度
#   - 描述符相关：
#     - __set__
#     - __get__
#     - __delete__
#   - 属性操作相关
#     - __getattr__: 访问一个不存在的属性时触发
#     - __setsttr__: 对成员属性进行设置的时候触发
#       - 参数：
#         - self用来获取当前对象
#         - 被设置的属性名称，以字符串形式出现
#         - 需要对属性名称设置的值
#       - 作用： 进行属性设置的时候进行验证或者修改
#       - 注意：在该方法中不能对属性直接赋值操作，否则死循环
#     
#   - 运算分类相关魔法函数方法
#     - __gt__ ：进行大于判断的时候触发的函数
#     - 参数：
#       - self
#       - 第二个参数是第二个对象
#       - 返回值可以任意值，推荐返回布尔值
#       
# ###
# - 类和对象的三种方法
#   - 实例方法
#     - 需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他对象的方法完成
#   - 静态方法
#     - 不需要实例化，通过类直接访问
#   - 类方法
#     - 不需要实例化
#     - 具体区别百度
#     
#     
# ### 
# - 抽象类
#   - 抽象方法： 没有具体实现内容的方法成为抽象方法
#   - 抽象方法的主要意义是规范子类的行为和接口
#   - 抽象类的使用需要借助abc模块
#   -     import abc
#   - 抽象类：包括抽象方法的类叫抽象类，通常成为ABC类
# - 抽象类的使用：
#   - 抽象类可以包括抽象方法，也可以包括具体方法
#   - 抽象类中可以有方法也可以有属性
#   - 抽象类中不允许直接实例化
#   - 必须继承才可以使用，且继承的子类必须实现所有继承来的抽象方法
#   - 假定子类没有是现实所有继承的抽象方法，则子类也不能实例化
#   - 抽象类的主要作用是设定类的标准，以便开发的时候具有统一的规范
#   
# ###
# - 自定义类
#   - 类其实是一个类定义和各种方法的自由组合
#   - 可以定义类和函数，然后自己通过类直接赋值
#   - 可以借助于MethodType实现
#   - 借助于type实现
#   - 利用元类实现 Metaclass
#     - 元类是类
#     - 备用来创造别的类

# In[26]:


# 属性案列
# 创建Student类，描述学生类
# 学生具有Student.name 属性
# 但是name格式并不同意
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name)
    def intro(self):
        print("hai,my name is {0}".format(self.name))
    
    def setName(self, name):
        self.name = name.upper()
        
s1 = Student("YFH",22)
s2 = Student("xx",21)

s1.intro()
s2.intro()


# In[3]:


#property案列
#对于任意输入的姓名，我们希望都用大写保存
# 年龄用整数保存
#  x = property（fget，fset，fdel，doc）

class Person():
    #函数名可以任意
    def fget(self):   #功能是：对变量进行读取操作的时候应该执行的函数功能
        return self._name * 3
    
    def fset(self,name):   #模拟对变量进行写操作的时候进行的功能
        self._name = name.upper()
        
    def fdel(self):     # fdel模拟的是删除变量的时候进行的操作
        self._name = "noname"
        
        
    name = property(fget,fset,fdel)
        
p1 = Person()
p1.name = "TndnakUInnknkna"
print(p1.name)


# In[19]:


#将输入的浮点数  输出整数

class Person11():
    
    '''
    但是肯定把可大大大健康查看大师课打开擦擦可参考ckak
    '''
    #函数名可以任意
    def fget(self):
        return self._age 
    
    def fset(self,age):
        self._age = int(age)
        
    def fdel(self):
        self._age = "no age"
        
        
    age = property(fget,fset,fdel)
        
p2 = Person11()
p2.age = 21.23545
print(p2.age)


# In[14]:


int(2.3355)


# In[23]:


# 类的内置属性
print(Person11.__dict__)
print(Person11.__doc__)
print(Person11.__name__)
print(Person11.__bases__)


# In[28]:


#魔法函数 实例化方法
class A():
    def __init__(self):
        print("我是构造函数")
        
    def __call__(self):
        print("我被调用了")
    
    def __str__(self):
        return "哈哈哈"
        
        
a = A()  # 构造函数__init__  直接触发
a()  #  __call__: 对象当函数使用的时候触发
print(a)#  __str__: 当对象被当做字符串使用的时候


# In[35]:


#__getattr__ 案列

class A():
    name = "noname"
    age = 22
    
    def __getattr__(self,hhhh):
        print("haadadka ")
        print(hhhh)
        
b = A()
print(b.name)
print("*"*30)
print(b.addr)   #访问一个不存在的属性时触发


# In[13]:


#   __setsttr__: 对成员属性进行设置的时候触发

class Person():
    def __init__(self):
        pass
    
    def __setattr__(self,name,value): 
        print("设置属性：{0}".format(name))
        #下面会导致死循环
        #self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name,value)
p = Person()
print(p.__dict__)
p.age = 21


# In[18]:


# __gt__案列  进行大于判断的时候触发的函数

class Student():
    def __init__(self,name):
        self._name = name
        
    def __gt__(self,kk):
        print("哈哈哈，{0}会比{1}大吗？？".format(self,kk))
        return self._name > kk._name
    
stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)


# In[30]:


#  类和对象的三种方法

class Person():
    #实例方法
    def eat(self):
        print(self)
        print("Eating....")
        
    # 类方法
    #类方法的第一个参数，一般命名为cls，区别于self
    @classmethod    # 类似一个声明
    def paly(cls):
        print(cls)
        print("palying...")
        
    #静态方法
    #不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("saying...")
        
yueyue = Person()
yueyue.eat()   #实例方法

Person.paly()   #类方法
yueyue.paly()

Person.say()    #静态方法
yueyue.say()


# In[36]:


# 变量的三种方法

class A():
    def __init__(self):
        self.name = "haha"
        self.age = 33
        
a = A()
print(a.name)
a.name
# 属性的三种方法
# 1、赋值
# 2、读取
# 3、删除
a.name = "刘大拿"
print(a.name)
del a.name


# In[1]:


# 类属性 property
#应用场景
# 对变量除了普通的三种操作，还想增加一些附加的操作，那么可以通过property完成
class A():
    def __init__(self):
        self.name = "haha"
        self.age = 22
        
    def fget(self):    #功能是：对变量进行读取操作的时候应该执行的函数功能
        print("我被读取了")
        return self.name
    
    def fset(self, name):   #模拟对变量进行写操作的时候进行的功能
        print("我被写入了")
        self.name = "xxx学院"  + name 
        
    def fdel(self):   # fdel模拟的是删除变量的时候进行的操作
        pass
    
    name2 = property(fget, fset, fdel, "这是一个property的例子")
        
pp = A()
pp.name2 = "刘大拿"
print(pp.name2)


# In[5]:


# 抽象   
class Aanmel():
    def sayhai(self):
        pass
    
class Dog(Aanmel):
    def sayhai(self):
        print("闻了闻对方的味道")
    
class Person(Aanmel):
    def sayhai(self):
        print("kiss you")
        
d = Dog()
d.sayhai()
print("*" * 30)
p = Person()
p.sayhai()


# In[13]:


#  抽象类的实现

import abc

# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    
    #定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass
    
    #定义类的抽象方法
    @abc.abstractclassmethod
    def drink(self):
        pass
    
    
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def paly(self):
        pass


# In[17]:


# 函数名可以当变量使用
def sayhello(name):
    print("你好{},晚上有空吗".format(name))
    
sayhello("yueyue")
print("$$"*20)
kkkk = sayhello
kkkk("月月")


# In[19]:


#自己组装一个类

class A():
    pass
def say(self):
    print("saying....")
    
class B():
    def say(self):
        print("saying....")  
    
say(8)
print("$$"*20)
A.say = say
a = A()
a.say()
print("$$"*20)
b = B()
b.say()


# In[21]:


#  自己组装类的例子
from types import MethodType

class A():
    pass
def say(self):
    print("saying....")
    
a = A()
a.say = MethodType(say , A)
a.say()


# In[24]:


help(MethodType)


# In[60]:


#利用type造一个函数
# 先定义类应该具有的成员函数

def say(self):
    print("saying...")
    
def hi(self):
    print("talking...")
    
#利用type来创建一个类

A = type("AName",(object,  ),{"class_say":say, "calss_hi":hi})

#然后就可以像正常一样使用类
a = A()
a.class_say()


# In[66]:


# 元类演示

# 元类写法是固定的 ，塔必须是继承type
#元类一般命名以MetaClass结尾
class TulingMetaClss(type):
    #注意一下写法
    def __new__(cls,name,bases,attrs):
        #自己的业务处理
        print("哈哈，我是一个元类")
        attrs['id'] = '0001'
        attrs['addr'] = "北京海淀区"
        return type.__new__(cls,name,bases,attrs)
    
#元类定义完就可以使用，使用注意写法

class Taecher(object,metaclass=TulingMetaClss):
    pass

t = Taecher()
print(t.id)
print(t.addr)


# In[68]:




