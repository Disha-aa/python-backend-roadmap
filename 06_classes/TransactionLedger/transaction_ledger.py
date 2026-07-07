from datetime import datetime
from decimal import Decimal
from pathlib import Path


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, file_path: str, initial_balance: Decimal = Decimal("0.0")):
        self.file_path = file_path
        self._balance = initial_balance

    @property
    def balance(self) -> Decimal:
        return self._balance

    def _log_transaction(
        self, operation: str, amount: Decimal, status: str = "SUCCESS"
    ) -> None:
        log_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        with open(self.file_path, "a") as f:
            f.write(f"[{log_time}] {operation} | {amount} | {status}\n")

    def deposit(self, amount: Decimal) -> None:
        self._balance += amount

        self._log_transaction(self.file_path, "DEPOSIT", amount)

    def withdraw(self, amount: Decimal) -> None:
        if amount > self._balance:
            self._log_transaction("WITHDRAWAL", amount, status="FAILED")
            raise InsufficientFundsError(f"Insufficient funds. Balance: {self.balance}")

        self._balance -= amount
        self._log_transaction("WITHDRAWAL", amount)


def main():
    CURRENT_DIR = Path(__file__).resolve().parent
    LEDGER_PATH = CURRENT_DIR / "ledger.txt"

    bank = BankAccount(LEDGER_PATH)

    bank.deposit(Decimal("175.404"))
    try:
        bank.withdraw(Decimal("1533.14"))
    except InsufficientFundsError as e:
        print(f"Log Review: Request rejected by the bank. Reason: {e}")


if __name__ == "__main__":
    main()
