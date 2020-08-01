
# coding: utf-8

# # 异常
# - 广义上的错误分为错误和异常
# - 错误指的是可以人为避免
# - 异常是指在语法逻辑正确的前提下，出现的问题
# - 在python里 ，异常时一个类，可以处理和使用

# # 异常的分类
# - 语法错误，类型错误等
# - 百度有点多
# 
# 
# 

# # 异常处理
# - 不能保证程序永远正确运行
# - 但是，必须保证程序在最坏的情况下得到问题的妥善处理
# - Python的异常处理模块全部语法为：
# 
#            try:
#                尝试实现某个操作
#                如果没有出现异常，任务就可完成
#                如果出现异常，将异常从当前代码扔出去尝试解决异常
#            except  异常类型1 ：
#              解决方案1：用于尝试在此处理异常解决问题
#              
#            except  异常类型2 ：
#              解决方案2：用于尝试在此处理异常解决问题
#            
#            except (异常类型1,异常类型2)
#              解决方案：针对多个异常使用相同的处理方式
#              
#            except：
#              解决方案：所有异常的解决方案
#              
#            else：
#              如果没有出现任何异常，将会执行此处的代码
#              
#            finally：
#              管你有没有异常都要执行的代码
#              
# - 流程：
#     
#       1.执行try下面的语句
#       2.如果出现异常，则在except语句里查找对应异常进行处理
#       3.如果没有出现异常，则执行else语句的内容
#       4.最后，不管是否出现异常，都要执行finally语句
#   - 除except（最少一个）以外，else和finally可选

# In[1]:


#简单的异常处理1

try: 
    num = int(input("Plz input your number: "))
    rst = 100/num
    print("计算结果是: {0}".format(rst))
except:
    print("你输入的是什么？？，，输入不能为0")
    
    #exit是推出程序的意思
    exit()


# In[1]:


# 简单异常处理案列2
# 给出提示消息
try: 
    num = int(input("Plz input your number: "))
    rst = 100/num
    print("计算结果是: {0}".format(rst))
# 异常捕获后，把异常实例化，出错信息在实例里
# 注意一下写法：
# 一下语句是捕获ZeroDivisionError异常并实例化案列e
except ZeroDivisionError  as e:
    print("你输入的是什么？？，，输入不能为0")
    print(e)
    #exit是推出程序的意思
    exit()


# In[2]:


# 简单异常处理案列2
# 给出提示消息
try: 
    num = int(input("Plz input your number: "))
    rst = 100/num
    prnit("计算结果是: {0}".format(rst))#这里故意将print打错
# 异常捕获后，把异常实例化，出错信息在实例里
# 注意一下写法：
# 出现多种error的情况
# 在异常类继承关系中，越是子类的异常，越要往前放
# 越是父亲类的异常，越要往后放
#在处理异常的时候，一旦拦截到某一异常，则不在继续往下查，直接进行下一个
# 代码，即有finally则执行finally语句块，否则就执行下一个大的语句
except ZeroDivisionError  as e:
    print("你输入的是什么？？，，输入不能为0")
    print(e)
    #exit是推出程序的意思
    exit()
    
except NameError  as e:
    print("名字错误")
    print(e)
    exit()
    
except AttributeError  as e:
    print("属性错误")
    print(e)
    exit()
# 所有异常都是继承来自Exception
# 如果写在上下面这句话，任何异常都会拦截住
# 而且，下面这句话一定是最后一个Exception
except Exception  as e:
    print("我也不知道问题出在哪了")
    print(e)
    exit()
#下面这句话 就不会执行了   
except ValueError  as e:
    print("No>>>>>>>>>>")
    
print("*"*30)    
print("我是照常运行的")


# # 用户手动引发异常
# - 当某些情况，用户希望自己引发一个异常的时候，可以使用
# - raise 关键词来引发异常

# In[5]:


# raise案列1

try:
    print("我爱python")
    print(3.1541215)
    #手动引发一个异常
    #注意语法： raise  ErrorClassName
    raise ValueError
    print("还没完哎呀")
    
except NameError as e:
    print("NameError")
    print(e)
except ValueError as e: 
    print("ValueError")
    print(e)
except Exception as e:
    print("有异常")
    print(e)
    
finally :
    print("我肯定会被执行")


# In[13]:


# raise案列1
# 自己定义异常
#   需要注意： 自定义异常必须是系统异常的子类
class DanaError(ValueError):
    pass
    
try:
    print("我爱python")
    print(3.1541215)
    #手动引发一个异常
    #注意语法： raise  ErrorClassName
    raise DanaError
    print("还没完哎呀")
    
except NameError as e:
    print("NameError")
    print(e)
except ValueError as e: 
    print("DanaError")
    print(e)
except Exception as e:
    print("有异常")
    print(e)    
finally :
    print("我肯定会被执行")
    


# In[18]:


# else 语句案列
try: 
    num = int(input("Plz input your number: "))
    rst = 100/num
    print("计算结果是: {0}".format(rst))
    
except Exception as e:
    print("Excepttion")
else:
    print("No Excepttion")
    
finally:
    print("我肯定会被执行")


# # 关于自定义异常
# - 只要raise异常，则推荐自定义异常
# - 在自定义异常的时候，一般包含以下内容
#   - 自定义发生异常的异常代码
#   - 自定义发生异常后的问题提示
#   - 自定义发生异常的行数
# - 最终的目的是，一旦发生异常，方便程序员快速定位错误现场
