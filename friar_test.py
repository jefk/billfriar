
import unittest
import friar

class TestFriar(unittest.TestCase):

  def test_parse_valid_input(self):
    # debtor, lender, amount, memo = friar.parse('jeff owes ryan 1000000 for a space station')
    parsed = friar.parse('jeff owes ryan 1000000 for a space station')
    self.assertEqual(parsed, ('jeff', 'ryan', 1000000, 'for a space station') )

  def test_parse_invalid_input(self):
    invalid_input = ''
    self.assertRaises(Exception, friar.parse, invalid_input)

    invalid_input = 'this is not in the grammar'
    self.assertRaises(Exception, friar.parse, invalid_input)

    invalid_input = 'jeff owes ryan ten dollars'
    self.assertRaises(Exception, friar.parse, invalid_input)

if __name__ == "__main__":
  unittest.main()