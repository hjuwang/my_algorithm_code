
def hui_array(array: list[int])->int:
    # 初始化一个dp[i][j] 表示将子数组[array[i]...array[j]]变成回文数组需要插入的最小值
    # 最后需要 dp[0][n-1] ,这个子数组就是数组本身
    # 对于 dp[i][j] :
    # 如果 array[i]=array[j],则 dp[i][j]=dp[i+1][j-1]
    # 如果 array[i]!=array[j]
    # 左侧插入 dp[i][j]=array[j]+dp[i][j-1]  右侧插入 dp[i][j]=array[i]+dp[i+1][j],取其中的最小值
    n= len(array)
    dp = [[0]* n for _ in range(n)]
    
    
    # 子数组的长度范围[2,n],当子数组的长度增加到n的时候，说明就是数组本身了
    for sub_array_length in range (2,n+1):
        #子数组的起始索引i范围推导 
        # 子数组的结束索引 j=i+sub_array_length-1,且不能超过n 所以 i+sub_array_length-1<n
        # 进而推出 i< n-sub_array_length+1
        for i in range(n-sub_array_length+1):
            #子数组结束索引
            j = i+sub_array_length-1
            if array[i]==array[j]:
                dp[i][j]=dp[i+1][j-1]
            else:
                left_insert=array[j]+dp[i][j-1]
                right_insert=array[i]+dp[i+1][j]
                
                #取其中的一个最小值
                dp[i][j]=min(left_insert,right_insert)
    
    return dp[0][n-1]               

    
    
print(hui_array([1, 3, 4, 1]))    