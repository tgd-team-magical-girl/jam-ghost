import ppb
from ppb import keycodes
from ppb.events import KeyPressed, KeyReleased

class Player(ppb.Sprite):


    def __init__(self,image=ppb.Image('magicalgirlbossfight/resources/magicalgirlbossfight.png'), position=ppb.Vector(0, 0)):
        super().__init__()

    def on_update(self,  event: ppb.events.Update, signal):
        self.position += self.move_vector

    def on_key_pressed(self, event: ppb.events.KeyPressed, signal):
        if event.key is keycodes.W:
            self.move_vector += ppb.directions.Up
        elif event.key is keycodes.A:
            self.move_vector += ppb.directions.Left
        elif event.key is keycodes.S:
            self.move_vector += ppb.directions.Down
        elif event.key is keycodes.D:
            self.move_vector += ppb.directions.Right

    def on_key_released(self, event: ppb.events.KeyReleased, signal):
        if event.key is keycodes.W:
            self.move_vector -= ppb.directions.Up
        elif event.key is keycodes.A:
            self.move_vector -= ppb.directions.Left
        elif event.key is keycodes.S:
            self.move_vector -= ppb.directions.Down
        elif event.key is keycodes.D:
            self.move_vector -= ppb.directions.Right
