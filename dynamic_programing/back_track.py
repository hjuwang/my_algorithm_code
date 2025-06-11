# 使用回溯穷举的方法计算爬楼梯解的问题

# 爬一个n 层的楼梯，每次只能爬 1层或者 2 层，试问爬到第n 层共有几种爬法

def back_track(n:int,state:int,res:list[int],choices:list[int]):
    if state==n:
        res[0]+=1
        
    for choice in choices:
        state+=choice
        if state>n:
            continue
        back_track(n,state,res,choices)
        # 回退(不爬)
        state-=choice
      
      
#         
        
choices= [1,2]
state = 0
res= [0]
back_track(4,state,res,choices)
print(res[0])        
        
        