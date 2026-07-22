# link to the task https://coderun.yandex.ru/problem/knight-move/description
import sys
import math


def main():
    n, m = list(map(int, input().split()))
    n, m = n-1, m-1
    if (n+m)%3 != 0:
        res = 0
    else:
        res = int(
            math.factorial(int((n+m)/3))/
            (math.factorial(int((2*n-m)/3)) * math.factorial(int((2*m-n)/3))))
    print(res)


if __name__ == '__main__':
    main()