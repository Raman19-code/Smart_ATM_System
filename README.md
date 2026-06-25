# Smart_ATM_System
Smart ATM System is a Python-based OOP project that simulates ATM operations such as PIN creation, balance inquiry, cash deposit, withdrawal, and transaction history. It features multilingual support (English, Hindi, Punjabi) and voice guidance, making ATM services more accessible, secure, and user-friendly.
# Smart ATM System

## Overview

Smart ATM System is a Python-based Object-Oriented Programming (OOP) project designed to simulate the functionality of an Automated Teller Machine (ATM). The project focuses on accessibility and user convenience by providing multilingual support and voice-assisted guidance.

The system allows users to securely create a PIN, deposit money, withdraw funds, check account balances, and view transaction history. It is designed as a learning project to demonstrate OOP concepts, software design principles, and user-friendly banking operations.

---

## Problem Statement

Many ATM users, especially elderly individuals, first-time users, and people who are not comfortable with a single language interface, face difficulties while performing banking operations. Traditional ATM systems often lack personalized guidance and multilingual accessibility.

This project aims to address these challenges by developing a Smart ATM System that supports multiple languages and voice guidance, making ATM operations easier and more accessible for a wider range of users.

---

## Features

### Current Features

* PIN Creation and Verification
* Secure PIN Input
* Deposit Money
* Withdraw Money
* Balance Inquiry
* Transaction History
* Input Validation
* Error Handling
* Multilingual Support

  * English
  * Hindi
  * Punjabi
* Voice Guidance Support
* Object-Oriented Design

### Planned Features

* SQLite Database Integration
* Speech Recognition
* Account Locking After Multiple Failed Attempts
* Change PIN Functionality
* GUI Interface using Tkinter
* AI-powered Banking Assistant
* Multiple User Accounts

---

## Technologies Used

### Programming Language

* Python 3

### OOP Concepts

* Classes and Objects
* Constructors
* Encapsulation
* Composition
* Properties
* Modular Programming

### Libraries

* getpass
* datetime
* pyttsx3 (Voice Assistant)

---

## Project Structure

```text
Smart-ATM-System/
│
├── main.py
├── README.md
├── requirements.txt
│
├── atm/
│   ├── atm.py
│   ├── account.py
│   ├── transaction.py
│   ├── language.py
│   └── voice_assistant.py
│
├── data/
│   ├── users.json
│   └── transactions.json
│
└── docs/
    ├── problem_statement.md
    └── screenshots/
```

---

## Class Design

### ATM Class

Controls the application flow and user interactions.

### Account Class

Manages account balance, PIN verification, deposits, and withdrawals.

### Transaction Class

Stores transaction details with timestamps.

### Language Class

Handles multilingual text and language selection.

### VoiceAssistant Class

Provides voice-based guidance using text-to-speech technology.

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/Smart-ATM-System.git
cd Smart-ATM-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python main.py
```

---

## Sample Operations

1. Select preferred language.
2. Create a secure 4-digit PIN.
3. Deposit money.
4. Withdraw money.
5. Check account balance.
6. View transaction history.
7. Exit the system.

---

## Learning Outcomes

This project helped in understanding:

* Object-Oriented Programming (OOP)
* Software Design Principles
* Python Class Architecture
* Encapsulation and Data Management
* Transaction Handling
* Localization (Multilingual Support)
* Voice Assistant Integration
* Input Validation and Error Handling

---

## Future Scope

* Speech-to-Text ATM Commands
* Database Integration
* ATM Card Simulation
* Biometric Authentication
* AI Chatbot Support
* Mobile Banking Integration
* Fraud Detection System

---

## Author

Ramandeep Kaur

Computer Science Engineering (AI & ML)

Python | OOP | AI/ML Enthusiast

