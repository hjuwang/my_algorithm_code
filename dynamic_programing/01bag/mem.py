# 使用记忆化搜索来优化暴力搜索递归,添加一个mem 来记录搜索结果

def bag_max_value(wgt:list[int],val:list[int],i:int,c:int,mem:list[list[int]])->int:
    #已经选完所有的物品，且背包没有剩余容量
    if i==0 or c==0:
        return 0
    
    if mem[i][c]!=-1:
        return mem[i][c]
    # 方不下第i 个物品，那就取自问题dp[i-c]
    if wgt[i-1]>c:
        return bag_max_value(wgt,val,i-1,c,mem)

    yes=bag_max_value(wgt,val,i-1,c-wgt[i-1],mem)+val[i-1]
    no=bag_max_value(wgt,val,i-1,c,mem)
    
    mem[i][c] = max(yes,no)
    return mem[i][c]

wgt = [10,20,30,40,50]
val=[50,120,150,210,240]

mem= [[-1] * 51 for _ in range(5+1)]

res=bag_max_value(wgt,val,5,50,mem)
print(res)