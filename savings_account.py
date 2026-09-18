from bank_account import BankAccount


class SavingsAccount(BankAccount):
    """Savings account that earns interest."""

    def __init__(self, customer_name, current_balance, minimum_balance,
                 account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance,
                         account_number, routing_number)
        self.interest_rate = interest_rate  # e.g. 0.03 means 3%

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Interest of ${interest:,.2f} added at {self.interest_rate * 100:.1f}% "
              f"(account {self._mask(self._account_number)}).")
        print(f"New balance: ${self.current_balance:,.2f}")

    def print_customer_information(self):
        print("Account Type: Savings")
        super().print_customer_information()
        print(f"Interest Rate: {self.interest_rate * 100:.1f}%")