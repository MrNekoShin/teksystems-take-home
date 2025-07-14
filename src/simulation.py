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

    def add_car(self, car):
        """Add a car to the simulation."""
        if not isinstance(car, Car):
            raise ValueError("Invalid car.")
        
        self.cars[0] = car

        