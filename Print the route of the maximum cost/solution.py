# link to the task https://coderun.yandex.ru/problem/print-the-route-of-the-maximum-cost/ai
import sys


def main():
    n, m = list(map(int, input().split()))
    mx = []
    for i in range(n):
        mx.append(list(map(lambda x: [int(x), 0, ''], input().split())))
    mx[0][0][1] = mx[0][0][0]
    for i in range(1, n):
        mx[i][0][1] = mx[i - 1][0][1] + mx[i][0][0]
        mx[i][0][2] = 'D'
    for j in range(1, m):
        mx[0][j][1] = mx[0][j - 1][1] + mx[0][j][0]
        mx[0][j][2] = 'R'
    for i in range(1, n):
        for j in range(1, m):
            if mx[i - 1][j][1] > mx[i][j - 1][1]:
                mx[i][j][1] = mx[i - 1][j][1] + mx[i][j][0]
                mx[i][j][2] = 'D'
            else:
                mx[i][j][1] = mx[i][j - 1][1] + mx[i][j][0]
                mx[i][j][2] = 'R'
    max_sum = mx[n - 1][m - 1][1]
    route = ''
    i, j = n - 1, m - 1
    for _ in range(n + m - 2):
        mark = mx[i][j][2]
        route += mark
        if mark == 'D':
            i -= 1
        else:
            j -= 1
    print(max_sum)
    print(*route[::-1])


if __name__ == '__main__':
    main()