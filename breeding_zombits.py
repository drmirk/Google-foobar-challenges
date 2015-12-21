r_dict = {0:1, 1:1, 2:2}

def answer(str_S):
    num_zombits = int(str_S)
    position = navigate_dict(num_zombits)
    if position == -1:
        return None
    else:
        return str(position)

def navigate_dict(num_zombits):
    left = num_zombits
    right = 0
    pos_ev = num_zombits/4 * 2
    pos_odd = num_zombits/4 *2 -1
    response = 0
    while response != num_zombits:
        response = recurse(pos_ev)
        if response > num_zombits:
            left = pos_ev
            pos_ev = pos_ev - (pos_ev - right)/4 *2
        elif response < num_zombits:
            right = pos_ev
            pos_ev = pos_ev + (left - pos_ev)/4 *2
        if pos_ev >= left or pos_ev <= right:
            pos_ev = -1
            break;
    response = 0
    left = num_zombits
    right = 0
    while response != num_zombits:
        response = recurse(pos_odd)
        if response > num_zombits:
            left = pos_odd
            pos_odd = pos_odd - (pos_odd - right)/4 * 2 +1
        elif response < num_zombits:
            right = pos_odd
            pos_odd = pos_odd + (left - pos_odd)/4 * 2 +1
        if pos_odd >= left or pos_odd <= right:
            pos_odd = -1
            break;
    return max(pos_ev, pos_odd)


def recurse(n):
    try:
        return r_dict[n]
    except:
        if n % 2== 0:
            r_dict[n] = recurse(n/2+1)+ recurse(n/2)+n/2
        else:
            r_dict[n] = recurse((n-1)/2)+recurse((n-1)/2-1)+1
        return r_dict[n]


print answer("7")
print answer("72")# == "41"
print answer("100")
print answer("133")
print answer("1083")
print answer(str(10**25))
