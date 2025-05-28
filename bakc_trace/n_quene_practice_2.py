
def back_track(
    n: int,
    #按行递归
    row_index: int,
    state: list[list[str]],
    res: list[list[list[str]]],
    
    #三个标记
    cols: list[bool],
    major_diag: list[bool],
    minor_diag: list[bool]
    
):
    if row_index==n:
        res.append([list(row) for row in state])
        return
    # 深度优先探索
    for col_index in range(len(cols)):
        #先计算对角线索引
        major_index= row_index-col_index+n-1
        minor_index= row_index+col_index
        if not cols[col_index] and not major_diag[major_index] and not minor_diag[minor_index]:
            state[row_index][col_index]="Q"
            cols[col_index]=major_diag[major_index]=minor_diag[minor_index]=True
            #递归继续摆放
            back_track(n,row_index+1,state,res,cols,major_diag,minor_diag)
            #回退
            state[row_index][col_index]="#"
            cols[col_index]=major_diag[major_index]=minor_diag[minor_index]=False

def n_qnenes(n: int):
    state=[["#" for _ in range(n)] for _ in range(n)]
    res=[]
    cols = [False]*n
    major_diag=[False]*(2*n-1)
    minor_diag=[False]*(2*n-1)
    back_track(n,0,state,res,cols,major_diag,minor_diag)

    print(res)

n_qnenes(4)    