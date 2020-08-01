
# coding: utf-8

# # 递归函数
# - 递归：函数间接或直接调用自己
# - 递归分为两个过程：
#   - 往下调用，分解的过程
#   - 往上回溯，综合的过程
# - 递归需要注意：
#   - 一定要有结束条件
# - 是以资源换取编写速度（并不是处理速度快）

# In[2]:


def fune(n):
    print("i love wangxiaojing")
    
def funb(n):
    fune(100)
    print("w jiao liudana")

funb(100)


# In[6]:


#阶乘
# 利用数学公式

def fun_a(n):
    print(n)
    if n == 1:
        return 1
    return n * fun_a(n - 1)


a = fun_a(5)
print("fun_a(5) =",a)
    


# In[9]:


# 递归必须要有结束条件，否则会死掉

def fun_b(n):
    print(n)

    return n * fun_b(n - 1)

fun_b(100)
    


# In[1]:


# 斐波那契数列
# 1,1 2,3,5,8,13.。。。
# f(n) = f(n-1) + f(n-2)，n>=3 ,f(n) = 1 n=1,2

def fun_c(n):
 
    if n ==1 or n == 2:
        return 1
    return fun_c(n - 1) + fun_c(n - 2)

fun_c(10)


# In[2]:


# 斐波那契数列
# 1,1 2,3,5,8,13.。。。
# f(n) = f(n-1) + f(n-2)，n>=3 ,f(n) = 1 n=1,2

def fun_c(n):
 
    if n ==1 or n == 2:
        return 1
    return fun_c(n - 1) + fun_c(n - 2)

fun_c(10)


# In[19]:


# 汉诺塔
# 递归
a = "A"
b = "B"
c = "C"
def yidong(a,b,c,n):
    if n == 1:
        print("{}-->{}".format(a,c))
        return None
    if n == 2:
        print("{}-->{}".format(a,c))
        print("{}-->{}".format(a,b))
        print("{}-->{}".format(b,c))
        return None
        
    
    yidong(a,c,b,n-1)# 把a借助c移动n-1个到b的过程打印出来
    print("{}-->{}".format(a,c))# 把最大的盘子移到c
    yidong(b,a,c,n-1)
   


yidong(a,b,c,1)
print()
yidong(a,b,c,2)
print()
yidong(a,b,c,3)
print()
yidong(a,b,c,4)

    
    

