
import unittest
import friar

class TestFriar(unittest.TestCase):

    def test_parse_valid_input(self):
        parsed = friar.parse('jeff owes ryan 1000000 for a space station')
        self.assertEqual(parsed, ('jeff', 'ryan', 1000000, 'for a space station') )

    def test_parse_invalid_input(self):
        invalid_input = ''
        self.assertRaises(Exception, friar.parse, invalid_input)

        invalid_input = 'this is not in the grammar'
        self.assertRaises(Exception, friar.parse, invalid_input)

        invalid_input = 'jeff owes ryan ten dollars'
        self.assertRaises(Exception, friar.parse, invalid_input)

    def test_shuffle(self):
        credit = {
            'aaron': 100,
            'abe': 50,
            'granger': -80,
            'the girl': -70
        }
        transactions = friar.shuffle(credit)
        expected = [
            {'payee': 'aaron','amount': 80.0,'payer': 'granger'},
            {'payee': 'abe', 'amount': 50.0, 'payer': 'the girl'},
            {'payee': 'aaron', 'amount': 20.0, 'payer': 'the girl'}
        ]
        self.assertEqual(transactions, expected)

if __name__ == "__main__":
    unittest.main()