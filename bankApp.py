def main():
    accounts = {}
    account_number = 1000
    while True:
        print("1. Add account\n2. Deposit\n3. Withdraw\n4. Check balance\n5. Check accounts\n6. Exit")
        try:
            selection = int(input("Select the option you want to perform: "))
            if selection == 1:
                addAccount(accounts, account_number)
                account_number += 1  
            elif selection == 2:
                deposit(accounts)
            elif selection == 3:
                withdraw(accounts)
            elif selection == 4:
                checkBalance(accounts)
            elif selection == 5:
                checkAccounts(accounts)
            elif selection == 6:
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid selection.")
        except Exception as e:
            print("An error occurred:", str(e))
    return accounts


def addAccount(accounts, account_number):
    try:
        name = input("Enter name: ")
        first_deposit = int(input("Enter your first deposit: "))
        if name in accounts:
            print("Account already exists")
        elif first_deposit < 0:
            print("Enter a valid amount")
        else:
            accounts[account_number] = {
                "name": name,
                "balance": first_deposit
            }
            print("Account created. Account number:", account_number)
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print("An error occurred:", str(e))


def deposit(accounts):
    try:
        account_number = int(input("Enter account number: "))
        amount = int(input("Enter the amount you want to deposit: "))
        if account_number in accounts:
            accounts[account_number]["balance"] += amount
            print("Deposit successful! Your new balance is:", accounts[account_number]["balance"])
        elif amount < 0:
            print("Enter a valid amount")
        else:
            print("Account not found")
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print("An error occurred:", str(e))


def withdraw(accounts):
    try:
        account_number = int(input("Enter account number: "))
        amount = int(input("Enter the amount you want to withdraw: "))
        if account_number in accounts:
            if amount <= accounts[account_number]["balance"]:
                accounts[account_number]["balance"] -= amount
                print("Withdraw successful! Your new balance is:", accounts[account_number]["balance"])
            elif amount < 0:
                print("Enter a valid amount")
            else:
                print("Insufficient funds")
        else:
            print("Account not found")
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print("An error occurred:", str(e))


def checkBalance(accounts):
    try:
        account_number = int(input("Enter account number: "))
        if account_number in accounts:
            print("Your balance is:", accounts[account_number]["balance"])
        else:
            print("Account not found")
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print("An error occurred:", str(e))


def checkAccounts(accounts):
    try:
        for account_number, account_info in accounts.items():
            print("Account number:", account_number)
            print("Name:", account_info["name"])
            print("Balance:", account_info["balance"], "\n")
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    accounts = main()
