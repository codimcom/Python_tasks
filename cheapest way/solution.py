import sys


def main():
    n, m = map(int, input().split())
    mx = []
    for i in range(n):
        mx.append(list(map(lambda x: [int(x), 0], input().split())))
    mx[0][0][1] = mx[0][0][0]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            mx[i][j][1] = min(
                mx[i-1][j][1] if i > 0 else float('inf'),
                mx[i][j-1][1] if j > 0 else float('inf')
            ) + mx[i][j][0]
    print(mx[n-1][m-1][1])



if __name__ == '__main__':
    main()