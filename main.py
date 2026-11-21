
# # import pyotp
# # import os

# # # Step 1: Check whether a secret key already exists
# # if os.path.exists("secret.txt"):

# #     # Load the existing secret key
# #     with open("secret.txt", "r") as file:
# #         secret = file.read().strip()

# #     print("Existing Secret Key Loaded!")

# # else:

# #     # Generate a new secret key
# #     secret = pyotp.random_base32()

# #     # Save the secret key
# #     with open("secret.txt", "w") as file:
# #         file.write(secret)

# #     print("New Secret Key Generated!")

# # # Step 2: Create TOTP object
# # totp = pyotp.TOTP(secret)

# # # Step 3: Generate current OTP
# # otp = totp.now()

# # print("\nYour Secret Key:", secret)
# # print("Your Current OTP:", otp)

# # # Step 4: Verify OTP
# # user_otp = input("\nEnter OTP: ").strip()

# # if totp.verify(user_otp):
# #     print("OTP Verified Successfully!")
# #     print("Access Granted!")
# # else:
# #     print("Invalid OTP!")
# #     print("Access Denied!")

# import pyotp
# import qrcode
# import json
# import os
# import re

# from cryptography.fernet import Fernet


# #  Define file names
# USER_FILE = "users.json"
# KEY_FILE = "secret.key"
# QR_FOLDER = "qrcodes"


# # Generate or load encryption key
# def load_encryption_key():

#     if os.path.exists(KEY_FILE):

#         with open(KEY_FILE, "rb") as file:
#             key = file.read()

#     else:

#         key = Fernet.generate_key()

#         with open(KEY_FILE, "wb") as file:
#             file.write(key)

#     return Fernet(key)


# # Encrypt the secret
# def encrypt_secret(secret):

#     encrypted_secret = cipher.encrypt(secret.encode())

#     return encrypted_secret.decode()


# # Decrypt the secret
# def decrypt_secret(encrypted_secret):

#     decrypted_secret = cipher.decrypt(
#         encrypted_secret.encode()
#     )

#     return decrypted_secret.decode()

# # Load users
# def load_users():

#     if os.path.exists(USER_FILE):

#         with open(USER_FILE, "r") as file:
#             return json.load(file)

#     return {}

# # Save users
# def save_users(users):

#     with open(USER_FILE, "w") as file:

#         json.dump(users, file, indent=4)


# # Build the registration system
# # Register user
# def register_user(users):

#     username = input("Enter a username: ").strip()

#     if not re.fullmatch(r"[A-Za-z0-9_-]{3,30}", username):
#         print("Username must be 3-30 characters using letters, numbers, _ or -.")
#         return

#     if username in users:
#         print("User already registered!")
#         return

#     # Generate a unique TOTP secret
#     secret = pyotp.random_base32()

#     # Create TOTP object
#     totp = pyotp.TOTP(secret)

#     # Generate QR provisioning URI
#     uri = totp.provisioning_uri(
#         name=username,
#         issuer_name="TOTP Security Project"
#     )

#     # Create QR code
#     qr = qrcode.make(uri)

#     # Save QR code
#     qr_path = os.path.join(QR_FOLDER, username + ".png")
#     qr.save(qr_path)

#     print("\nQR code generated successfully!")
#     print("QR code location:", qr_path)
#     print("Scan it using Google Authenticator.")

#     # Confirm enrollment using an OTP
#     enrollment_otp = input("Enter the OTP displayed in your Authenticator: ").strip()

#     if not totp.verify(enrollment_otp):
#         os.remove(qr_path)
#         print("Registration failed! Invalid or expired OTP.")
#         return

#     # Encrypt the secret
#     encrypted_secret = encrypt_secret(secret)

#     # Store encrypted secret
#     users[username] = {
#         "secret": encrypted_secret
#     }

#     save_users(users)

#     print("\nRegistration successful!")
#     print("Your TOTP secret has been encrypted and saved.")


import pyotp
import qrcode
import json
import os
import re

from cryptography.fernet import Fernet


# File names
USER_FILE = "users.json"
KEY_FILE = "secret.key"
QR_FOLDER = "qrcodes"


# Load or generate encryption key
def load_encryption_key():

    if os.path.exists(KEY_FILE):

        with open(KEY_FILE, "rb") as file:
            key = file.read()

    else:

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

    return Fernet(key)


# Encrypt TOTP secret
def encrypt_secret(secret):

    encrypted_secret = cipher.encrypt(secret.encode())

    return encrypted_secret.decode()


# Decrypt TOTP secret
def decrypt_secret(encrypted_secret):

    decrypted_secret = cipher.decrypt(
        encrypted_secret.encode()
    )

    return decrypted_secret.decode()


# Load registered users
def load_users():

    if os.path.exists(USER_FILE):

        with open(USER_FILE, "r") as file:
            return json.load(file)

    return {}


# Save registered users
def save_users(users):

    with open(USER_FILE, "w") as file:

        json.dump(users, file, indent=4)


# Register new user
def register_user(users):

    username = input("Enter a username: ").strip()

    if not re.fullmatch(r"[A-Za-z0-9_-]{3,30}", username):
        print("Username must be 3-30 characters using letters, numbers, _ or -.")
        return

    if username in users:
        print("User already registered!")
        return

    # Generate unique TOTP secret
    secret = pyotp.random_base32()

    # Create TOTP object
    totp = pyotp.TOTP(secret)

    # Generate provisioning URI
    uri = totp.provisioning_uri(
        name=username,
        issuer_name="TOTP Security Project"
    )

    # Generate QR code
    qr = qrcode.make(uri)

    qr_path = os.path.join(QR_FOLDER, username + ".png")
    qr.save(qr_path)

    print("\nQR code generated successfully!")
    print("QR code location:", qr_path)
    print("Scan it using Google Authenticator.")

    # Confirm enrollment
    enrollment_otp = input(
        "Enter the OTP displayed in your Authenticator: "
    ).strip()

    if not totp.verify(enrollment_otp):
        os.remove(qr_path)
        print("Registration failed! Invalid or expired OTP.")
        return

    # Encrypt and save the secret
    encrypted_secret = encrypt_secret(secret)

    users[username] = {
        "secret": encrypted_secret
    }

    save_users(users)

    print("\nRegistration successful!")
    print("TOTP secret encrypted and saved successfully.")


# Verify user OTP
def verify_user(users):

    username = input("Enter your username: ").strip()

    if username not in users:
        print("User not registered!")
        return

    # Read encrypted secret
    encrypted_secret = users[username]["secret"]

    # Decrypt secret
    secret = decrypt_secret(encrypted_secret)

    # Create TOTP object
    totp = pyotp.TOTP(secret)

    # Get OTP from user
    user_otp = input("Enter OTP from Authenticator: ").strip()

    # Verify OTP
    if totp.verify(user_otp):

        print("\nOTP verified successfully!")
        print("Access Granted!")

    else:

        print("\nInvalid or expired OTP!")
        print("Access Denied!")


# Main application
def main():

    global cipher

    # Create QR folder
    os.makedirs(QR_FOLDER, exist_ok=True)

    # Initialize encryption
    cipher = load_encryption_key()

    # Load users
    users = load_users()

    while True:

        print("\n===== TOTP TWO-FACTOR AUTHENTICATION =====")
        print("1. Register New User")
        print("2. Verify OTP")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            register_user(users)

        elif choice == "2":

            verify_user(users)

        elif choice == "3":

            print("Exiting application...")
            break

        else:

            print("Invalid choice!")


# Start program
if __name__ == "__main__":
    main()
