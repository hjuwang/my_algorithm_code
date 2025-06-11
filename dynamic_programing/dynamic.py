# 动态规划的思想，是从底至顶的解决问题
# 不实用递归，使用循环的办法来解决

def dyna_pro(i:int)->int:
   
    dp=[-1]*(i+1)
    dp[1],dp[2]=1,2
    for i in range(3,i+1):
        dp[i]=dp[i-1]+dp[i-2]
        
    return dp[i]

print(dyna_pro(3))               
print(dyna_pro(4))   



# 对这个算法进行空间优化
# 通过观察发现,我们要求的最后的结果i和i-1,i-2 成递进关系
def dyna_pro(i:int)->int:
   
    if i==1 or i==2:
        return i
    a,b=1,2
    for i in range(3,b+1):
        a,b =b, a+b
        
    return             