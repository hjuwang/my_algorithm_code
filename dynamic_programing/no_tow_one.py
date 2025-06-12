# 爬楼梯问题,不能连续的上1个台阶
def climb_stairs(n:int):
    
    #初始化dp数组存储结果
    dp = [[0]*3 for _ in range(n+1)]
    
    #初始值
    # dp[1][1]表示爬到第一个楼梯且最后一步爬一层
    dp[1][1],dp[1][2]= 1,0
    # dp[1][1]表示爬到第一个楼梯且最后一步爬一层说明第一次也是爬一层，但是这不符合条件，所以是0
    dp[2][1],dp[2][2]=0,1
    
    for i in range(3,n+1):
        dp[i][1]=dp[i-1][2] 
        dp[i][2]=dp[i-2][1]+dp[i-2][2]
        
    return dp[n][1]+dp[n][2] 


# 这种算法不符合无后效性

print(climb_stairs(3))  
