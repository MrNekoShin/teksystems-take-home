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

    def test_add_car_with_same_name(self):
        """Test adding a car with the same name."""
        from src.car import Car
        car1 = Car(name="SameNameCar", position=(0, 0), orientation='N', instructions="")
        car2 = Car(name="SameNameCar", position=(1, 1), orientation='E', instructions="")
                
        with pytest.raises(ValueError, match="Car with this name already exists."):
            self.simulation.add_car(car1)
            self.simulation.add_car(car2)

    def add_car_with_invalid_position(self):
        """Test adding a car with an invalid position."""
        from src.car import Car
        car = Car(name="InvalidPositionCar", position=(10, 10), orientation='N', instructions="")
        with pytest.raises(ValueError, match="Position out of bounds."):
            self.simulation.add_car(car)
        
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
        
