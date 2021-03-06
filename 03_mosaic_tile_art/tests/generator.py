#!/usr/bin/env python3
import random

MIN = 1
MAX = 10**5

SMALL_TESTCASES = 10
LARGE_TESTCASES = 10
RANDOM_TESTCASES = 20

testcases = []

testcases.append(MIN)
testcases.append(3)
testcases.append(MAX)

small_cases = 2
large_cases = 1
random_cases = 0


while small_cases < SMALL_TESTCASES:
    case = random.randint(MIN, MIN+100)
    if case in testcases: continue
    testcases.append(case)
    small_cases += 1
while large_cases < LARGE_TESTCASES:
    case = random.randint(MAX-100, MAX)
    if case in testcases: continue
    testcases.append(case)
    large_cases += 1
while random_cases < RANDOM_TESTCASES:
    case = random.randint(MIN, MAX)
    if case in testcases: continue
    testcases.append(case)
    random_cases += 1


for i,n in enumerate(list(testcases)):
    with open('input_{:03d}.in'.format(i), 'w') as fout:
        fout.write(str(n) + '\n')
