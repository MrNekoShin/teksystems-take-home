from src.car import Car
from src.field import Field


class Simulation:
    """Simulation class to manage the simulation environment."""

    def __init__(self, field_size):
        """Initialize the simulation with a given field size."""
        if not isinstance(field_size, tuple) or len(field_size) != 2 or not all(isinstance(dim, int) and dim > 0 for dim in field_size):
            raise ValueError("Field size must be a tuple of two positive integers.")
        
        self.field = Field(width=field_size[0], height=field_size[1])
        self.cars = {}
        self.car_names = set()

    def add_car(self, car):
        """Add a car to the simulation."""
        if not isinstance(car, Car):
            raise ValueError("Invalid car.")
        
        if car.name in self.car_names:
            raise ValueError("Car with this name already exists.")
        
        #check if the car's position is within the field bounds
        if not (0 <= car.position[0] < self.field.width and 0 <= car.position[1] < self.field.height):
            raise ValueError("Position out of bounds.")
        
        # Get index for car based on add logic (e.g., next available index)
        car_index = len(self.cars)
        self.cars[car_index] = car
        self.car_names.add(car.name)

        
    def move_car(self, car_index):
        """Move a car in the simulation."""
        
        car = self.cars[car_index]

        #check car's next position based on its orientation
        if car.orientation == 'N':
            next_position = (car.position[0], car.position[1] + 1)
        elif car.orientation == 'E':
            next_position = (car.position[0] + 1, car.position[1])
        elif car.orientation == 'S':
            next_position = (car.position[0], car.position[1] - 1)
        elif car.orientation == 'W':
            next_position = (car.position[0] - 1, car.position[1])
        else:
            raise ValueError("Invalid orientation.")
        
        #check if next position is within bounds
        if not (0 <= next_position[0] < self.field.width and 0 <= next_position[1] < self.field.height):
            return False  # Cannot move out of bounds
        
        car.position = next_position

        return True