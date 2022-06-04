from models.tournament import Tournament
from models.player import Player


def read_participants() -> list[str]:
    with open("partecipanti.txt", "r", encoding="utf8") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    names = read_participants()
    players = list(map(lambda n: Player(n), names))
    t = Tournament(players)
    print(t)
