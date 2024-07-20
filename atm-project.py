accno = int(input("Enter your account no...\n"))
pin = int(input("\nEnter your pin no...\n"))

user_accno = 12345
user_pin = 1111
Balance = 12000
dep = 0
withdraw = 0
inp_no = 0

if accno == user_accno and pin == user_pin:
    attempts = 4
    while attempts > 0:
        print("\n1--Balance")
        print("2--Deposit")
        print("3--Withdraw")
        print("4--Exit\n") 

        inp_no = int(input("Enter the option in number...\n"))

        if inp_no == 1:
            print("\nBalance:", Balance, "$")
        elif inp_no == 2:
            dep = int(input("\nEnter the deposit amount\n"))
            Balance = Balance + dep
            print("\nYour money deposited..", "Balance:", Balance)
        elif inp_no == 3:
            withdraw = int(input("\nEnter the withdraw amount\n"))
            Balance = Balance - withdraw
            print("\nYour money withdrawn..", "Balance:", Balance)
        elif inp_no == 4:
            print("Thank you for choosing our ATM\n")
            break
        else:
            print("\nInvalid option!!!!")

        attempts -= 1
else:
    print("\nInvalid account number or pin number\n")
