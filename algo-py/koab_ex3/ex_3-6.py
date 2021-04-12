import sys

K = int(input('K? >>'))
N = int(input('N? >>'))
cal_cnt = 0

cand_li = list(range(0, K+1))
ans_li = []

cnt = 0
for X in cand_li:
    for Y in cand_li:
        for Z in cand_li:
            cal_cnt += 1
            if X + Y + Z == N:
                cnt += 1
                ans_li.append('{0}, {1}, {2}'.format(X, Y , Z))

print('ans: ', cnt)
print('ans list: ', ans_li)
print('N : ', N)
print('calc count : ', cal_cnt)