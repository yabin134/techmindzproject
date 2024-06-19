class Account:

    def __init__(self, accnumber, name, initialbalance):
        self.accnumber = accnumber
        self.name = name
        self.balance = initialbalance
        self.transactionhistory = []

    def deposit(self, amount):
        self.balance += amount
        self.transactionhistory.append(f"Deposited Rs{amount}")
        print(f"Deposited Rs{amount}. New balance: Rs{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactionhistory.append(f"Withdrew Rs{amount}")
            print(f"Withdrew Rs{amount}. New balance: Rs{self.balance}")
        else:
            print("LOW Balance")

    def showbalance(self):
        print(f"Current balance: Rs{self.balance}")

    def savetransactionhistory(self):
        with open(f"{self.accnumber}_transactionhistory.txt", "w") as file:
            for transaction in self.transactionhistory:
                file.write(transaction + "\n")

    def main():
        accounts = {}
        while True:
            print("\nWelcome to the Bank Of Kochi")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Show Balance")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                accnumber = input("Enter account number: ")
                if accnumber in accounts:
                    print("Account number already exists!")
                    continue
                name = input("Enter account holder name: ")
                try:
                    initialbalance = float(input("Enter initial balance: "))
                    accounts[accnumber] = Account(accnumber, name, initialbalance)
                    print(f"Account created for {name} with balance Rs{initialbalance}")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for initial balance")
            elif choice == "2":
                accnumber = input("Enter account number: ")
                if accnumber in accounts:
                    try:
                        amount = float(input("Enter amount to deposit: "))
                        accounts[accnumber].deposit(amount)
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                else:
                    print("Account not found")

            elif choice == "3":
                accnumber = input("Enter account number: ")
                if accnumber in accounts:
                    try:
                        amount = float(input("Enter amount to withdraw: "))
                        accounts[accnumber].withdraw(amount)
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                else:
                    print("Account not found")

            elif choice == "4":
                accnumber = input("Enter account number: ")
                if accnumber in accounts:
                    accounts[accnumber].showbalance()
                else:
                    print("Account not found")

            elif choice == "5":
                for acc in accounts.values():
                    acc.savetransactionhistory()
                print("Exiting the system. Transaction histories saved.")
                break

            else:
                print("Invalid choice, please try again.")

# Run the main method
if __name__ == "__main__":
    Account.main()
