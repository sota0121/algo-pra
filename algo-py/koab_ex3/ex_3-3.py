import sys

a = list(map(int,input().split()))
cal_cnt = 0

min_val = 2**10
min_2nd_val = 2**10
for av in a:
    cal_cnt += 1
    if min_2nd_val > av:
        if min_val > av:
            min_val = av
        else:
            min_2nd_val = av

print('ans: ', min_2nd_val)
print('input list len: ', len(a))
print('calc count : ', cal_cnt)
