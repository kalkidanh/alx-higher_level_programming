#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    print('{}'.format(chr(char - ord('a') + (char % 2) * ord('A') +
                          ((char + 1) % 2) * ord('a'))), end='')
