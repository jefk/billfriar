#! /usr/bin/python3.2

import sys
import re
import heapq
from collections import Counter

class MaxHeap():
    ''' making heapq classy
    '''

    def __init__(self, ls = []):
        ''' ls is a list of tuples in this format
            [ (val, label), (val, label), ... ]
        '''
        # multiply val by -1 to make this into a max heap, heapq is min heap
        self.heap = [ [-1 * val, label] for val, label in ls ]
        heapq.heapify(self.heap)

    def pop(self):
        entry = heapq.heappop(self.heap)
        entry[0] = -1 * entry[0]
        return entry

    def push(self, entry):
        heapq.heappush(self.heap, [-1 * entry[0], entry[1] ])

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return self.heap.__str__()


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
    return MaxHeap(debtor_values), MaxHeap(lender_values)

def shuffle(credit):
    '''
    '''
    debtors, lenders = make_heaps(credit)
    while not debtors.is_empty() or not lenders.is_empty():
        debtor = debtors.pop()
        lender = lenders.pop()
        amount = min(debtor[0], lender[0])

        if debtor[0] > lender[0]:
            debtor[0] -= amount
            debtors.push(debtor)
        elif debtor[0] < lender[0]:
            lender[0] -= amount
            lenders.push(lender)
        else:
            # the debts are equal, so neither goes back on the heap
            pass

        print('{debtor[1]} pays {lender[1]} ${amount}'.format( **locals() ))

if __name__ == "__main__":
    credit = Counter()
    for line in sys.stdin:
        debtor, lender, amount = parse(line)
        credit[lender] += amount
        credit[debtor] -= amount

    transactions = shuffle(credit)
