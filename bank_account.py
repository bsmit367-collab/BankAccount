class BankAccount:
    """Base class for all bank accounts."""

    bank_title = "My Bank"

    def __init__(self, customer_name, current_balance, minimum_balance,
                 account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # protected: subclasses may use it
        self.__routing_number = routing_number  # private: only this class may use it

    # ---------- accessors ----------
    def get_account_number(self):
        return self._account_number

    def get_routing_number(self):
        # Subclasses cannot touch self.__routing_number directly
        # (name mangling), so they go through this getter.
        return self.__routing_number

    # ---------- protected helper ----------
    @staticmethod
    def _mask(number):
        """Show only the last 4 digits, e.g. ****5678."""
        number = str(number)
        return "*" * (len(number) - 4) + number[-4:]

    # ---------- behavior ----------
    def deposit(self, amount):
        self.current_balance += amount
        print(f"${amount:,.2f} deposited.")
        print(f"New balance: ${self.current_balance:,.2f}")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Withdrawal denied: minimum balance must be maintained.")
        else:
            self.current_balance -= amount
            print(f"${amount:,.2f} withdrawn.")
            print(f"New balance: ${self.current_balance:,.2f}")

    def print_customer_information(self):
        print("Bank:", BankAccount.bank_title)
        print("Customer:", self.customer_name)
        print("Account Number:", self._mask(self._account_number))
        print("Routing Number:", self._mask(self.__routing_number))
        print(f"Current Balance: ${self.current_balance:,.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:,.2f}")