class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance (default = 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient balance exists. Return True if successful, False otherwise."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
