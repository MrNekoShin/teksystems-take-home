
class Car:

    def __init__(self, name, position, orientation, instructions):
        """Initialize the Car with an position and orientation."""

        if orientation not in ['N', 'E', 'S', 'W']:
            raise ValueError("Invalid orientation.")
        
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(coord, int) and coord >= 0 for coord in position):
            raise ValueError("Initial position must be a tuple of two positive integers.")

        if not name:
            raise ValueError("Name cannot be empty.")
        
        if not isinstance(instructions, str):
            raise ValueError("Instructions must be a string.")

        self.name = name
        self.position = position
        self.orientation = orientation
        self.instructions = instructions

        
    def __repr__(self):
        return f"{self.name}, {self.position} {self.orientation}, {self.instructions}"
    
    def rotate(self, direction):
        """Rotate the car left or right."""
        if direction not in ['L', 'R']:
            raise ValueError("Invalid rotation command.")
        
        orientations = ['N', 'E', 'S', 'W']
        idx = orientations.index(self.orientation)
        
        if direction == 'L':
            idx = (idx - 1) % len(orientations)
        elif direction == 'R':
            idx = (idx + 1) % len(orientations)
        
        self.orientation = orientations[idx]
        
    def move(self):
        """Move the car forward in the current orientation."""
        if self.orientation == 'N':
            self.position = (self.position[0], self.position[1] + 1)
        elif self.orientation == 'E':
            self.position = (self.position[0] + 1, self.position[1])
        elif self.orientation == 'S':
            self.position = (self.position[0], self.position[1] - 1)
        elif self.orientation == 'W':
            self.position = (self.position[0] - 1, self.position[1])
        


if __name__ == "__main__":
    # Create some example cars
    car1 = Car(name="Rover1", position=(0, 0), orientation='N', instructions="")
    car2 = Car(name="Explorer", position=(5, 3), orientation='E', instructions="FFLFRFF")
    car3 = Car(name="Scout", position=(10, 10), orientation='S', instructions="RFLLFR")
    
    print("Car representations:")
    print(f"Car 1: {repr(car1)}")
    print(f"Car 2: {repr(car2)}")
    print(f"Car 3: {repr(car3)}")
    
    print("\nDirect print (uses __repr__):")
    print(car1)
    print(car2)
    print(car3)