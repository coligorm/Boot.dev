class TokenPouch:
    def __init__(self, starting_tokens):
        self.starting_tokens = starting_tokens

    @property
    def tokens(self):
        return self.starting_tokens

    def deposit(self, amount):
        self.__validate_amount(amount)
        self.starting_tokens += amount
        return self.starting_tokens

    def withdraw(self, amount):
        self.__validate_amount(amount)
        self.__validate_funds(self.starting_tokens, amount)
        self.starting_tokens -= amount
        return self.starting_tokens

    def transfer_to(self, other_pouch, amount):
        if type(other_pouch) != TokenPouch:
            raise TypeError
        self.__validate_amount(amount)
        self.__validate_funds(self.starting_tokens, amount)
        self.starting_tokens -= amount
        other_pouch.starting_tokens += amount
        return (self.starting_tokens, other_pouch.starting_tokens)
            

    def __validate_amount(self, amount):
        if type(amount) != int or amount <= 0:
            raise ValueError
        else:
            return True

    def __validate_funds(self, tokens, amount):
        if tokens < amount:
            raise ValueError
        else:
            return True
        
        