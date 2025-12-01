#step1:importing bcrypt  
import bcrypt
import os

#step6: creating a user.txt file 
USER_FILE = "users.txt"

# -----------------------------
# PASSWORD SECURITY (bcrypt)
# -----------------------------
#step2:Implement the Password Hashing Function
def hash_password(password):
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")

#Step 3: Implement the Password Verification Function
def verify_password(password, hashed_password):
    password_bytes = password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)

# -----------------------------
# USER VALIDATION
# -----------------------------
#Step 4: Implement the Password Verification Function

def validate_username(username):
    if username.strip() == "":
        return False, "Username cannot be empty."
    if " " in username:
        return False, "Username cannot contain spaces."
    return True, ""

def validate_password(password):
    if password.strip() == "":
        return False, "Password cannot be empty."
    if len(password) < 5:
        return False, "Password must be at least 5 characters long."
    if " " in password:
        return False, "Password cannot contain spaces."
    return True, ""
# -----------------------------
# USER REGISTRATION
# -----------------------------
#step 5: Implement the Registration Function

def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False

    with open(USER_FILE, "r") as file:
        for line in file:
            if ":" not in line:
                continue
            stored_username = line.split(":")[0].strip()  # IMPORTANT FIX
            if stored_username == username:
                return True
    return False

#Step 6:  Implement the User Existence Check
def register_user(username, password):
    if user_exists(username):
        return "Error: User already exists."

    hashed_pw = hash_password(password)

    with open(USER_FILE, "a") as file:
        file.write(f"{username}:{hashed_pw}\n")

    return f"Success: User '{username}' registered successfully!"

# -----------------------------
# USER LOGIN
# -----------------------------
#Step 7: Implement the Login Function
def login_user(username, password):
    if not os.path.exists(USER_FILE):
        return "Error: No users registered yet."

    with open(USER_FILE, "r") as file:
        for line in file:
            if ":" not in line:
                continue

            stored_username, stored_hash = line.strip().split(":")

            if stored_username == username:
                if verify_password(password, stored_hash):
                    return f"Success: WELCOME BACK, {username}!"
                else:
                    return "Error: Incorrect password."

    return "Error: Username not found."

# -----------------------------
# MENU AND MAIN LOOP
# -----------------------------
#step 8 : displaying menu 
def display_menu():
    print("\n" + "=" * 50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)


def main():
    print("\nWelcome to the Multi-Domain Intelligence Platform")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        # OPTION 1: REGISTRATION
        if choice == "1":
            print("\n---- USER REGISTRATION ----")

            username = input("Enter a username: ").strip()
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"\nError: {error_msg}")
                continue

            password = input("Enter a password: ").strip()
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"\nError: {error_msg}")
                continue

            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("\nError: Passwords do not match.")
                continue

            print("\n" + register_user(username, password))

        # OPTION 2: LOGIN
        elif choice == "2":
            print("\n---- USER LOGIN ----")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            result = login_user(username, password)
            print("\n" + result)

        # OPTION 3: EXIT
        elif choice == "3":
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break

        # INVALID OPTION
        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")


main()
