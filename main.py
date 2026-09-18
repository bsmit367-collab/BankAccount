from savings_account import SavingsAccount
from checking_account import CheckingAccount


def line(title):
    print("\n" + "=" * 45)
    print(title)
    print("=" * 45)


# ---------------------------------------------------------
# Scenario 1: Alice opens a checking account and withdraws
# ---------------------------------------------------------
line("Checking 1: Alice opens a checking account")
checking1 = CheckingAccount("Alice", 1000, 100, "100200301234", "021000021", transfer_limit=2)
checking1.print_customer_information()

print("\n-> Alice withdraws $250")
checking1.withdraw(250)

print("\n-> Alice tries to withdraw $700 (would go below minimum)")
checking1.withdraw(700)

# ---------------------------------------------------------
# Scenario 2: Bob's checking account + transfer limitation
# ---------------------------------------------------------
line("Checking 2: Bob opens a checking account")
checking2 = CheckingAccount("Bob", 500, 50, "100200305678", "021000021", transfer_limit=2)
checking2.print_customer_information()

print("\n-> Alice transfers $100 to Bob")
checking1.transfer(100, checking2)

print("\n-> Alice transfers $50 to Bob")
checking1.transfer(50, checking2)

print("\n-> Alice tries a 3rd transfer (limit is 2)")
checking1.transfer(25, checking2)

print("\n-> Bob's account after receiving transfers")
checking2.print_customer_information()

# ---------------------------------------------------------
# Scenario 3: Maria opens a savings account and earns interest
# ---------------------------------------------------------
line("Savings 1: Maria opens a savings account")
savings1 = SavingsAccount("Maria", 2000, 500, "200300409876", "021000021", interest_rate=0.03)
savings1.print_customer_information()

print("\n-> Maria deposits $500")
savings1.deposit(500)

print("\n-> Interest is added")
savings1.add_interest()

print("\n-> Maria tries to withdraw $2,200 (would go below minimum)")
savings1.withdraw(2200)

# ---------------------------------------------------------
# Scenario 4: David's savings account
# ---------------------------------------------------------
line("Savings 2: David opens a savings account")
savings2 = SavingsAccount("David", 800, 100, "200300405432", "021000021", interest_rate=0.045)
savings2.print_customer_information()

print("\n-> David withdraws $300, then interest is added")
savings2.withdraw(300)
savings2.add_interest()

# ---------------------------------------------------------
# Private / protected demo
# ---------------------------------------------------------
line("Private member demo")
try:
    print(checking1.__routing_number)
except AttributeError as e:
    print("Cannot access private routing number directly:", e)

print("Access through the getter works:", checking1.get_routing_number())