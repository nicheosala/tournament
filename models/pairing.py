from dataclasses import dataclass

from models.player import Player
from models.config import LINE_LEN

@dataclass
class Pairing:
    p1: Player
    p2: Player

    def __repr__(self) -> str:
        return f"{str(self.p1).ljust((LINE_LEN - 1) // 2)}VS{str(self.p2).rjust((LINE_LEN - 2) // 2)}\n"
