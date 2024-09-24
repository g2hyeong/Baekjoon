def solution(a, b, c, d):
    
    # 4 / 3 - 1 / 2 - 2 / 2 - 1 - 1 / 1 - 1 - 1 - 1
    answer = 0
    
    dice = [0] * 7
    dice[a] += 1
    dice[b] += 1
    dice[c] += 1
    dice[d] += 1
    
    if max(dice) == 1:
        answer = dice.index(1)
    elif max(dice) == 2:
        if dice.count(2) == 2:
            p = dice.index(2)
            q = dice[p+1:].index(2) + p+1
            answer = (p + q) * abs(p - q)
        else:
            q = dice.index(1)
            r = dice[q+1:].index(1) + q+1
            answer = q * r
    elif max(dice) == 3:
        p = dice.index(3)
        q = dice.index(1)
        answer = (10 * p + q) * (10 * p + q)
    else:
        p = dice.index(4)
        answer = p * 1111
    
    return answer