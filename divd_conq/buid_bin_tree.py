from modules import TreeNode

#分治的思想构建二叉树
def dfs(
    preorder:list[int], #前序遍历列表
    inorder_map:dict[int,int], # 中序遍历字典[value:index]
    i:int ,# 当前树 root 节点在前序遍历中的索引
    
    l:int,r:int #[l,r],当前树在中序遍历中的索引范围（闭区间）
    )-> TreeNode:
    
    if l>r: # 遍历完成
        return None
    #初始化root 节点
    
    root = TreeNode(preorder[i])
    m= inorder_map[preorder[i]]
    #分治构建左子树
    '''
    在前序遍历中，左子树的根节点索引是当前根节点的索引+1 ,所以= i+1
    在中序遍历中，左子树的范围是   
    '''
    root.left = dfs(preorder,inorder_map,i+1,l,m-1)
    root.right = dfs(preorder,inorder_map,i+1+(m-l),m+1,r)    
    return root
    
def build_tree(preeorder:list[int],inorder:list[int])->TreeNode:
    
    inorder_map = {val:i for i,val in enumerate(inorder)}
    i,l,r = 0,0,len(inorder)-1
    
    root = dfs(preeorder,inorder_map,i,l,r)
    
    return root
    
preorder = [3,9,2,1,7]
inorder = [9,3,1,2,7]
root = build_tree(preorder,inorder)

print(root.left)

    