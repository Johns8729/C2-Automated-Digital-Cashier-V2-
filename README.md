# 🏦 TECH BANK RIWI DIGITAL – ATM System

## Overview

This project simulates an **ATM (Automated Teller Machine)** built with Python.
The program allows a user to securely access their account and perform common banking operations such as:

* Checking account balance
* Withdrawing money
* Depositing money
* Viewing a transaction history

The system includes **authentication, security limits, and error handling** to ensure safe and controlled operations.

---

# System Workflow

The program is divided into several sections that guide the user through the ATM experience.

---

# 1. Welcome Interface

When the program starts, it displays a **welcome banner** for the bank.

```python
welcome = """
╔════════════════════════════════════════════════════════════╗
    🏦 BIENVENIDO AL CAJERO ATM TECH BANK RIWI DIGITAL 🏦 
╚════════════════════════════════════════════════════════════╝
"""
```

To improve the user experience, the text is printed **character by character** with a small delay.

```python
for _ in welcome:
    print(_,end="",flush=True)
    sleep(0.005)
```

This creates a **smooth animation effect**, similar to what users might see on real ATM machines.

---

# 2. Initial System Configuration

The program defines the **main variables used during the session**.

Examples include:

* `saldo` → The user's account balance (initially set to $1000)
* `pin_correcto` → The correct PIN for authentication
* `intentos_maximos` → Maximum number of login attempts
* `limite_diario_retiro` → Daily withdrawal limit
* `historial` → Stores all transaction records

These variables allow the system to **track operations and enforce security rules**.

---

# 3. User Login (Username Input)

The user is asked to enter their **username** before accessing the system.

```python
cuenta_1 = input("🤵 Ingrese su Nombre de Usuario: ")
```

This name will later appear in **receipts and transaction history**.

---

# 4. Authentication Process (PIN Security)

To access the ATM menu, the user must enter a **valid PIN code**.

Security features include:

* Maximum **3 attempts**
* Only **numeric PINs are accepted**
* The program terminates after too many failed attempts

Example logic:

```python
while intentos < max_intentos:
```

If the correct PIN is entered:

```
Autenticación exitosa, puede continuar al menú principal.
```

Otherwise, the user is warned and the remaining attempts are displayed.

This simulates **basic ATM security authentication**.

---

# 5. Number of Operations

Before entering the main menu, the user chooses **how many operations they want to perform**.

```python
Cant_Operaciones= int(input("¿Cuántas operaciones desea realizar?"))
```

Validation ensures that the number:

* Must be **positive**
* Must be **an integer**

This controls how many times the menu will appear.

---

# 6. Main ATM Menu

For each operation, the program shows the **main menu**:

```
1) 🔍 Check Balance
2) 💳 Withdraw Money
3) 💰 Deposit Money
4) ✅ Finish
```

The user selects the desired action.

Input validation ensures the selection is **within valid menu options**.

---

# 7. Balance Inquiry

If the user selects option **1**, the program displays the current balance.

Example output:

```
Your current balance is: 1000
```

The action is also saved in the transaction history.

---

# 8. Withdraw Money

Option **2** allows the user to withdraw money from their account.

Security validations include:

* The withdrawal amount must be **greater than zero**
* The user must have **sufficient funds**
* The withdrawal must **not exceed the daily limit**

Daily withdrawal limit:

```
$800
```

The system also records:

* **Date of transaction**
* **Time of transaction**

Example information shown after withdrawal:

```
Withdrawal successful
New balance: $850
Daily limit remaining: $650
```

The transaction is stored in the **operation history**.

---

# 9. Deposit Money

Option **3** allows the user to **add funds to the account**.

Validation rules:

* Deposit amount must be **positive**
* Only **numeric values are accepted**

Example result:

```
Your new balance is: $1200
```

The deposit is also recorded in the **transaction history**.

---

# 10. Transaction History

At the end of the session, the system prints a **summary of all actions performed**.

Example output:

```
Transaction History

User: Carlos
🔍 Balance Inquiry
💳 Withdrawal $200
💰 Deposit $300
```

If no actions were performed, the system displays a message indicating **no operations occurred**.

---

# 11. Session Closing

Finally, the program thanks the user for using the ATM.

Example:

```
Thank you Carlos for using the ATM.
```

This simulates the **end of an ATM banking session**.

---

# Key Features

✔ Secure PIN authentication
✔ Input validation and error handling
✔ Daily withdrawal limit control
✔ Transaction history tracking
✔ Date and time registration for withdrawals
✔ Simple and user-friendly interface

---

# Technologies Used

* **Python**
* `time` module (for delays and timestamps)
* `datetime` module (for date tracking)

---

# Conclusion

This project demonstrates how a **basic ATM system can be implemented using Python**.
It provides a realistic banking interaction with authentication, financial operations, and transaction tracking, making it useful for **learning programming logic, control structures, and user input validation**.
