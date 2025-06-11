#汉诺塔问题
# 首先定义三个列表，表示三个汉诺塔
# 要求在任意时刻，每一个列表中的数据，都是从大到小排列的
# 要求将 A 数组中的所有数据转移到 C 数组中


# 定义一个移动函数

def move(src:list[int],target:list[int]):
    target.append(src.pop())
    
    
# 将src 中的 n 个圆盘放到 target 中   
def hannuo_solve(n:int,src:list[int],buf:list[int],target:list[int]):
    # 如果 n==1
    if n==1:
        move(src,target)
        return 
    # 使用分治的思想,将顶层的n-1 个圆盘，移动到buf,利用target

    hannuo_solve(n-1,src,target,buf)
    # 将第n个圆盘移动到 target
    move(src,target)
    # 将 buf 中的n-1个圆盘移动到 target
    hannuo_solve(n-1,buf,src,target)
    
    
A=[3,1]
B=[]
C=[]

hannuo_solve(len(A),A,B,C)

print(A)   
print(B)   
print(C)   

#  时间复杂度分析
# 首先分析该算法的递归树的层数是 n 层，每层要计算的数据成指数式增长
# 所以时间复杂度 是 1+2+4+...2^(n-1)= 2^n-1 所以时间复杂度是O(2^n)
