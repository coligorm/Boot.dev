class BankAccount:
    bank_name = "Boot Bank"
    next_account_number = 1000
    default_daily_withdraw_limit = 200

    def __init__(self, owner_name):
        self.__owner_name = owner_name
        self.__balance = 0
        self.__transactions = []

        self.__account_number = BankAccount.next_account_number
        self.next_account_number += 1

        self.__daily_withdraw_limit = BankAccount.default_daily_withdraw_limit

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, new_owner_name):
        self.__owner_name = new_owner_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_daily_withdraw_limit(self):
        return self.__daily_withdraw_limit

    def set_daily_withdraw_limit(self, limit):
        if type(limit) is not int:
            raise ValueError("daily_withdraw_limit must be an int")
        if limit <= 0:
            raise ValueError("daily_withdraw_limit must be > 0")
        BankAccount.default_daily_withdraw_limit = limit
        self.__daily_withdraw_limit = BankAccount.default_daily_withdraw_limit

    def deposit(self, amount):
        if type(amount) is not int:
            raise ValueError("deposit amount must be an int")
        if amount <= 0:
            raise ValueError("deposit amount must be > 0")

        self.__balance += amount
        self.__transactions.append({"type": "deposit", "amount": amount})

    def withdraw(self, amount):
        if type(amount) is not int:
            raise ValueError("withdraw amount must be an int")
        if amount <= 0:
            raise ValueError("withdraw amount must be > 0")
        if amount > self.__daily_withdraw_limit:
            raise ValueError("withdraw amount exceeds daily limit")
        if amount > self.__balance:
            raise ValueError("insufficient funds")

        self.__balance -= amount
        self.__transactions.append({"type": "withdraw", "amount": amount})

    def get_transactions(self):
        return self.__transactions
