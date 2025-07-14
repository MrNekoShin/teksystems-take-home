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