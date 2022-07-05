

class MoneyMachine:
    
    CURRENCY = "$"

    COIN_VALUES = {
        "quaters": 0.25,
        "dimess": 0.1,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_recieved = 0
    
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def process_coins(self, total):
        print("please insert coins")
        for coin in self.COIN_VALUES:
            self.money_recieved += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_recieved
    
    def make_payment(self, cost):
        self.process_coins()
        if self.money_recieved >= cost:
            change = round(self.money_recieved - cost, 2)
            print(f"Here is ${self.CURRENCY}{change} in change")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded")
            return False
        self.money_recieved = 0



