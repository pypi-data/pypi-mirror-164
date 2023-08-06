from dataclasses import dataclass
from decimal import Decimal


@dataclass
class JournalEntries:
    to_account: str
    amount: Decimal


@dataclass
class ReverseJournalEntries:
    from_account: str
    amount: Decimal
