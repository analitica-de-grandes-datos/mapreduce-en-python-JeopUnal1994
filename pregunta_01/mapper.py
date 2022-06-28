#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

#! /usr/bin/ python3

import sys

def purpose_amount(x):
    return x[2]

for line in sys.stdin:
    result = line.split(',')
    print(purpose_amount(result))
