# 部分和問題を再帰関数で解いたコード4.9をメモ化せよ

# まずはメモ化していないコード4.9をそのままPythonで書き下す
# > https://github.com/drken1215/book_algorithm_solution/blob/master/codes/chap04/code_4_9.cpp

import sys
from typing import List


calc_cnt = 0
memo = None


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

# 解答（メモ化したもの）
# > O(NW)なので、N個の要素とW個の要素の組み合わせの結果を配列に入れるのかな？
# >> いやその場合だと計算量の削減につながらない。W=wについてTrue/Falseかわかればいいのだから、Wについて結果を保持しておけばいい
def partial_sum_memorized(i: int, W: int, numbers: List[int]) -> bool:
    # すでに計算しているならば計算しない
    global memo
    if memo[i][W] is not None:
        return memo[i][W]
    
    # show process
    global calc_cnt
    print('call i={0}, W={1}, calc:{2}'.format(i, W, calc_cnt))
    calc_cnt += 1
    
    # base case
    if i == 0:
        if W == 0:
            memo[i][W] = True
            return True
        else:
            memo[i][W] = False
            return False
    
    # a[i-1] を選ばない場合
    if partial_sum_memorized(i - 1, W, numbers):
        memo[i-1][W] = True
        return True
    # a[i-1] を選ぶ場合
    if partial_sum_memorized(i - 1, W - numbers[i - 1], numbers):
        memo[i-1][W] = True
        return True
    memo[i][W] = False
    return False


if __name__ == "__main__":
    #numbers = list(map(int, input("numbers(sep space) >> ").split()))
    numbers = [i for i in range(1000)]
    N = len(numbers)
    W = int(input('W? >>'))
    
    # init memo 2d array
    memo = [[None for _ in range(W+1)] for _ in range(N+1)] # row=N+1, col=W+1
    
    if partial_sum_memorized(N, W, numbers):
        print('Yes')
    else:
        print('No')
    print('N=', N, ' W=', W)
