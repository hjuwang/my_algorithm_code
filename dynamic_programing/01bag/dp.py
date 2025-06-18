# 使用动态规划的方式来解决这个问题 
# dp[i][c] 记录为放入前i 个物品后在cap 为c 容量的背包中的最大价值

# 状态转移的过程，就是决策是不是要放第 i 个物品
# 1 不放的话，dp[i][c] = dp[i-1][c]
# 2 放的话，  dp[i][c] = dp[i-1][c-wgt[i-1]]+val[i-1]
# 求二者中的最大值

def bag_max_value(val:list[int],wgt:list[int],cap :int)->int:
    # 初始化dp 表
    n = len(val)
    dp = [[0]* (cap+1) for _ in range(n+1)]
    
    #初始值 第一行都是0（不放任何物品，价值为0），第一列都是0 （背包的容量为0,背包不能放下任何东西）
    
    #开始状态转移
    for i in range(1,n+1):
        for c in range(1,cap+1):
            # 如果第i 个物品超出容量,则不放
            if wgt[i-1] > c:
                dp[i][c]=dp[i-1][c]
            else:
                dp[i][c]=max(
                    dp[i-1][c],
                    dp[i-1][c-wgt[i-1]]+val[i-1]
                )    
            
    return dp[n][cap]


wgt = [10,20,30,40,50]
val=[50,120,150,210,240]

res= bag_max_value(val,wgt,50)

print(res)
  
            