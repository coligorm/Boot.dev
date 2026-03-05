class TokenPouch:
    def __init__(self, starting_tokens):
        self.__validate_amount(starting_tokens)
        self.__tokens = starting_tokens

    @property
    def tokens(self):
        return self.__tokens

    def deposit(self, amount):
        self.__validate_amount(amount)
        self.__tokens += amount
        return self.__tokens

    def withdraw(self, amount):
        self.__validate_amount(amount)
        self.__validate_funds(amount)
        self.__tokens -= amount
        return self.__tokens

    def transfer_to(self, other_pouch, amount):
        if type(other_pouch) is not TokenPouch:
            raise TypeError("other_pouch must be a TokenPouch")
        self.__validate_amount(amount)
        self.__validate_funds(amount)
        self.__tokens -= amount
        other_pouch.__tokens += amount
        return (self.__tokens, other_pouch.__tokens)
            
    def __validate_amount(self, amount):
        if type(amount) is not int or amount <= 0:
            raise ValueError("amount must be an int > 0")

    def __validate_funds(self, amount):
        if self.__tokens < amount:
            raise ValueError("insufficient tokens")
 