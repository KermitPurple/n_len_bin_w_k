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

def main():
    '''Driver Code'''
    _ = argv.pop(0)
    match len(argv):
        case 0:
            n = int(input('Enter n> '))
            k = int(input('Enter k> '))
        case 2:
            n, k = map(int, argv)
        case count:
            print(f'Invalid number of arguments: {count}')
            return 1
    strings = set()
    for bin_string in bin_strings(n):
        if bin_string.count(1) == k:
            rev_bin_string = reversed(bin_string)
            string = ''.join(map(str, bin_string))
            rev_string = ''.join(map(str, rev_bin_string))
            if rev_string not in strings:
                print(string)
                strings.add(string)

if __name__ == '__main__':
    raise SystemExit(main())
