class Atm():
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
        user_input = input("""Hey Dude, How would you like to proceed?
        1. Enter 1 to Create pin
        2. Enter 2 to Deposit
        3. Enter 3 to Withdraw
        4. Enter 4 to Check Balance
        5. Enter 5 to Exit
        """)
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.chkbal()
        elif user_input=='5':
            self.exit()

    def create_pin(self):
        self.pin=input("Create Your Own pin ")
        print("Pin Created SuccessFully")
        self.menu()

    def deposit(self):
        temp = input("Create Your Own pin ")
        if self.pin==temp:
            amount=int(input("Enter the Amount to Deposite"))
            self.balance=self.balance+amount
            print("Successfully Deposited ", self.balance)
        else:
            print("Chor he Tu")
        self.menu()

    def withdraw(self):
        temp = input("Create Your Own pin ")
        if self.pin == temp:
            amt = int(input("Enter to Withdraw"))
            if self.balance>amt:
                self.balance=self.balance-amt
                print("BALANCE: ",self.balance)
            else:
                print("Invalid Input")
        else:
            print("Chor He tu ")
        self.menu()

    def chkbal(self):
        temp = input("Enter the Create pin")
        if temp==self.pin:
            print("Your Balce is", self.balance)
        self.menu()

    def exit(self):
        pass

temp=Atm()