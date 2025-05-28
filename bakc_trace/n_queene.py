
def back_track(
    row: int, 
    n: int,
    # 表示当前的状态，二维数组
    state: list[list[str]], 
    # 记录结果，每一个结果都是一个二维数组
    res: list[list[list[str]]],

    # 记录当前行是否有皇后
    cols: list[bool],
    diags1: list[bool],
    diags2: list[bool],
):
    if row==n:
        res.append([list(row)  for row in state])
        return
    #遍历所有的列
    for col in range(n):
        # 计算所在的主，次对角线
        diag1=row-col+n-1
        diag2=row+col
        if not cols[col] and not diags1[diag1] and not diags2[diag2]:
            # 在该位置放置皇后,并做标记
            state[row][col]= "Q"
            cols[col]=diags1[diag1]=diags2[diag2]=True
            #放置下一行
            back_track(row+1,n,state,res,cols,diags1,diags2) 
            #回退
            state[row][col]="#"
            cols[col]=diags1[diag1]=diags2[diag2]=False


def n_queens(n: int) -> list[list[list[str]]]:
    # 初始化棋盘二维数组
    state =[["#" for _ in range(n)] for _ in range(n)]  
    # 共有 n 列
    cols = [False]*n
    # 分别有 2n-1个主对角线和次对角线
    diags1=[False]*(2*n-1)
    diags2=[False]*(2*n-1)
    res = []
    back_track(0,n,state,res,cols,diags1,diags2)
    return res

# 单独运行这个脚本
if __name__ == "__main__":
   res= n_queens(8)
   print(res)