# 桶排序，基于分治策略的,但是非比较的排序,
def bucket_sort(array:list[int]):
    # 暂定每个桶放2个元素
    k=len(array)//2 
    #初始化桶
    buckets=[[] for _ in range(k)]
    #注意这个桶索引计算的方法
    for v in array:
        # 这是浮点数计桶索引的办法
        bucket_index =int(v*k)
        buckets[bucket_index].append(v)
        
    #对每个桶进行排序
    for bucket in buckets:
        bucket.sort()
        
    #将桶中的数组替换进原来的数组中
    i=0
    for bucket in buckets:
        for v in bucket:
            array[i]=v
            i+=1       
            
            
array = [0.49,0.96,0.82,0.09,0.57,0.43,0.91,0.75,0.15,0.37]
bucket_sort(array=array)
print(array)            
            
# 算法时间复杂度分析
            
            