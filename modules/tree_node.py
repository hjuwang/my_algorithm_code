
# 定义二叉树节点类
class TreeNode:
    
    def __init__(self,val :int =0):
        self.val = val
        self.left:TreeNode| None = None
        self.right:TreeNode| None = None