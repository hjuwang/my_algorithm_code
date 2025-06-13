
# 01 背包问题
'''

第i 个物品的容量为wgt[i-1]，价值为val[i-1]
求将这些物品放入容量为cap的背包中,获得的物品的最大价值



使用dp[i][c] 表示决策到第 i 个物品时，在容量为c 的背包中可以获得的最大价值

假设总共有 n 个物品
所以dp = (n+1)(cap+1)

当决策到 第 i个物品的时候，有一下两种情况：

- 1,不放 dp[i][c]= dp[i-1][c]
- 2,放入 dp[i][c]=dp[i-c][c-wgt[i]]+val(i-1)
 求二者中的最大值
'''

def bag_max_value(wgt:list[int],val:list[int],i:int,c:int)->int:
    #已经选完所有的物品，且背包没有剩余容量
    if i==0 or c==0:
        return 0
    # 方不下第i 个物品，那就取自问题dp[i-c]
    if wgt[i-1]>c:
        return bag_max_value(wgt,val,i-1,c)

    yes=bag_max_value(wgt,val,i-1,c-wgt[i-1])+val[i-1]
    no=bag_max_value(wgt,val,i-1,c)
    
    return max(yes,no)

wgt = [10,20,30,40,50]
val=[50,120,150,210,240]

res=bag_max_value(wgt,val,5,50)
print(res)

# 时间复杂度分析
#  递归树的深度为 n ,每次都会产生选和不选两个分支，n 层，每层扩大2倍，
# 所以时间复杂度O(2^n)