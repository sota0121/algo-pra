# 部分和問題を再帰関数で解いたコード4.9をメモ化せよ

# まずはメモ化していないコード4.9をそのままPythonで書き下す
# > https://github.com/drken1215/book_algorithm_solution/blob/master/codes/chap04/code_4_9.cpp

import sys
from typing import List


def partial_sum(i: int, W: int, numbers: List[int]) -> bool:
    # show process
    global calc_cnt
    print('call i={0}, W={1}, calc:{2}'.format(i, W, calc_cnt))
    calc_cnt += 1
    
    # base case
    if i == 0:
        if W == 0:
            return True
        else:
            return False
    
    # a[i-1] を選ばない場合
    if partial_sum(i - 1, W, numbers):
        return True
    # a[i-1] を選ぶ場合
    if partial_sum(i - 1, W - numbers[i - 1], numbers):
        return True
    return False

if __name__ == "__main__":
    calc_cnt = 0
    numbers = list(map(int, input("numbers(sep space) >> ").split()))
    N = len(numbers)
    W = int(input('W? >>'))
    
    if partial_sum(N, W, numbers):
        print('Yes')
    else:
        print('No')
