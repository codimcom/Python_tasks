# link to the task https://coderun.yandex.ru/problem/anagrams
import sys


def main():
    a = input()
    b = input()
    sym_a = set(a)
    sym_b = set(b)
    if sym_a != sym_b:
        print(0)
    else:
        counter_a = dict((c, a.count(c)) for c in sym_a)
        counter_b = dict((c, b.count(c)) for c in sym_b)
        print(int(counter_a == counter_b))


if __name__ == '__main__':
    main()
