import sys
from typing import Tuple

# K以下の753数を数える問題。許容計算量は、O(3^d)。ただし、dはKの桁数。

# 動的計画法で解く
def count_consists_of_three_nums_dp(
    n1: int, n2: int, n3: int, K: int) -> Tuple[int, int]:
    """考えたこと
        - 制約条件は、K以下。dが3以上。これがベースケース作りに繋がると思う
        - 漸化式の元になる考え方は
            - 7/5/3からそれぞれ1つずつ選び、
            - d-3>0 ならば、d-3回、重複ありで7/5/3から数値を選ぶ
            - d桁取り終えたら、並べ替えのパターンを昇順にforループを回し
            - Kより大になったらおわり
        - わからないところ
            - 関数一回でなんの処理をすればいいか、どういう単位で再帰すればいいか
    """
    return 1, 2


# 線形探索
def count_consists_of_three_nums(n1: int, n2: int, n3: int, K: int) -> Tuple[int, int]:
    # K is more than the least number
    sorted_numbers = sorted([n1, n2, n3])
    the_least_number = int(''.join(map(str, sorted_numbers)))
    if K < the_least_number:
        return 0, 1
    
    count = 0
    cal_cnt = 0
    for k in range(the_least_number, K+1):
        digits = [int(d) for d in str(k)]
        found_n1 = 0
        found_n2 = 0
        found_n3 = 0
        found_other = False
        for d in digits:
            cal_cnt += 1
            if n1 == d:
                found_n1 += 1
            elif n2 == d:
                found_n2 += 1
            elif n3 == d:
                found_n3 += 1
            else:
                found_other = True
                break
        if (found_other == False) and (found_n1 > 0) and (found_n2 > 0) and (found_n3 > 0):
            count += 1
    return count, cal_cnt


K = int(input('K? >>'))
n1 = int(input('n1? >>'))
n2 = int(input('n2? >>'))
n3 = int(input('n3? >>'))
result, cal_cnt = count_consists_of_three_nums(n1, n2, n3, K)
print('==============')
print('ans : ', result)
print('cal cnt : ', cal_cnt)
