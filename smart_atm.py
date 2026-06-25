"""
Smart ATM System
================
Features:
  - OOP design (ATM, Account, Transaction, Language, VoiceAssistant classes)
  - Multilingual support: English, Hindi (Devanagari), Punjabi (Gurmukhi)
  - Voice-assisted guidance (pyttsx3 if installed, else text fallback)
  - Secure PIN creation with confirmation + masking via getpass
  - Deposit, Withdraw, Balance Check
  - Transaction History with timestamps
  - Input validation and error handling

Run:
  python3 smart_atm.py

Optional voice:
  pip install pyttsx3
"""

import os
import getpass
from datetime import datetime


# ─────────────────────────────────────────────
# LANGUAGE PACK
# ─────────────────────────────────────────────

class Language:
    """Holds all UI strings for a given language."""

    PACKS = {
        "1": {
            "name": "English",
            "welcome":        "Welcome to Smart ATM!",
            "menu_title":     "\n========= MAIN MENU =========",
            "opt_create_pin": "1. Create PIN",
            "opt_balance":    "2. Check Balance",
            "opt_deposit":    "3. Deposit Money",
            "opt_withdraw":   "4. Withdraw Money",
            "opt_history":    "5. Transaction History",
            "opt_exit":       "6. Exit",
            "enter_choice":   "Enter your choice: ",
            "create_pin":     "Create a new 4-digit PIN: ",
            "confirm_pin":    "Confirm your PIN: ",
            "pin_set":        "[OK]  PIN set successfully!",
            "pin_mismatch":   "[ERR] PINs do not match. Please try again.",
            "enter_pin":      "Enter your PIN: ",
            "pin_wrong":      "[ERR] Incorrect PIN.",
            "no_pin":         "[ERR] No PIN set. Please create a PIN first.",
            "enter_amount":   "Enter amount (Rs.): ",
            "deposited":      "[OK]  Deposit successful!",
            "withdrawn":      "[OK]  Withdrawal successful!",
            "insufficient":   "[ERR] Insufficient balance.",
            "balance_msg":    "Current Balance",
            "history_header": "\n--- Transaction History ---",
            "no_history":     "No transactions yet.",
            "invalid_choice": "[ERR] Invalid choice. Please try again.",
            "invalid_amount": "[ERR] Please enter a valid positive amount.",
            "exit_msg":       "Thank you for using Smart ATM. Goodbye!",
            "pin_too_short":  "[ERR] PIN must be exactly 4 digits.",
            "pin_not_digit":  "[ERR] PIN must contain digits only.",
            "voice_welcome":  "Welcome to Smart ATM. Please select an option.",
            "voice_pin":      "Please enter your 4-digit PIN.",
            "voice_success":  "Transaction completed successfully.",
            "voice_error":    "An error occurred. Please try again.",
            "voice_balance":  "Your current balance is displayed on screen.",
            "voice_exit":     "Thank you. Goodbye.",
            "attempts_left":  "attempt(s) left",
        },

        "2": {
            "name": "हिंदी (Hindi)",
            "welcome":        "स्मार्ट ATM में आपका स्वागत है!",
            "menu_title":     "\n========= मुख्य मेनू =========",
            "opt_create_pin": "1. PIN बनाएं",
            "opt_balance":    "2. बैलेंस देखें",
            "opt_deposit":    "3. पैसे जमा करें",
            "opt_withdraw":   "4. पैसे निकालें",
            "opt_history":    "5. लेन-देन इतिहास",
            "opt_exit":       "6. बाहर जाएं",
            "enter_choice":   "अपना विकल्प चुनें: ",
            "create_pin":     "नया 4-अंकीय PIN बनाएं: ",
            "confirm_pin":    "PIN की पुष्टि करें: ",
            "pin_set":        "[ठीक]  PIN सफलतापूर्वक बना दिया गया!",
            "pin_mismatch":   "[त्रुटि] PIN मेल नहीं खाते। पुनः प्रयास करें।",
            "enter_pin":      "अपना PIN दर्ज करें: ",
            "pin_wrong":      "[त्रुटि] गलत PIN।",
            "no_pin":         "[त्रुटि] PIN नहीं बना है। पहले PIN बनाएं।",
            "enter_amount":   "राशि दर्ज करें (₹): ",
            "deposited":      "[ठीक]  जमा सफल!",
            "withdrawn":      "[ठीक]  निकासी सफल!",
            "insufficient":   "[त्रुटि] अपर्याप्त बैलेंस।",
            "balance_msg":    "वर्तमान शेष",
            "history_header": "\n--- लेन-देन इतिहास ---",
            "no_history":     "अभी तक कोई लेन-देन नहीं।",
            "invalid_choice": "[त्रुटि] अमान्य विकल्प। पुनः प्रयास करें।",
            "invalid_amount": "[त्रुटि] कृपया वैध राशि दर्ज करें।",
            "exit_msg":       "धन्यवाद! अलविदा!",
            "pin_too_short":  "[त्रुटि] PIN ठीक 4 अंकों का होना चाहिए।",
            "pin_not_digit":  "[त्रुटि] PIN में केवल अंक होने चाहिए।",
            "voice_welcome":  "स्मार्ट ATM में आपका स्वागत है। कृपया एक विकल्प चुनें।",
            "voice_pin":      "कृपया अपना 4-अंकीय PIN दर्ज करें।",
            "voice_success":  "लेन-देन सफलतापूर्वक पूर्ण।",
            "voice_error":    "एक त्रुटि हुई। पुनः प्रयास करें।",
            "voice_balance":  "आपका वर्तमान शेष स्क्रीन पर दिखाया गया है।",
            "voice_exit":     "धन्यवाद। अलविदा।",
            "attempts_left":  "प्रयास शेष",
        },

        "3": {
            "name": "ਪੰਜਾਬੀ (Punjabi)",
            "welcome":        "ਸਮਾਰਟ ATM ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!",
            "menu_title":     "\n========= ਮੁੱਖ ਮੀਨੂ =========",
            "opt_create_pin": "1. PIN ਬਣਾਓ",
            "opt_balance":    "2. ਬੈਲੇਂਸ ਦੇਖੋ",
            "opt_deposit":    "3. ਪੈਸੇ ਜਮ੍ਹਾਂ ਕਰੋ",
            "opt_withdraw":   "4. ਪੈਸੇ ਕਢਵਾਓ",
            "opt_history":    "5. ਲੈਣ-ਦੇਣ ਇਤਿਹਾਸ",
            "opt_exit":       "6. ਬਾਹਰ ਜਾਓ",
            "enter_choice":   "ਆਪਣਾ ਵਿਕਲਪ ਚੁਣੋ: ",
            "create_pin":     "ਨਵਾਂ 4-ਅੰਕੀ PIN ਬਣਾਓ: ",
            "confirm_pin":    "PIN ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ: ",
            "pin_set":        "[ਠੀਕ]  PIN ਸਫਲਤਾਪੂਰਵਕ ਬਣਾਇਆ ਗਿਆ!",
            "pin_mismatch":   "[ਗਲਤੀ] PIN ਮੇਲ ਨਹੀਂ ਖਾਂਦੇ। ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।",
            "enter_pin":      "ਆਪਣਾ PIN ਦਾਖਲ ਕਰੋ: ",
            "pin_wrong":      "[ਗਲਤੀ] ਗਲਤ PIN।",
            "no_pin":         "[ਗਲਤੀ] PIN ਸੈੱਟ ਨਹੀਂ ਹੋਇਆ। ਪਹਿਲਾਂ PIN ਬਣਾਓ।",
            "enter_amount":   "ਰਕਮ ਦਾਖਲ ਕਰੋ (₹): ",
            "deposited":      "[ਠੀਕ]  ਜਮ੍ਹਾਂ ਸਫਲ!",
            "withdrawn":      "[ਠੀਕ]  ਕਢਵਾਉਣਾ ਸਫਲ!",
            "insufficient":   "[ਗਲਤੀ] ਨਾਕਾਫ਼ੀ ਬੈਲੇਂਸ।",
            "balance_msg":    "ਮੌਜੂਦਾ ਬੈਲੇਂਸ",
            "history_header": "\n--- ਲੈਣ-ਦੇਣ ਇਤਿਹਾਸ ---",
            "no_history":     "ਹੁਣ ਤੱਕ ਕੋਈ ਲੈਣ-ਦੇਣ ਨਹੀਂ।",
            "invalid_choice": "[ਗਲਤੀ] ਅਮਾਨਯੋਗ ਵਿਕਲਪ। ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।",
            "invalid_amount": "[ਗਲਤੀ] ਕਿਰਪਾ ਕਰਕੇ ਸਹੀ ਰਕਮ ਦਾਖਲ ਕਰੋ।",
            "exit_msg":       "ਧੰਨਵਾਦ! ਅਲਵਿਦਾ!",
            "pin_too_short":  "[ਗਲਤੀ] PIN ਠੀਕ 4 ਅੰਕਾਂ ਦਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।",
            "pin_not_digit":  "[ਗਲਤੀ] PIN ਵਿੱਚ ਕੇਵਲ ਅੰਕ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।",
            "voice_welcome":  "ਸਮਾਰਟ ATM ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ ਵਿਕਲਪ ਚੁਣੋ।",
            "voice_pin":      "ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ 4-ਅੰਕੀ PIN ਦਾਖਲ ਕਰੋ।",
            "voice_success":  "ਲੈਣ-ਦੇਣ ਸਫਲਤਾਪੂਰਵਕ ਪੂਰਾ ਹੋਇਆ।",
            "voice_error":    "ਕੋਈ ਗੜਬੜ ਹੋਈ। ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।",
            "voice_balance":  "ਤੁਹਾਡਾ ਮੌਜੂਦਾ ਬੈਲੇਂਸ ਸਕ੍ਰੀਨ ਤੇ ਦਿਖਾਇਆ ਗਿਆ ਹੈ।",
            "voice_exit":     "ਧੰਨਵਾਦ। ਅਲਵਿਦਾ।",
            "attempts_left":  "ਕੋਸ਼ਿਸ਼ਾਂ ਬਾਕੀ",
        },
    }

    def __init__(self, code="1"):
        self.code  = code
        self._pack = self.PACKS.get(code, self.PACKS["1"])

    def get(self, key):
        return self._pack.get(key, key)

    @classmethod
    def select(cls):
        print("\n" + "=" * 45)
        print("  Select Language / भाषा चुनें / ਭਾਸ਼ਾ ਚੁਣੋ")
        print("=" * 45)
        for code, pack in cls.PACKS.items():
            print(f"  {code}. {pack['name']}")
        while True:
            choice = input("\n  Enter choice (1/2/3): ").strip()
            if choice in cls.PACKS:
                return cls(choice)
            print("  Invalid. Please enter 1, 2, or 3.")


# ─────────────────────────────────────────────
# VOICE ASSISTANT
# ─────────────────────────────────────────────

class VoiceAssistant:
    """
    Speaks text using pyttsx3 when available.
    Gracefully falls back to a printed [Voice] label.
    """

    def __init__(self):
        self._engine = None
        try:
            import pyttsx3
            self._engine = pyttsx3.init()
            self._engine.setProperty("rate", 140)
        except Exception:
            pass

    def speak(self, text):
        print(f"\n  [Voice] {text}")
        if self._engine:
            try:
                self._engine.say(text)
                self._engine.runAndWait()
            except Exception:
                pass


# ─────────────────────────────────────────────
# TRANSACTION
# ─────────────────────────────────────────────

class Transaction:
    """Immutable record of one credit or debit operation."""

    CREDIT = "Credit"
    DEBIT  = "Debit"

    def __init__(self, txn_type, amount, balance_after):
        self.txn_type      = txn_type
        self.amount        = amount
        self.balance_after = balance_after
        self.timestamp     = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __str__(self):
        sign = "+" if self.txn_type == self.CREDIT else "-"
        return (
            f"  [{self.timestamp}]  {self.txn_type:<7}  "
            f"{sign}Rs.{self.amount:>10,.2f}   "
            f"Balance: Rs.{self.balance_after:>10,.2f}"
        )


# ─────────────────────────────────────────────
# ACCOUNT
# ─────────────────────────────────────────────

class Account:
    """
    Manages PIN, balance, and transaction history.
    All account-level business logic lives here.
    """

    MAX_PIN_ATTEMPTS = 3

    def __init__(self, initial_balance=10_000.0):
        self._pin          = None
        self._balance      = initial_balance
        self._transactions = []

    @property
    def has_pin(self):
        return self._pin is not None

    def set_pin(self, pin):
        self._pin = pin

    def verify_pin(self, entered):
        return self._pin == entered

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(
            Transaction(Transaction.CREDIT, amount, self._balance)
        )

    def withdraw(self, amount):
        """Returns True on success, False when funds are insufficient."""
        if amount > self._balance:
            return False
        self._balance -= amount
        self._transactions.append(
            Transaction(Transaction.DEBIT, amount, self._balance)
        )
        return True

    @property
    def transactions(self):
        return self._transactions


# ─────────────────────────────────────────────
# ATM  (main controller)
# ─────────────────────────────────────────────

class ATM:
    """
    Main ATM controller.
    Coordinates Language, VoiceAssistant, and Account objects.
    """

    def __init__(self):
        self._lang    = Language.select()
        self._voice   = VoiceAssistant()
        self._account = Account()
        self._running = True

    # ── Helpers ──────────────────────────────

    def _t(self, key):
        return self._lang.get(key)

    def _speak(self, key):
        self._voice.speak(self._t(key))

    def _divider(self):
        print("-" * 45)

    def _get_pin_masked(self, prompt_key):
        """Read PIN silently (no terminal echo)."""
        try:
            return getpass.getpass(self._t(prompt_key))
        except Exception:
            return input(self._t(prompt_key))

    def _get_amount(self):
        """Prompt for a positive numeric amount. Returns float or None."""
        raw = input(self._t("enter_amount")).strip()
        try:
            amount = float(raw)
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print(self._t("invalid_amount"))
            return None

    def _validate_pin(self, pin):
        """Return an error-key if invalid, else None."""
        if not pin.isdigit():
            return "pin_not_digit"
        if len(pin) != 4:
            return "pin_too_short"
        return None

    def _authenticate(self):
        """
        Verifies the user PIN (up to MAX_PIN_ATTEMPTS tries).
        Returns True if authenticated.
        """
        if not self._account.has_pin:
            print(self._t("no_pin"))
            return False

        self._speak("voice_pin")
        for attempt in range(1, Account.MAX_PIN_ATTEMPTS + 1):
            entered   = self._get_pin_masked("enter_pin")
            if self._account.verify_pin(entered):
                return True
            remaining = Account.MAX_PIN_ATTEMPTS - attempt
            if remaining > 0:
                print(f"{self._t('pin_wrong')} ({remaining} {self._t('attempts_left')})")
            else:
                print(self._t("pin_wrong"))
                self._speak("voice_error")
        return False

    # ── Menu operations ──────────────────────

    def _create_pin(self):
        self._speak("voice_pin")
        while True:
            pin = self._get_pin_masked("create_pin")
            err = self._validate_pin(pin)
            if err:
                print(self._t(err))
                continue
            confirm = self._get_pin_masked("confirm_pin")
            if pin != confirm:
                print(self._t("pin_mismatch"))
                continue
            self._account.set_pin(pin)
            print(self._t("pin_set"))
            self._speak("voice_success")
            break

    def _check_balance(self):
        if not self._authenticate():
            return
        self._speak("voice_balance")
        self._divider()
        print(f"  {self._t('balance_msg')}: Rs.{self._account.balance:,.2f}")
        self._divider()

    def _deposit(self):
        if not self._authenticate():
            return
        amount = self._get_amount()
        if amount is None:
            self._speak("voice_error")
            return
        self._account.deposit(amount)
        print(self._t("deposited"))
        print(f"  {self._t('balance_msg')}: Rs.{self._account.balance:,.2f}")
        self._speak("voice_success")

    def _withdraw(self):
        if not self._authenticate():
            return
        amount = self._get_amount()
        if amount is None:
            self._speak("voice_error")
            return
        if self._account.withdraw(amount):
            print(self._t("withdrawn"))
            print(f"  {self._t('balance_msg')}: Rs.{self._account.balance:,.2f}")
            self._speak("voice_success")
        else:
            print(self._t("insufficient"))
            self._speak("voice_error")

    def _show_history(self):
        if not self._authenticate():
            return
        print(self._t("history_header"))
        self._divider()
        txns = self._account.transactions
        if not txns:
            print(f"  {self._t('no_history')}")
        else:
            for txn in txns:
                print(txn)
        self._divider()

    def _show_menu(self):
        print(self._t("menu_title"))
        self._divider()
        for key in [
            "opt_create_pin", "opt_balance", "opt_deposit",
            "opt_withdraw",   "opt_history", "opt_exit",
        ]:
            print(f"  {self._t(key)}")
        self._divider()

    # ── Main loop ────────────────────────────

    def run(self):
        self._speak("voice_welcome")
        print(f"\n  {self._t('welcome')}")

        ACTIONS = {
            "1": self._create_pin,
            "2": self._check_balance,
            "3": self._deposit,
            "4": self._withdraw,
            "5": self._show_history,
        }

        while self._running:
            self._show_menu()
            choice = input(self._t("enter_choice")).strip()

            if choice in ACTIONS:
                ACTIONS[choice]()
            elif choice == "6":
                self._speak("voice_exit")
                print(f"\n  {self._t('exit_msg')}\n")
                self._running = False
            else:
                print(self._t("invalid_choice"))


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    atm = ATM()
    atm.run()
