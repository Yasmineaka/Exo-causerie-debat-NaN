from card import Card

class Epique(Card):
    def __init__(self, nom: str) -> None:
        super().__init__(nom, "epique")