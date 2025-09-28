import  unittest
from bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000000)

    def tearDown(self):
        del self.account

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(),1000000)

    def  test_deposit(self):
        self.account.deposit(6000000)
        self.assertEqual(self.account.get_balance(),7000000)

    def  test_withdraw_success(self):
        result =self.account.withdraw(400000)
        self.assertTrue(result)
        self.assertEqual(self.account.get_balance(),600000)

    def test_withdraw_fail(self):
        result = self.account.withdraw(2000000)
        self.assertFalse(result)
        self.assertEqual(self.account.get_balance(),1000000)

if __name__ == '__main__':
    unittest.main()