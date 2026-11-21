# 🔐 TOTP-Based Two-Factor Authentication System

A Python-based **Multi-User Two-Factor Authentication (2FA) System** that implements Time-Based One-Time Password (TOTP) authentication with encrypted secret storage.

This project demonstrates how an additional authentication layer can improve account security by requiring users to verify their identity using a time-based one-time password generated through an authenticator application.

---

## 📌 Project Overview

Passwords alone may not provide sufficient protection against unauthorized access. Two-Factor Authentication (2FA) adds another verification layer to the login process.

This project implements a multi-user TOTP authentication system in Python. Each registered user receives a unique TOTP secret, which is converted into a QR code for enrollment with an authenticator application.

The application verifies time-based OTPs and encrypts stored TOTP secrets using Fernet symmetric encryption.

## ✨ Key Features

- **Multi-User Registration:** Supports registration of multiple users with unique usernames.
- **TOTP Authentication:** Generates and verifies time-based one-time passwords.
- **QR Code Generation:** Generates QR codes for authenticator application enrollment.
- **Unique Secret Generation:** Creates a separate TOTP secret for every registered user.
- **Encrypted Secret Storage:** Uses Fernet encryption to protect stored TOTP secrets.
- **Username Validation:** Validates usernames and prevents duplicate registrations.
- **OTP Verification:** Checks OTP validity during registration and authentication.
- **Invalid OTP Handling:** Rejects invalid or expired OTPs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyOTP | TOTP generation and verification |
| QRCode | QR code generation |
| Cryptography (Fernet) | Encryption of stored TOTP secrets |
| JSON | User data storage |

## ⚙️ Project Structure

```text
TOTP-2FA-System/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

Runtime files generated locally:

```text
├── secret.key
├── users.json
└── qrcodes/
```

These runtime files are excluded from the public repository because they contain sensitive authentication material or local application data.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Narra-Nikhilesh/TOTP-2FA-System.git
```

### 2. Navigate to the Project Directory

```bash
cd TOTP-2FA-System
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

On the first run, the application initializes its local encryption key and creates the required runtime directories and data files.

## 🔄 How It Works

### 1. User Registration
- The user enters a username.
- The application validates the username.
- Duplicate usernames are rejected.
- A unique TOTP secret is generated for the new user.

### 2. QR Code Enrollment
- The application generates a TOTP provisioning URI.
- A QR code is created from that URI.
- The user scans the QR code using a compatible authenticator application.

### 3. Enrollment Verification
- The user enters the OTP displayed by the authenticator application.
- The application verifies the OTP.
- Registration succeeds only when the OTP is valid.

### 4. Encrypted Storage
- The TOTP secret is encrypted using Fernet.
- The encrypted secret is stored in the local JSON user database.

### 5. User Authentication
- The user enters their username and current OTP.
- The application retrieves and decrypts the corresponding TOTP secret.
- PyOTP verifies the submitted OTP.
- Access verification succeeds only when the OTP is valid.

## 🔒 Security Features

- Unique TOTP secrets for individual users.
- Fernet encryption for stored TOTP secrets.
- Duplicate username prevention.
- OTP validation during registration.
- Rejection of invalid or expired OTPs.
- Sensitive runtime files excluded through `.gitignore`.

**Security Note:** The Fernet encryption key must be protected separately from the encrypted user database. Anyone who obtains both may be able to decrypt the stored TOTP secrets. Never upload `secret.key`, `users.json`, or generated QR codes to a public repository.

## 🧪 Testing

The application was tested with the following scenarios:

| Test Case | Expected Result |
|---|---|
| Register a new user | Registration successful |
| Register an existing username | Duplicate username rejected |
| Enter a valid enrollment OTP | Registration successful |
| Enter an invalid or expired OTP | Registration rejected |
| Verify a user with a valid OTP | Authentication successful |
| Verify a user with an invalid OTP | Authentication rejected |

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding Time-Based One-Time Password authentication.
- Implementing multi-user authentication.
- Working with PyOTP and QR code generation.
- Applying symmetric encryption using Fernet.
- Handling user data using JSON.
- Implementing input validation and error handling.
- Understanding the importance of protecting authentication secrets.

## 🔮 Future Enhancements

- Graphical user interface (GUI).
- Password-based authentication combined with TOTP.
- Account recovery and secret-key rotation.
- Improved authentication logging and monitoring.
- Database integration.
- Rate limiting and account lockout mechanisms.

## 👨‍💻 Author

**Narra Nikhilesh Yadav**

B.Tech – Computer Science and Engineering

Interests: Cybersecurity | Artificial Intelligence | Emerging Technologies

## 📄 License

This project is available for educational and learning purposes. A formal open-source license can be added separately if the project is intended for reuse and redistribution.
