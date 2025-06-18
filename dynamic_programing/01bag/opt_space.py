# 动态规划的空间优化，将二维数组优化成一纬数组
# dp[c] 表示最大价值，只需要将 物品遍历完毕即可


def bag_max_value(val:list[int],wgt:list[int],cap :int)->int:
    # 初始化dp 表
    n = len(val)
    dp = [0]* (cap+1) 
    
    #初始值 第一行都是0（不放任何物品，价值为0），第一列都是0 （背包的容量为0,背包不能放下任何东西）
    
    #开始状态转移
    for i in range(1,n+1):
        for c in range(cap,0,-1):
            # 如果第i 个物品超出容量,则不放
            if wgt[i-1] > c:
                dp[c]=dp[c]
            else:
                dp[c]=max(
                    dp[c],
                    dp[c-wgt[i-1]] + val[i-1]
                )    
            
    return dp[cap]


wgt = [10,20,30,40,50]
val=[50,120,150,210,240]

res= bag_max_value(val,wgt,50)

print(res)
