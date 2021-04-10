import random
# create budget class
# function that deposit money into each categories
# function that withdraw fund from each categories
# function that check your balance
# function that transfer between categories
# food clothing and entertainment categories
# logic (entry point function that generate fund(for future automation))


class Budget:
    def __init__(self,category_name,category_coffer,spendable):
        self.category_name = category_name
        self.category_coffer = category_coffer
        self.spendable = spendable

    def entry_point(self,choice):
        choice = int(input("Welcome to ZURI BUDGET APP\n 1.transfer to your categories account\n 2. withdraw from your category account\n"
                           " 3.check your coffer balance\n 4.Deposit to your categories account\n 5. logout\n"))
        if choice == 1:
            self.transfer()
        elif choice == 2:
            self.withdrawal()
        elif choice == 3:
            self.balance()
        elif choice == 4:
            self.deposit()
        elif choice == 5:
            self.logout()

    def total_income_generator(self):
        total_income = random.randrange(spendable,category_coffer)
        if total_income < self.spendable:
            print("insufficient fund\n")
        else:
            print(f"the amount you generate this month is: #{total_income}")

    def transfer(self):
        amount = int(input("enter the amount you wish to transfer:\n"))
        if amount < self.category_coffer:
            print("transfer completed\nyou transfer #",amount)
            return amount

    def withdrawal(self):
        print("*"*20,"welcome swiftly withdraw to your categories account","*"*20)
        print("withdrawal page")
        deposit = int(input("enter the amount you wish to withdraw:\n"))
        if deposit < self.category_coffer:
            print("transaction completed\n take your #{} cash your eye go soon clear".format(deposit))
            return deposit

    def balance(self):
        balance = self.category_coffer - self.spendable
        if balance < 0:
            print("you have zero naira to budget with\n go and hustle and return back")
        else:
            print(f"here is your balance:{balance}")

    def deposit(self):
        savings = int(input("enter the amount you wish to save:\n"))
        print(f"you deposit:{savings} into your account")

    def contact_us(self):
        print("thanks for contacting us\nkindly log your complain in the dialog box below \n")
        complaint = input("log your complain here\n")
        return complaint

    def logout(self):
        print("you are been logout of the page\n thanks for your patronage,visit us again for you accurate budget plan")

# work on the money generated here by making use of function so it doesnt break your code or you pass it in as cash like this
category_coffer = random.randrange(5000,15000)
spendable = random.randrange(5000,12000)

# instantiating the app
food = Budget("food",category_coffer,spendable)
entertainment = Budget("food",category_coffer,spendable)
clothing = Budget("cloth",category_coffer,spendable)

print(food.entry_point(1))






'''
i will have love to extend on this more but right now final year project beckon,i hope i will pardon for this sir/ma
function that show all category
contact us page(security,ATM request,chat with our BOT, change your mobile number)
'''