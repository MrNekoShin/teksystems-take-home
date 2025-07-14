import pytest
from src.car import Car

class TestCarInitialization:
    """Test Module for Car Class."""
    def test_car_initialization(self):
        """Test the initialization of the Car class."""
        car = Car(name="Test", position=(0, 0), orientation='N', instructions="")
        
        assert car.name == "Test"
        assert car.position == (0, 0)
        assert car.orientation == 'N'
        assert car.instructions == ""

    def test_car_initialization_with_empty_name(self):
        """Test the initialization of the Car class with an empty name."""
        with pytest.raises(ValueError, match="Name cannot be empty."):
            Car(name="", position=(0, 0), orientation='N', instructions="")

    def test_car_initialization_with_invalid_orientation(self):
        """Test the initialization of the Car class with invalid orientation."""
        with pytest.raises(ValueError, match="Invalid orientation."):
            Car(name="Test", position=(0, 0), orientation='X', instructions="")

    def test_car_initialization_with_invalid_initial_position(self):
        """Test the initialization of the Car class with invalid initial position."""
        with pytest.raises(ValueError, match="Initial position must be a tuple of two positive integers."):
            Car(name="Test", position=(0, -1), orientation='N', instructions="")

class TestCarRotation:
    """Test Module for Car Class Rotation."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup a car instance for testing."""
        self.car = Car(name="TestCar", position=(0, 0), orientation='N', instructions="")
        
    def test_car_rotation_left(self):
        """Test the car's left rotation."""
        self.car.rotate('L')
        assert self.car.orientation == 'W'

    def test_car_rotation_right(self):
        """Test the car's right rotation."""
        self.car.rotate('R')
        assert self.car.orientation == 'E'

    def test_car_invalid_rotation(self):
        """Test the car's invalid rotation."""
        with pytest.raises(ValueError, match="Invalid rotation command."):
            self.car.rotate('X')
