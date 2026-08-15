import random
import string

passwords = {}

# Load existing passwords from file
try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*_()-+"
    password = "".join(random.choice(chars) for _ in range(8))
    return password


def save_all_to_file():
    """Sob password re-write kore file e save kore"""
    with open("password.txt", "w") as file:
        for site, pwd in passwords.items():
            file.write(f"{site}:{pwd}\n")


while True:
    print("\n-----PERSONAL PASSWORD MANAGER---")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Exit")

    choice = input("Enter your choice ")

    if choice == "1":
        site = input("Enter website: ")
        pwd = input("Enter password: ")

        passwords[site] = pwd

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!")

    elif choice == "2":
        if not passwords:
            print("No data")
        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)

    elif choice == "3":
        print("Generated password:", generate_password())

    elif choice == "4":
        site = input("Enter website to update: ")

        if site not in passwords:
            print("Website not found!")
        else:
            old_pwd = input("Enter current password: ")

            if old_pwd != passwords[site]:
                print("Wrong current password!")
            else:
                choice2 = input("Generate new password automatically? (y/n): ")

                if choice2.lower() == "y":
                    new_pwd = generate_password()
                    print("New password generated:", new_pwd)
                else:
                    new_pwd = input("Enter new password: ")

                passwords[site] = new_pwd
                save_all_to_file()
                print("Password updated successfully!")

    elif choice == "5":
        site = input("Enter website to delete: ")

        if site not in passwords:
            print("Website not found!")
        else:
            confirm = input(f"Are you sure you want to delete '{site}'? (y/n): ")
            if confirm.lower() == "y":
                del passwords[site]
                save_all_to_file()
                print("Password deleted successfully!")
            else:
                print("Cancelled.")

    elif choice == "6":
        print("Ok bye...")
        break

    else:
        print("Invalid input")
