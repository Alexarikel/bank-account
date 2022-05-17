import getpass
def read_acc():
    with open("bank.csv", mode="r") as bank_file:
        for line in bank_file.readlines():
            accounts.append(line.split(","))
    return(accounts)
def save_acc(accounts):
    with open("bank.csv", mode="w") as bank_file:
        i = 0
        while i < len(accounts):
            bank_file.write(f"{accounts[i][0]},{accounts[i][1]},{accounts[i][2]},{accounts[i][3]}")
            i += 1
def read_loan():
    with open("loan.csv", mode="r") as loan_file:
        for line in loan_file.readlines():
            loans.append(line.split(","))
    return(loans)
def save_loan(i,loan,rate,period):
    with open("loan.csv", mode="a") as loan_file:
        loan_file.write(f"{accounts[i][3].strip()},{loan},{rate},{period}\n")
        print(f"{accounts[i][3].strip()},{loan},{rate},{period}\n")
        
def authorization():
    us_ps = [input("Enter your name: "), getpass.getpass("Enter you password: ")]
    j = 0
    while j < 3:
        i = 0
        while i < len(accounts):
            if us_ps[0] == accounts[i][0] and us_ps[1] == accounts[i][1]:
                user(i)
            i += 1
        us_ps = [input("Enter your name: "), getpass.getpass("Enter you password: ")]
        j += 1  
    if j == 3:
        return False
def user(i):
    what = input("""Please, select an option:
      S - account status
      W - withdraw
      P - put
      T - transfer
      L - loan calculator
      C - change password
      X - exit
      """)
    if what == "S":
        see(i)
    elif what == "W":
        withdraw(i)
    elif what == "P":
        put(i)
    elif what == "T":
        transfer(i)
    elif what == "L":
        loan_calc(i)
    elif what == "C":
        change_pas(i)
    elif what == "X":
        authorization()
def see(i):
    print(f"You have {accounts[i][2]}$ in your account")
    j = 0
    counter = 0
    while j < len(loans):
        if accounts[i][3].strip() == loans[j][0].strip():
            counter += 1
            print(f"A loan for {loans[j][1]}$ with rate {loans[j][2]}% for {loans[j][3].strip()} months")
        j += 1
    print(f'\tYou have total of {counter} loans')
    user(i)
def withdraw(i):
    amount = float(input("Please, enter an amount: "))
    accounts[i][2] = float(accounts[i][2]) - amount
    print(f"{accounts[i][2]}$ left in your account")
    save_acc(accounts)
    user(i)
def put(i):
    amount = float(input("Please, enter an amount: "))
    accounts[i][2] = float(accounts[i][2]) + amount
    print(f"{accounts[i][2]}$ left in your account")
    save_acc(accounts)
    user(i)
def transfer(i):
    recipient = input("Please, enter a name: ")
    amount = float(input("Please, enter an amount: "))
    for recip in accounts:
        if recip[0] == recipient:
            accounts[i][2] = float(accounts[i][2]) - amount
            recip[2] = float(recip[2]) + amount
    print(f"{accounts[i][2]}$ left in your account")
    save_acc(accounts)
    user(i)
def loan_calc(i):
    loan = float(input("Enter a loan amount, please: "))
    period = float(input("For what period?(months) "))
    rate = float(input("Choose a loan rate, please(%): "))
    mon_rep = (loan * rate / 100 + loan)/period
    a = input(f"""Your monthly repayment is {mon_rep}$
    Enter LN - to confirm a loan
          CL - to change loan terms
          X - to return to the main menu
    """)
    if a == "LN":
        take_ln(i,loan, rate, period)
    elif a == "CL":
        loan_calc(i)
    else:
        user(i)
def take_ln(i,loan,rate,period):
    accounts[i][2] = float(accounts[i][2]) + loan 
    loans.append([accounts[i][3], loan, rate, period])
    print(f"""Congratulations, your account has been credited with {loan}$!
    You have {accounts[i][2]}$ in your account
    """)
    save_loan(i,loan,rate,period)
    save_acc(accounts)
    user(i)
def change_pas(i):
    pas = input("Please, confirm you password: ")
    if pas == accounts[i][1]:
        accounts[i][1] = input("Enter a new password: ")
    save_acc(accounts)
    user(i)
accounts = []
loans = []
read_acc()
read_loan()
authorization()

