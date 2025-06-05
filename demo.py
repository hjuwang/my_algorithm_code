

nums = [1,2,3,4]
a = enumerate(nums)
for i,val in a:
    print(i,val)

inorder_map = {val:i for i,val in enumerate(nums)}