from .shape import Shape
class Velocity():
    def calculate(self, colliding_shape, velocity, graverty=1):
        self.move(velocity[0], 0)
        if self.collide(colliding_shape):
            velocity[0]=-velocity[0]
        self.move(0, velocity[1])
        if self.collide(colliding_shape):
            velocity[1]=-velocity[1]