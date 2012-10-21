
import sys
import re
import heapq
from collections import Counter

def max_heapify(ls):
    return heapq.heapify( [(-1 * val, label) for val, label in ls] )

def parse(line):
    ''' lines are expect to be in this form
        [debtor] owes [lender] [dollars]
    '''
    line = line.strip()
    line = re.sub('\s+', ' ', line)
    debtor, rest = line.split(' owes ', 1)
    lender, rest = rest.split(' ', 1)
    amount = rest.split(' ')[0]
    amount = amount.replace('$', '')

    try:
        amount = float(amount)
    except:
        amount = 0

    return debtor, lender, amount

def make_heaps(credit):
    debtor_values = [ (-1 * credit[person], person) for person in credit if credit[person] < 0 ]
    lender_values = [ (credit[person], person) for person in credit if credit[person] > 0 ]
    print(debtor_values)
    print(lender_values)
    max_heapify(debtor_values)
    max_heapify(lender_values)
    return debtor_values, lender_values

def shuffle(credit):
    '''
    '''
    debtors, lenders = make_heaps(credit)
    print(debtors)
    print(lenders)

if __name__ == "__main__":
    credit = Counter()
    for line in sys.stdin:
        debtor, lender, amount = parse(line)
        credit[lender] += amount
        credit[debtor] -= amount

    transactions = shuffle(credit)