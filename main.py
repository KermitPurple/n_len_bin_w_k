#!/usr/bin/env python3

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

def print_bin_string(string: list[int]):
    '''print a binary string'''
    print(''.join(map(str, string)))

def main():
    '''Driver Code'''
    for string in bin_strings(9):
        print_bin_string(string)
    strings = set()

if __name__ == '__main__':
    main()
