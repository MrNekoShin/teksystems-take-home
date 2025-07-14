import pytest
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
        from src.car import Car
        with pytest.raises(ValueError, match="Invalid car."):
            self.simulation.add_car("Not a car instance")
