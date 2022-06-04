from dataclasses import dataclass


@dataclass
class Player:
    name: str

    def __repr__(self) -> str:
        return self.name
