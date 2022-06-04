from dataclasses import dataclass
from models.pairing import Pairing
from models.pairing import LINE_LEN


@dataclass
class Round:
    number: int
    pairings: list[Pairing]

    def __repr__(self) -> str:
        s = "\n" + f"Round {self.number}".center(LINE_LEN) + "\n"
        for p in self.pairings:
            s += str(p)

        return s
