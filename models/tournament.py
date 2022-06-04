from dataclasses import dataclass
from typing import Iterable

from models.player import Player
from models.round import Pairing, Round


def round_robin(p: list[Player]) -> Iterable[list[tuple[Player, Player]]]:

    if len(p) % 2 != 0:
        p.append(Player("Riposo"))

    for i in range(len(p) - 1):
        yield Round(i + 1, list(Pairing(p[i], p[-i - 1]) for i in range(len(p) // 2)))
        p.insert(1, p.pop())


@dataclass
class Tournament:
    participants: list[Player]
    rounds: list[Round]

    def __init__(self, participants: list[Player]) -> None:
        self.participants = participants
        self.rounds = list(round_robin(participants))

    def __repr__(self) -> str:

        s = ""

        for r in self.rounds:
            s += str(r)

        return s
