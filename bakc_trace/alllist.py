#  使用回溯算法，计算去全排列

def back_track(
    # 全排列的个数    
    n: int,
    choice: list[bool],
    selected: list[bool],
   
    state: list[int],
    # 保存结果,每个结果是一纬数组,所有结果是二维数组
    res: list[list[int]]
):  
    #如果已经填完了则直接返回
    if len(state)==n:
        #添加结果
        res.append(state.copy()) 
        # res.append([v for v in state]) 
        return
    #在choice 中循环选择没有被使用的数字
    for i in range(len(choice)):
        # 填充state
        if not selected[i]:
            state.append(choice[i])
            selected[i]=True
            #深度优先
            back_track(n,choice,selected,state,res)
            #回退
            selected[i]=False
            state.pop()    
def alllist(choice: list[int]) -> list[list[int]]:

    selected = [False]*len(choice)
    state=[]
    res=[]
    back_track(len(choice),choice,selected,state,res)
    return res


if __name__=="__main__":
    choice= [1,2,3]
    res=alllist(choice)
    print(res)                    