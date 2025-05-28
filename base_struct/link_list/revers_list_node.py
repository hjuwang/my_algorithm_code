
class Node:
    def __init__(self,value:int):
        self.value: int = value
        self.next: Node | None=None
        

# 构造单链表
def create_list(array: list[int])->Node:
    # 头插法构造单链表
    head = None
    for i in reversed(array):
        # 创建一个节点
        node=Node(i)
        node.next=head
        head=node
        # print(i)
    return head


def print_list(head: Node):
    p = head
    while p != None:
        print(p.value)
        p=p.next

def reverse_list(head: Node)-> None:
    p = head
    #  新的单链表
    newNead = None
    
    while p!=None:
        #暂存下一个节点
        nextNode=p.next
        #头插
        p.next=newNead
        newNead=p

        #向下接力
        p=nextNode
    return newNead
list = create_list(array=[1,2,3,4])
print_list(list)
print("反转")
newlist =reverse_list(list)
print_list(newlist)


       