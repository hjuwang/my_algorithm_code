# 给定 n 中面值不同的硬币,第 i 种硬币的面值是 coins[i-1],目标金额 amnt
# 用最少的硬币数，凑出 amnt,返回这个硬币数字，否则返回-2


def conis_change_greedy(coins:list[int],amnt:int)->int:
    
    # 假设 coins 是从小到大排序
    count=0
    while amnt>0:
        # 选出一个最接近 amnt的,且不能超过 amnt
        i=0
        while i<len(coins):
            if coins[i]>amnt:
                break
            i+=1
        amnt-=coins[i-1]
        count+=1    
        
    return count if amnt==0 else -1   

def conis_change_greedy(coins:list[int],amnt:int)->int:
    
    # 假设 coins 是从小到大排序
    count=0
    while amnt>0:
        
        select_coin=0
        # 每次选择一个最接近 amnt的 coin,但是不超过 amnt
        # amnt-coin>0
        for coin in coins:
            if am
            
            
            
        amnt-=coins[i-1]
        count+=1    
        
    return count if amnt==0 else -1   

res = conis_change_greedy(coins=[1,5,10,20,50,100],amnt=131)
print(res) 