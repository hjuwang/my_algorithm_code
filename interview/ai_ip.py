def ip_back_track(ip_num: str, res: list[str], state: list[str]):
    # 剪枝条件1：剩余数字长度不合法
    if len(ip_num) < (4 - len(state)) or len(ip_num) > 3 * (4 - len(state)):
        return
    
    # 递归出口：已经分成4部分
    if len(state) == 4:
        if not ip_num:  # 确保所有数字都用完了
            ip_str = ".".join(state)
            res.append(ip_str)
        return
    
    for i in range(1, min(4, len(ip_num) + 1)):
        current_num = ip_num[:i]
        next_ip_num = ip_num[i:]
        
        # 检查当前分段是否合法：0-255且没有前导零（除非就是0）
        if int(current_num) > 255:
            continue
        if len(current_num) > 1 and current_num[0] == '0':  # 前导零检查
            continue
            
        state.append(current_num)
        ip_back_track(next_ip_num, res, state)
        state.pop()

ip_num = "25525511135"
res = []
state = []

ip_back_track(ip_num, res, state)

print(res)