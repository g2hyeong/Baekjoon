cash = int(input())
chart = list(map(int, input().split()))

def BNP():
    leftover = cash
    cnt = 0
    for c in chart:
        cnt += leftover // c
        leftover = leftover % c
    return cnt, leftover

def TIMING():
    leftover = cash
    cnt = 0
    buy_flag = False
    sell_flag = False
    for i in range(3, len(chart)):
        if chart[i - 3] < chart[i - 2] < chart[i - 1] < chart[i]:
            sell_flag = True
        else:
            sell_flag = False

        if chart[i - 3] > chart[i - 2] > chart[i - 1] > chart[i]:
            buy_flag = True
        else:
            buy_flag = False

        if sell_flag:
            leftover += cnt * chart[i]
            cnt = 0

        if buy_flag:
            cnt += leftover // chart[i]
            leftover = leftover % chart[i]

    return cnt, leftover


bnp_cnt, bnp_leftover = BNP()
bnp_rst = bnp_cnt * chart[-1] + bnp_leftover

timing_cnt, timing_leftover = TIMING()
timing_rst = timing_cnt * chart[-1] + timing_leftover

if bnp_rst > timing_rst:
    print("BNP")
elif bnp_rst < timing_rst:
    print("TIMING")
else:
    print("SAMESAME")

