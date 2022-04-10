import getpass

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
    while j < len(loans):
        if accounts[i][3] == loans[j][0]:
            print(f"You have a loan of {loans[j][1]}$")
        j += 1
    user(i)
def withdraw(i):
    amount = int(input("Please, enter an amount: "))
    accounts[i][2] = int(accounts[i][2]) - amount
    print(f"{accounts[i][2]}$ left in your account")
    user(i)
def put(i):
    amount = int(input("Please, enter an amount: "))
    accounts[i][2] = int(accounts[i][2]) + amount
    print(f"{accounts[i][2]}$ left in your account")
    user(i)
def transfer(i):
    recipient = input("Please, enter a name: ")
    amount = int(input("Please, enter an amount: "))
    for recip in accounts:
        if recip[0] == recipient:
            accounts[i][2] = int(accounts[i][2]) - amount
            recip[2] = int(recip[2]) + amount
    print(f"{accounts[i][2]}$ left in your account")
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
    user(i)
def change_pas(i):
    pas = input("Please, confirm you password: ")
    if pas == accounts[i][1]:
        accounts[i][1] = input("Enter a new password: ")
    user(i)
accounts = [
    ["Alex", "12345", 1500,100],
    ["Eugene", "123456", 1500,101]
    ]
loans = []
authorization()
