

def authorization():
    us_ps = [input("Enter your name: "), input("Enter you password: ")]
    j = 0
    while j < 3:
        i = 0
        while i < len(accounts):
            if us_ps[0] == accounts[i][0] and us_ps[1] == accounts[i][1]:
                user(i)
            i += 1
        us_ps = [input("Enter your name: "), input("Enter you password: ")]
        j += 1  
    if j == 3:
        return False
def user(i):
    what = input("Please, choose an option: S-to see amount of money; W-to withdraw money; P-to put money; T-to transfer money; C-change password; X-to exit ")
    if what == "S":
        see(i)
    elif what == "W":
        withdraw(i)
    elif what == "P":
        put(i)
    elif what == "T":
        transfer(i)
    elif what == "C":
        change_pas(i)
    elif what == "X":
        authorization()
def see(i):
    print(f"You have {accounts[i][2]}$ in your account")
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
def change_pas(i):
    pas = input("Please, confirm you password: ")
    if pas == accounts[i][1]:
        accounts[i][1] = input("Enter a new password: ")
    user(i)
accounts = [
    ["Alex", "12345", 1500],
    ["Eugene", "123456", 1500]
    ]
authorization()
