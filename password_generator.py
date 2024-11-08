import random
import string
import time

# Generate a random password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to authenticate user password input
def authenticate(generated_password):
    attempts = 0
    max_attempts = 3
    lockout_time = 30 * 60  # 30 minutes in seconds

    while attempts < max_attempts:
        user_password = input("Enter the password: ")

        if user_password == generated_password:
            print("Access granted!")
            return True
        else:
            attempts += 1
            print("Incorrect password.")

        if attempts >= max_attempts:
            print("Account locked due to too many failed attempts.")
            print("Your security is our priority.")
            time.sleep(lockout_time)  # Lockout for 30 minutes
            attempts = 0  # Reset attempts after lockout

    return False

# Generate and display a password
generated_password = generate_password()
print("Your generated password is:", generated_password)

# Start authentication
authenticate(generated_password)
