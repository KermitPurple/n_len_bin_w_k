#!/usr/bin/env python3

from sys import argv
from typing import Iterator

def bin_strings(length: int) -> Iterator[list[int]]:
    '''
    gets all binary strings with a given length
    :length: The length of the binary string
    :returns: a generator of lists of ints
    '''
    string = [0 for _ in range(length)]
    for _ in range(2 ** length):
        yield string
        for i in range(len(string)):
            string[i] += 1
            if string[i] < 2:
                break
            string[i] = 0

def m_spaced(bin_string: list[int], m: int) -> bool:
    '''
    make sure that there are at least m 1s spaced evenly from eachother
    :bin_string:
    :m: number of correctly spaced 1s
    :returns: true if it is spaced correctly
    '''
    distances = {i: 0 for i in range(len(bin_string))}
    for i, a in enumerate(bin_string):
        if a == 0:
            continue
        for j, b in enumerate(bin_string[i + 1:], i + 1):
            if b == 0:
                continue
            distances[j - i] += 1
    for count in distances.values():
        if count >= m:
            return True
    return False

def main():
    '''Driver Code'''
    _ = argv.pop(0)
    match len(argv):
        case 0:
            n = int(input('Enter n> '))
            k = int(input('Enter k> '))
            m = int(input('Enter m> '))
        case 3:
            n, k, m = map(int, argv)
        case count:
            print(f'Invalid number of arguments: {count}')
            return 1
    strings = set()
    for bin_string in bin_strings(n):
        if bin_string.count(1) == k and not m_spaced(bin_string, m):
            rev_bin_string = reversed(bin_string)
            string = ''.join(map(str, bin_string))
            rev_string = ''.join(map(str, rev_bin_string))
            if rev_string not in strings:
                print(string)
                strings.add(string)

if __name__ == '__main__':
    raise SystemExit(main())
