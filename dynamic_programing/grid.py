

def grid_min_cost(n:int,m:int,cost:list[list[int]])->int:
    #初始化dp表 dp[i][j] 表示走到[i][j]位置的最小开销
    #dp[i][j]=min(dp[i-1][j],dp[j-1][i])+cost[i][j]
    
    dp=[[0]*m for _ in range(n)]
    
    #初始化最小状态
    dp[0][0]=cost[0][0]
    #首行
    for j in range(1,m):
        dp[0][j]=dp[0][j-1]+cost[0][j]
        

    #首列
    for i in range(1,n):
        dp[i][0]=dp[i-1][0]+cost[i][0]
    #状态转移
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+cost[i][j]
            
    return dp[n-1][m-1]


# 将这个函数进行空间优化，使用单行dp表,表示某一行的状态
def grid_min_cost2(n:int,m:int,cost:list[list[int]])->int:
    #初始化dp表示某行第几列的最小开销
    
    dp=[0]*m
    
    #初始化最小状态
    dp[0]=cost[0][0]
    #首行(从第0行开始初始化)
    for j in range(1,m):
        dp[j]=dp[j-1]+cost[0][j]
        
      
    #在循环中更新每一行的值(时间复杂度并没有优化)
    for i in range(1,n):
        dp[0]+=cost[i][0]
        for j in range(1,m):
            dp[j]=min(dp[j-1],dp[j])+cost[i][j]
            
    return dp[m-1]


#test 
cost = [
    [1,3,1,5],
    [2,2,4,2],
    [5,3,2,1],
    [4,3,5,2]
    
]


print(grid_min_cost(n=len(cost),m=len(cost[0]),cost=cost))
print(grid_min_cost2(n=len(cost),m=len(cost[0]),cost=cost))
        