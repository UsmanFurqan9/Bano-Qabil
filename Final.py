import json
import time

accounts = {}

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. List Accounts\n6. Save Data\n7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name, phone, balance = input("Name: "), input("Phone: "), float(input("Balance: "))
        accounts[len(accounts) + 1] = {'name': name, 'phone': phone, 'balance': balance, 'transactions': []}
        print("Account created successfully.")

    elif choice in {'2', '3'}:
        account_number, amount = int(input("Account: ")), float(input("Amount: "))
        if account_number in accounts:
            if choice == '2':
                accounts[account_number]['balance'] += amount
                accounts[account_number]['transactions'].append({'type': 'Deposit', 'amount': amount})
                print("Deposit successful")
            elif accounts[account_number]['balance'] >= amount:
                accounts[account_number]['balance'] -= amount
                accounts[account_number]['transactions'].append({'type': 'Withdrawal', 'amount': amount})
                print("Withdrawal successful")
            else:
                print("Failed to withdraw. Insufficient balance.")
        else:
            print("Account not found.")

    elif choice == '4':
        query = input("Enter account number or (name, phone) separated by comma: ")
        if ',' in query:
            name, phone = query.split(',')
            found = False
            for acc_num, acc_info in accounts.items():
                if acc_info['name'] == name.strip() and acc_info['phone'] == phone.strip():
                    print("Balance in account {}: {}".format(acc_num, acc_info['balance']))
                    found = True
                    break
            if not found:
                print("Account not found.")
        else:
            account_number = int(query)
            print("Balance in account {}: {}".format(account_number, accounts.get(account_number, {}).get('balance', 'Account not found.')))

    elif choice == '5':
        print("All Account Numbers:", list(accounts.keys()))

    elif choice == '6':
        time.sleep(1)
        with open('bank_data.json', 'w') as f:
            json.dump(accounts, f)
        print("Data saved successfully.")

    elif choice == '7':
        print("Exiting...")
        break

    else:
        print("Invalid choice")

    time.sleep(1)  # Add a delay after each interaction
