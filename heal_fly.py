from fly import Fly

class HealFly(Fly):
    def __init__(self, turtle_shape):
        super().__init__(turtle_shape)
        self.name = "heal"
