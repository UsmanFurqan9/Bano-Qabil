import json
import time

accounts = {}
print("Welcome To The Corrupted Bank!")
time.sleep(2.5)
while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. List Accounts\n6. Save Data\n7. Exit")
    choice = input("Enter Your Choice: ")
    if choice == '1':
        name, phone, balance = input("Name: "), input("Phone: "), float(input("Balance: "))
        account_number = len(accounts) + 1
        accounts[account_number] = {'name': name, 'phone': phone, 'balance': balance}
        print(f"Account Created Successfully. Your Account Number Is: {account_number}")
    elif choice in {'2', '3', '4'}:
        search_account = input("Enter Account Number (Or Name,Phone) Separated By A Comma: ")
        if ',' in search_account:
            name, phone = search_account.split(',')
            name, phone = name.strip(), phone.strip()
            account_number = None
            for acc_num, acc_info in accounts.items():
                if acc_info['name'] == name and acc_info['phone'] == phone:
                    account_number = acc_num
                    break
            if account_number is None:
                print("Account Not Found.")
                continue
        else:
            account_number = int(search_account)
        if account_number in accounts:
            if choice == '2':
                amount = float(input("Amount: "))
                accounts[account_number]['balance'] += amount
                print("Deposit Successful.")
            elif choice == '3':
                amount = float(input("Amount: "))
                if amount <= accounts[account_number]['balance']:
                    accounts[account_number]['balance'] -= amount
                    print("Withdrawal Successful.")
                else:
                    print("Insufficient Funds.")
            elif choice == '4':
                print(f"Balance In Account {account_number}: {accounts[account_number]['balance']}")
        else:
            print("Account Not Found.")
    elif choice == '5':
        print("Accounts:", list(accounts.keys()))
    elif choice == '6':
        with open('bank_data.json', 'w') as f:
            json.dump(accounts, f)
        print("Data Saved Successfully.")
    elif choice == '7':
        print("Thank You For Using The Corrupted Bank!")
        break
    else:
        print("Invalid Choice.")
    time.sleep(2.5) 