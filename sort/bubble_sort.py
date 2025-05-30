# 每次从[0,i] 的范围中选取最大的放在 array[i]
# i的曲直范围是[1,n-1]

def bubble_sort(array):
    n=len(array)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                
                
array = [4,2,7,89,4]

bubble_sort(array)

print(array)            
            
            
            
#时间复杂度和            
            