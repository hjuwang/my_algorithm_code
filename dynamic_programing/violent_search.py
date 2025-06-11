# 使用暴力搜索的方法来解 爬楼梯问题

def dfs (i:int) ->int:
    if i==1 or i==2:
        return i
    return dfs(i-1)+dfs(i-2)
    
    
print(dfs(4))    


# 递归树的深度为n 每次广度增加 2 倍，所以时间复杂度为O(2^n)
# 问题是 计算 
# dfs[7]=dfs[6]+dfs[5]
# dfs[8]=dfs[7]+dfs[6]
# 会产生很多重复的计算，所以接下来，改进这个算法，用一个数组记录，已经计算过的值
def rember_search (i:int,rem:list[int]) ->int:
    # 最初值
    if i==1 or i==2:
        return i
    #记忆值
    if rem[i]!=-1:
        return rem[i]
    #递归值并记忆
    count=rember_search(i-1,rem)+rember_search(i-2,rem)
    rem[i]=count
    return count


n=4
rem= [-1]*(n+1)
print(rember_search(n,rem))
