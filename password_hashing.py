import bcrypt

print("===== Password Hashing Login System =====")

username = input("Enter username: ")
password = input("Enter password: ").encode()

salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)

print("\nPassword has been securely hashed.")
print("Stored hash:", hashed_password.decode())

login_password = input("\nEnter password again to login: ").encode()

if bcrypt.checkpw(login_password, hashed_password):
    print("Login successful! ✅")
else:
    print("Login failed! ❌")
