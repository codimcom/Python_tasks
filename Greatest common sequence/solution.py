# task link https://coderun.yandex.ru/problem/nop-with-response-recovery/description

import sys


def main():
    n = int(input())
    s1 = input().split()
    m = int(input())
    s2 = input().split()
    common = set(s1) & set(s2)
    s, f = '', ''
    for i in range(n):
        if s1[i] in common:
            s += s1[i]
    for i in range(m):
        if s2[i] in common:
            f += s2[i]
    i = 0
    gcs = ''
    prev = False
    for j in range(n):
        w = s[i:j+1]
        if w in f:
            prev = True
            if len(w) > len(gcs):
                gcs = w
        else:
            if prev:
                i = j
                prev = False
    i = 0
    prev = False
    for j in range(m):
        w = f[i:j + 1]
        if w in s:
            prev = True
            if len(w) > len(gcs):
                gcs = w
        else:
            if prev:
                i = j
                prev = False
    print(*gcs, sep=' ')



if __name__ == '__main__':
    main()
