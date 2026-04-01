# Cryptarithmetic: SEND + MORE = MONEY

from itertools import permutations

letters = ('S','E','N','D','M','O','R','Y')

# Try all permutations of digits
for perm in permutations(range(10), len(letters)):
    d = dict(zip(letters, perm))

    # Leading digit constraint
    if d['S'] == 0 or d['M'] == 0:
        continue

    # Form numbers
    send  = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
    more  = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
    money = 10000*d['M'] + 1000*d['O'] + 100*d['N'] + 10*d['E'] + d['Y']

    # Check equation
    if send + more == money:
        print("Solution Found:\n")
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        print("\nMapping:", d)
        break
