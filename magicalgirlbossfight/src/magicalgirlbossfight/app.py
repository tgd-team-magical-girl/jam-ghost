"""
A game jam game of Magical Girls and big boss fights.
"""
import ppb


class magicalgirlbossfight(ppb.BaseScene):
    def __init__(self, **props):
        super().__init__(**props)

        self.add(ppb.Sprite(
            image=ppb.Image('magicalgirlbossfight/resources/magicalgirlbossfight.png'),
        ))


def main():
    ppb.run(
        starting_scene=magicalgirlbossfight,
        title='magical-girl-boss-fight',
    )
