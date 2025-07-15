import pytest
from src.car import Car
from src.simulation import Simulation

class TestSimulationInitialization:
    """Test Module for Simulation Class."""
    
    def test_simulation_initialization(self):
        """Test the initialization of the Simulation class."""
        simulation = Simulation(field_size=(10, 10))
        
        assert simulation.field.height == 10
        assert simulation.field.width == 10

    def test_simulation_initialization_with_invalid_field_size(self):
        """Test the initialization of the Simulation class with invalid field size."""
        with pytest.raises(ValueError, match="Field size must be a tuple of two positive integers."):
            Simulation(field_size=(-10, 10))

    def test_simulation_initialization_with_non_tuple_field_size(self):
        """Test the initialization of the Simulation class with non-tuple field size."""
        with pytest.raises(ValueError, match="Field size must be a tuple of two positive integers."):
            Simulation(field_size=[10, 10])

    def test_simulation_initialization_with_non_integer_field_size(self):
        """Test the initialization of the Simulation class with non-integer field size."""
        with pytest.raises(ValueError, match="Field size must be a tuple of two positive integers."):
            Simulation(field_size=(10, '10'))

    def test_simulation_initialization_with_empty_field_size(self):
        """Test the initialization of the Simulation class with empty field size."""
        with pytest.raises(ValueError, match="Field size must be a tuple of two positive integers."):
            Simulation(field_size=())


class TestSimulationCarManagement:
    """Test Module for Car Management in Simulation Class."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup a simulation instance for testing."""
        self.simulation = Simulation(field_size=(10, 10))

    def test_add_car(self):
        """Test adding a car to the simulation."""
        from src.car import Car
        car = Car(name="TestCar", position=(0, 0), orientation='N', instructions="")
        self.simulation.add_car(car)
        
        assert len(self.simulation.cars) == 1
        assert self.simulation.cars[0].name == "TestCar"
    
    def test_add_invalid_car(self):
        """Test adding an invalid car to the simulation."""
        with pytest.raises(ValueError, match="Invalid car."):
            self.simulation.add_car("Not a car instance")

    def add_car_with_invalid_position(self):
        """Test adding a car with an invalid position."""
        from src.car import Car
        car = Car(name="InvalidPositionCar", position=(10, 10), orientation='N', instructions="")
        with pytest.raises(ValueError, match="Position out of bounds."):
            self.simulation.add_car(car)

    def test_add_multiple_cars(self):
        """Test adding multiple cars to the simulation."""
        from src.car import Car
        car1 = Car(name="Car1", position=(0, 0), orientation='N', instructions="")
        car2 = Car(name="Car2", position=(1, 1), orientation='E', instructions="")
        
        self.simulation.add_car(car1)
        self.simulation.add_car(car2)
        
        assert len(self.simulation.cars) == 2
        assert self.simulation.cars[0].name == "Car1"
        assert self.simulation.cars[1].name == "Car2"

    def test_add_multiple_cars_with_same_name(self):
        """Test adding a car with the same name."""
        from src.car import Car
        car1 = Car(name="SameNameCar", position=(0, 0), orientation='N', instructions="")
        car2 = Car(name="SameNameCar", position=(1, 1), orientation='E', instructions="")
                
        self.simulation.add_car(car1)

        with pytest.raises(ValueError, match="Car with this name already exists."):
            self.simulation.add_car(car2)
    
    def test_add_multiple_cars_with_same_position(self):
        """Test adding multiple cars with the same position."""
        from src.car import Car
        car1 = Car(name="Car1", position=(0, 0), orientation='N', instructions="")
        car2 = Car(name="Car2", position=(0, 0), orientation='E', instructions="")
        
        self.simulation.add_car(car1)
        
        with pytest.raises(ValueError, match="Position already occupied by another car."):
            self.simulation.add_car(car2)
        
class TestSimulationCarFieldMovement:
    """Test Module for Car Movement in Simulation Class."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup a simulation instance for testing."""
        self.simulation = Simulation(field_size=(10, 10))
        self.simulation.add_car(Car(name="TestCarA", position=(0, 0), orientation='N', instructions=""))

    def test_move_car_within_bounds(self):
        """Test moving a car within the field bounds."""
        car = self.simulation.cars[0]
        car.position = (0, 0)
        car.orientation = 'N'

        # Test Simulation's move method
        valid = self.simulation.move_car(0)
        assert valid is True
        assert car.position == (0, 1)

    def test_move_car_out_of_bounds(self):
        """Test moving a car out of the field bounds."""
        car = self.simulation.cars[0]
        car.position = (0, 9)  # Near the top edge
        car.orientation = 'N'
    
        valid = self.simulation.move_car(0)
        assert valid is False
        assert car.position == (0, 9)  # Position should not change if out of bounds

        car.orientation = 'W'  # Change orientation to West
        valid = self.simulation.move_car(0)
        assert valid is False
        assert car.position == (0, 9)

        car.orientation = 'E'  # Change orientation to East
        car.position = (9, 0)  # Near the right edge
        valid = self.simulation.move_car(0)
        assert valid is False
        assert car.position == (9, 0)

        car.orientation = 'S'  # Change orientation to South
        valid = self.simulation.move_car(0)
        assert valid is False
        assert car.position == (9, 0)

    def test_move_car_to_edge(self):
        """Test moving a car to the edge of the field."""
        car = self.simulation.cars[0]
        car.position = (8, 8)
        car.orientation = 'E'  # Facing East

        valid = self.simulation.move_car(0)
        assert valid is True
        assert car.position == (9, 8)
        
        car.orientation = 'N'
        valid = self.simulation.move_car(0)
        assert valid is True
        assert car.position == (9, 9)

        car.position = (1, 1)
        car.orientation = 'S'  # Facing South
        valid = self.simulation.move_car(0)
        assert valid is True
        assert car.position == (1, 0)

        car.orientation = 'W'
        valid = self.simulation.move_car(0)
        assert valid is True
        assert car.position == (0, 0)  

        
class TestSimulationCarCollision:
    """Test Module for Car Collision in Simulation Class."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup a simulation instance for testing."""
        self.simulation = Simulation(field_size=(10, 10))
        self.simulation.add_car(Car(name="Car1", position=(0, 0), orientation='N', instructions=""))
        self.simulation.add_car(Car(name="Car2", position=(1, 0), orientation='W', instructions=""))

    def test_move_cars_into_each_other(self):
        """Test moving two cars into the same position."""
        car1 = self.simulation.cars[0]
        car2 = self.simulation.cars[1]

        #Move Car2 to collide with Car1
        valid = self.simulation.move_car(1)
        assert valid is True
        assert car1.collision.name == "Car2"
        assert car2.collision.name == "Car1"
        assert car1.position == (0, 0)
        assert car2.position == (0, 0)

    def test_moving_collided_cars(self):
        """Test moving cars after a collision."""

        car1 = self.simulation.cars[0]
        car2 = self.simulation.cars[1]

        # Move them into each other
        valid = self.simulation.move_car(1)  # Move Car2
        assert valid is True
        assert car1.collision.name == "Car2"
        assert car2.collision.name == "Car1"
        assert car1.position == (0, 0)
        assert car2.position == (0, 0)

        # Try to move them again
        valid1 = self.simulation.move_car(0)
        valid2 = self.simulation.move_car(1)

        assert valid1 is False
        assert valid2 is False
        assert car1.position == (0, 0)
        assert car2.position == (0, 0)
        assert car1 in self.simulation.cars_in_field[(0, 0)]
        assert car2 in self.simulation.cars_in_field[(0, 0)]


class TestSimulationInstructions:
    """Test Module for Car Instructions in Simulation Class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup a simulation instance for testing."""
        self.simulation = Simulation(field_size=(10, 10))
        self.simulation.add_car(Car(name="TestCar", position=(0, 0), orientation='N', instructions=""))

    def test_car_no_instructions_execution(self):
        """Test executing instructions when no instructions are available."""
        car = self.simulation.cars[0]
        car.instructions = ""

        self.simulation.execute_instructions(0)
        
        assert car.position == (0, 0)

    def test_car_forward_instructions_execution(self):
        """Test executing car instructions."""
        car = self.simulation.cars[0]
        car.instructions = "F"

        self.simulation.execute_instructions(0)
        
        assert car.position == (0, 1)

    def test_car_multiple_instructions_execution(self):
        """Test executing multiple instructions for a car."""
        car = self.simulation.cars[0]
        car.instructions = "FF"

        self.simulation.execute_instructions(0)
        assert car.position == (0, 1)
        assert car.instructions == "F"  # Remaining instruction after first execution

        self.simulation.execute_instructions(0)
        assert car.position == (0, 2)
        assert car.instructions == ""  # No remaining instructions after second execution

    def test_car_rotation_right_instructions_execution(self):
        """Test executing rotation instructions for a car."""
        car = self.simulation.cars[0]
        car.instructions = "RR"

        self.simulation.execute_instructions(0)

        assert car.orientation == 'E'
        assert car.position == (0, 0)  # Position should not change on rotation

        self.simulation.execute_instructions(0)
        assert car.orientation == 'S'
        assert car.position == (0, 0)

    def test_car_rotation_left_instructions_execution(self):
        """Test executing rotation instructions for a car."""
        car = self.simulation.cars[0]
        car.instructions = "LL"

        self.simulation.execute_instructions(0)
        
        assert car.orientation == 'W'
        assert car.position == (0, 0)

        self.simulation.execute_instructions(0)

        assert car.orientation == 'S'
        assert car.position == (0, 0)

    def test_car_combined_rotation_instructions_execution(self):
        """Test executing a combination of forward and rotation instructions."""
        car = self.simulation.cars[0]
        car.instructions = "RL"

        self.simulation.execute_instructions(0)
        assert car.orientation == 'E'
        assert car.position == (0, 0)
        
        self.simulation.execute_instructions(0)
        assert car.orientation == 'N'
        assert car.position == (0, 0)


    def test_car_combined_instructions_execution(self):
        """Test executing a combination of forward and rotation instructions."""
        car = self.simulation.cars[0]
        car.instructions = "FRF"

        self.simulation.execute_instructions(0)
        assert car.position == (0, 1)  # Move forward
        assert car.orientation == 'N'  # Orientation should remain the same
        
        self.simulation.execute_instructions(0)
        assert car.position == (0, 1)  # Still at (0, 1) after rotation
        assert car.orientation == 'E'

        self.simulation.execute_instructions(0)
        assert car.position == (1, 1)  # Move forward again
        assert car.orientation == 'E'  # Orientation should remain the same


class TestSimulationCarCollisionInstructionsExecution:
    """Test Module for Car Collision during Instructions Execution in Simulation Class."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup a simulation instance for testing."""
        self.simulation = Simulation(field_size=(10, 10))
        self.simulation.add_car(Car(name="Car1", position=(0, 0), orientation='N', instructions=""))
        self.simulation.add_car(Car(name="Car2", position=(0, 1), orientation='S', instructions=""))

    def test_car_instructions_execution_with_collision(self):
        """Test executing instructions when a collision occurs."""
        car1 = self.simulation.cars[0]
        car2 = self.simulation.cars[1]

        # Set instructions to collide
        car1.instructions = "F"
        car2.instructions = "F"

        # Run simulation instructions
        self.simulation.run_simulation()

        # Car1 should collide with Car2
        assert car1.collision.name == "Car2"
        assert car2.collision.name == "Car1"
        
        # Both cars should exist in the same position
        assert car1.position == (0, 1)
        assert car2.position == (0, 1)

        # Check if cars are in the field at the same position
        assert (0, 1) in self.simulation.cars_in_field
        assert len(self.simulation.cars_in_field[(0, 1)]) == 2
        assert car1 in self.simulation.cars_in_field[(0, 1)]
        assert car2 in self.simulation.cars_in_field[(0, 1)]

        assert car1.instructions == ""
        assert car2.instructions == "F" # Car2 still has an instruction to execute