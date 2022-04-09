from string import capwords


class atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balance(self):
        print("Your balance is: $100")

    def cashwithdrawl(self, amount):
        new_amount = 100-amount
        print("You withdrawed:" + str(amount) + "Your remaining balance is:" + str(new_amount))

def main():
    name = input("Hello! What is your name?")
    print("Hello"+name)
    cardnumber = input("Insert your card number: ")
    pin = input("Enter your pin: ")
    new_user = atm(cardnumber, pin)

    print("Choose your activity: ")
    print("1. Balance enquiry")
    print("2. Cash withdrawl")
    activity = int(input("Enter your activity choice: "))

    if(activity == 1):
        new_user.balance()
    elif(activity == 2):
        amount = int(input("Enter your amount: "))
        new_user.cashwithdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()

