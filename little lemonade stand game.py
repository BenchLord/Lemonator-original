from random import randint
import sys

class Stand: 
    def __init__(self,balance,lemons):
        self.balance = balance
        self.lemons = lemons
        
    def sell(self):
        cost = raw_input("How much do you charge for your lemonade?(please use whole numbers)\nHow much: ")
        try:
            costN = int(cost)
            for n in range(100):
                if randint(0,costN) == 1:
                    self.balance += costN
                    self.lemons -= 1
                    if self.lemons <= 0:
                        if self.balance < 3:
                            print "You ran out of lemons and don't have enough money to buy more, GAME OVER!"
                            sys.exit
                        else:
                            print "You ran out of lemons, time to buy more!"
                            self.buy()
                            break
                        
        except:
            print "That's not a whole number!"
            
    def buy(self):
        oldBalance = self.balance
        oldLemons = self.lemons
        choice = raw_input("Lemons are 3 dollars, you have " + str(self.balance) + " dollars, how many do you want to buy?\nHow many:")
        try:
            choiceN = int(choice)
            self.lemons += choiceN
            self.balance -= 3 * choiceN
            if self.balance < 0:
                self.lemons = oldLemons
                self.balance = oldBalance
                print "You can't buy that many, you don't have enough money."
        except:
            print "You can't do that?"

def main():
    print "==Welcome to Lemons==\n The goal of this game is to get money! you can:\n Buy Lemons\n Quit the game\n or Open up your stand to sell your lemonade!"
    user = Stand(0, 100)
    running = True
    while running:
        print "You have " + str(user.balance) + " dollars, and " + str(user.lemons) + " lemons."
        choice = raw_input("QUIT, BUY, or SELL\nWhat do you do: ")
        choiceN = choice.lower()
        if choiceN == "sell":
            user.sell()
        if choiceN == "quit":
            running = False
        if choiceN == "buy":
            user.buy()

if __name__ == '__main__':
    main()
