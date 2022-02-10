from unittest.mock import patch
from io import StringIO
from phonebook_ import *
import unittest


print('Task 2', end='\n\n')

# Write tests for the Phonebook application,
# which you have implemented in module 1.
# Design tests for this solution and
# write tests using unittest library


class TestPhonebook(unittest.TestCase):
    def setUp(self) -> None:
        self.fakeio = StringIO()
        self.fake_out = patch('sys.stdout', new=self.fakeio)
        self.contacts = all_contacts

    def test_display_one_contact(self):
        with self.fake_out:
            display_one_contact(self.contacts[0])
            self.assertIn('Onopko', self.fakeio.getvalue())
            self.assertNotIn('Ohrim Sudomora', self.fakeio.getvalue())

    def test_search_any(self):
        rez = search_any(self.contacts, 'Zelinska', 'surname')
        self.assertIn('Zelinska', rez[0].get('surname'))
        self.assertNotIn('Ohrim Sudomora', rez[0].get('surname'))


if __name__ == '__main__':
    unittest.main()
