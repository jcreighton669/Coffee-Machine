class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents

        if self.cents > 99:
            temp_cents = self.cents % 100
            temp_dollars = self.cents // 100
            self.dollars += temp_dollars
            self.cents = temp_cents

