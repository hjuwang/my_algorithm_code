# 将一串数字字符串使用 三个点，划分成一个合法的IP 地址
# 递归的出口条件是，使用了第三个点
# 剪枝的条件是,当前点分配的这个IP地址不合法
# 使用回溯算法来解决这个问题


# ip_num 是剩余的数字字符串
# state 表示当前已经添加了几个
def ip_back_track(ip_num:str,res:list[str],state:list[str]):
    
    if len(ip_num) < (4 - len(state)) or len(ip_num) > 3 * (4 - len(state)):
        return
    # 够了 4 个直接返回
    if len(state)==4 and not ip_num:
        # 拼接
        ip_str=".".join(state)
        res.append(ip_str)
        return      
    for i in range(1,min(4,len(ip_num)+1)):
        # 截取
        current_num=ip_num[:i]
        next_ip_num=ip_num[i:]
        # 当前的数字要符合条件 and 剩余的数字也要符合条件
        # 剩余的数字=len(ip)
        if int(current_num) > 255:
            continue
        if len(current_num) > 1 and current_num[0] == '0':  # 前导零检查
            continue
        state.append(current_num)
        ip_back_track(next_ip_num,res,state)
            #尝试完了要回退
        state.pop()
        
        

ip_num = "25525511135"
res = []
state = [] 
# 添加点索引的范围[0,2]{0,1,2}
ip_back_track(ip_num,res,state)

print(res)
            
            
    
        