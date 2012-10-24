#! /usr/bin/python3.2

import sys
import re
import heapq
from collections import Counter

class MaxHeap(list):
    ''' making heapq classy
    '''

    def __init__(self, ls = []):
        ''' ls is a list of tuples in this format
            [ (val, label), (val, label), ... ]
        '''
        list.__init__(self, ls)
        # multiply val by -1 to make this into a max heap, heapq is min heap
        heapq.heapify([ [-1 * val, label] for val, label in self ])

    def pop(self):
        entry = heapq.heappop(self)
        entry[0] = -1 * entry[0]
        return entry

    def push(self, entry):
        heapq.heappush(self, [-1 * entry[0], entry[1] ])

    def is_empty(self):
        return len(self) == 0


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
    debtor_values = [ (credit[person], person) for person in credit if credit[person] < 0 ]
    lender_values = [ (-1 * credit[person], person) for person in credit if credit[person] > 0 ]
    return MaxHeap(debtor_values), MaxHeap(lender_values)

def shuffle(credit):
    '''
    '''
    debtors, lenders = make_heaps(credit)
    print(debtors, lenders)
    while not debtors.is_empty() or not lenders.is_empty():
        debtor = debtors.pop()
        lender = lenders.pop()
        amount = abs(debtor[0] - lender[0])
        print('debtor,lender', debtor, lender)

        if debtor[0] > lender[0]:
            debtor[0] -= amount
            debtors.push(debtor)
        elif lender[0] < debtor[0]:
            lender[0] -= amount
            lenders.push(lender)
        else:
            # the debts are equal, so neither goes back on the heap
            pass

        print(debtors, lenders)
        print('{lender[1]} pays {debtor[1]} ${amount}'.format( **locals() ))

if __name__ == "__main__":
    credit = Counter()
    for line in sys.stdin:
        debtor, lender, amount = parse(line)
        credit[lender] += amount
        credit[debtor] -= amount

    transactions = shuffle(credit)
