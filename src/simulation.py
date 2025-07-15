try:
    # Try absolute imports first (for pytest, imports from outside)
    from src.car import Car
    from src.field import Field
except ImportError:
    # Fall back to direct imports (for running directly)
    from car import Car
    from field import Field


class Simulation:
    """Simulation class to manage the simulation environment."""

    def __init__(self, field_size):
        """Initialize the simulation with a given field size."""
        if not isinstance(field_size, tuple) or len(field_size) != 2 or not all(isinstance(dim, int) and dim > 0 for dim in field_size):
            raise ValueError("Field size must be a tuple of two positive integers.")
        
        self.field = Field(width=field_size[0], height=field_size[1])
        self.cars = {}
        self.car_names = set()
        self.cars_in_field = {}
        self.step = 0  # Track the simulation step

    def add_car(self, car):
        """Add a car to the simulation."""
        if not isinstance(car, Car):
            raise ValueError("Invalid car.")
        
        if car.name in self.car_names:
            raise ValueError("Car with this name already exists.")
        
        if car.position in self.cars_in_field:
            raise ValueError("Position already occupied by another car.")
        
        #check if the car's position is within the field bounds
        if not (0 <= car.position[0] < self.field.width and 0 <= car.position[1] < self.field.height):
            raise ValueError("Position out of bounds.")
        
        # Get index for car based on add logic (e.g., next available index)
        car_index = len(self.cars)
        self.cars[car_index] = car
        self.cars_in_field[car.position] = car
        self.car_names.add(car.name)

        
    def move_car(self, car_index):
        """Move a car in the simulation."""
        
        car = self.cars[car_index]

        #check if car has collided
        if car.collision:
            return False

        #remove car from current position in the field
        if car in self.cars_in_field:
            del self.cars_in_field[car.position]

        next_position = car.next_position()
        
        #check if next position is within bounds
        if not (0 <= next_position[0] < self.field.width and 0 <= next_position[1] < self.field.height):
            return False  # Cannot move out of bounds
        
        car.move()

        # Check for collisions with other cars
        if next_position in self.cars_in_field:
            other_car = self.cars_in_field[next_position]
            car.collided(other_car, self.step)
            self.cars_in_field[next_position] = [car, other_car]
            
        else:
            # Update car's position in the field
            self.cars_in_field[next_position] = car


        return True
    
    def execute_instructions(self, car_index):
        """Execute the instructions for a car."""
        car = self.cars[car_index]

        if car.collision:
            return  # Do not execute instructions if the car has collided

        curr_command = car.instructions[0] if car.instructions else None

        if curr_command == 'F':
            self.move_car(car_index)
        elif curr_command == 'L':
            car.rotate('L')
        elif curr_command == 'R':
            car.rotate('R')

        car.instructions = car.instructions[1:]  # Remove the executed command
    
    def run_simulation(self):
        """Run the simulation by executing all car instructions."""
        
        while True:
            # Check if all cars have either no instructions left or have collided
            if all(car.instructions == "" or car.collision for car in self.cars.values()):
                break
            
            self.step += 1  # Increment the simulation step after each round of instructions
            
            # Execute instructions for each car
            for car_index in range(len(self.cars)):
                self.execute_instructions(car_index)
            

            

if __name__ == "__main__":
    simulation = Simulation(field_size=(10, 10))
    car1 = Car(name="Car1", position=(0, 0), orientation='N', instructions="")
    car2 = Car(name="Car2", position=(1, 1), orientation='W', instructions="")

    simulation.add_car(car1)
    simulation.add_car(car2)

    print("Initial car positions:")
    for car in simulation.cars.values():
        print(car)

    # Move car1
    simulation.move_car(0)
    print("\nAfter moving Car1:")
    for car in simulation.cars.values():
        print(car)

    # Move car2 to collide with car1
    simulation.move_car(1)
    print("\nAfter moving Car2 to collide with Car1:")
    for car in simulation.cars.values():
        print(car)

