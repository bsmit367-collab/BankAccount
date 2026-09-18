from bank_account import BankAccount


class CheckingAccount(BankAccount):
    """Checking account with a limit on the number of transfers."""

    def __init__(self, customer_name, current_balance, minimum_balance,
                 account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance,
                         account_number, routing_number)
        self.transfer_limit = transfer_limit  # max transfers allowed
        self.transfers_made = 0

    def transfer(self, amount, target_account):
        if self.transfers_made >= self.transfer_limit:
            print(f"Transfer denied: limit of {self.transfer_limit} transfers reached.")
            return False

        if self.current_balance - amount < self.minimum_balance:
            print("Transfer denied: minimum balance must be maintained.")
            return False

        self.current_balance -= amount
        target_account.current_balance += amount
        self.transfers_made += 1

        print(f"${amount:,.2f} transferred from account {self._mask(self._account_number)} "
              f"to account {self._mask(target_account.get_account_number())}.")
        print(f"New balance: ${self.current_balance:,.2f}")
        print(f"Transfers used: {self.transfers_made}/{self.transfer_limit}")
        return True

    def print_customer_information(self):
        print("Account Type: Checking")
        super().print_customer_information()
        print(f"Transfers Used: {self.transfers_made}/{self.transfer_limit}")