@staticmethod
def calculate_velocity(shape1, shape2):
        # Your velocity calculation logic goes here
        # For example, you might calculate the velocity based on the difference in positions of the shapes
        dx = shape2.get_pos()[0] - shape1.get_pos()[0]
        dy = shape2.get_pos()[1] - shape1.get_pos()[1]

        # Assuming a simple frame rate for demonstration purposes
        frame_rate = 30  # frames per second
        velocity_x = dx / frame_rate
        velocity_y = dy / frame_rate

        return velocity_x, velocity_y

@staticmethod
def apply_velocity(shape, velocity):
        # Update the position of the shape based on the calculated velocity
        new_x = shape.get_pos()[0] + velocity[0]
        new_y = shape.get_pos()[1] + velocity[1]

        # Move the shape to the new position
        shape.move_to(new_x, new_y)

        return new_x, new_y

@staticmethod
def handle_immovable(shape, velocity):
        # If the shape is immovable, set its velocity to 0
        if shape.immovable:
            return 0, 0
        else:
            return velocity
