# billfriar
billfriar is a script that makes splitting bills among a group easy. The input to the script is a list of debts, like `jeff owes ryan $30 for electric bill`. billfriar will consolidate debts for a group of people, and tell you who owes owe what, minimizing* the number of transactions. (*the greedy algorithm is not garanteed to find the minimum transactions, but it ususally does it)

## usage
`cat data | python3.2 friar.py`
It's a barebones interface--right now you can pipe a list of debts into the script. We plan on setting the billfriar up to be able to recieve emails about debts, and then he will reply with the minimum transactions.

The parser ignores things it can't parse, so the input can be pretty messy. Just make sure there are some lines that have
`[player 1] owes [player 2] [amount]`
billfriar can handle an arbitrary number of debtors and lenders.

## name
billfriar is named (uncreatively) after billmonk, a potentially awesome website that rarely is operational.