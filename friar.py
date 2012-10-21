
import sys
import re
from collections import Counter

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

def shuffle(debts):
    pass

if __name__ == "__main__":
    debts = Counter()
    for line in sys.stdin:
        debtor, lender, amount = parse(line)
        debts[lender] += amount
        debts[debtor] -= amount

    transactions = shuffle(debts)