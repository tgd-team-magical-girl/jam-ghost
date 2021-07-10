"""
A game jam game of Magical Girls and big boss fights.
"""
import ppb
import players
from magicalgirlbossfight.players import Player

class magicalgirlbossfight(ppb.BaseScene):
    def __init__(self, **props):
        super().__init__(**props)

        self.add(Player())


def main():
    ppb.run(
        starting_scene=magicalgirlbossfight,
        title='magical-girl-boss-fight',
    )
