
from typing import Dict, Tuple, Optional


class Car:

    DIRECTIONS_DELTA: Dict[str, Tuple[int, int]] = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, name: str, position: Tuple[int, int], orientation: str, instructions: str) -> None:
        """Initialize the Car with an position and orientation."""

        if orientation not in ['N', 'E', 'S', 'W']:
            raise ValueError("Invalid orientation.")
        
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(coord, int) and coord >= 0 for coord in position):
            raise ValueError("Initial position must be a tuple of two positive integers.")

        if not name:
            raise ValueError("Name cannot be empty.")
        
        if not isinstance(instructions, str):
            raise ValueError("Instructions must be a string.")

        self.name: str = name
        self.position: Tuple[int, int] = position
        self.orientation: str = orientation
        self.instructions: str = instructions
        self.collision: Optional['Car'] = None
        self.collision_step: Optional[int] = None

        
    def __repr__(self) -> str:
        """Return a string representation of the car."""

        if self.collision:
            return f"{self.name}, collides with {self.collision.name} at ({self.position[0]},{self.position[1]}) at step {self.collision_step})"
        else:
            return f"{self.name}, {self.position} {self.orientation}{f", {self.instructions}" if self.instructions else ""}"
    
    def rotate(self, direction: str) -> None:
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
        
    def next_position(self) -> Tuple[int, int]:
        """Calculate the next position based on current orientation."""
        delta = self.DIRECTIONS_DELTA[self.orientation]
        return (self.position[0] + delta[0], self.position[1] + delta[1])
    

    def move(self) -> None:
        """Move the car forward in the current orientation."""
        self.position = self.next_position()

    def collided(self, other_car: 'Car', step: int) -> None:
        """Handle collision with another car."""
        self.collision = other_car
        other_car.collision = self
        self.collision_step = step
        other_car.collision_step = step
    


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