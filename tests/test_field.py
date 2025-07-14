"""
Test Module for Field Class.

"""

import pytest
from src.field import Field


class TestField:
    """Test Module for Field Class."""
    def test_field_initialization(self):
        """Test the initialization of the Field class."""
        field = Field(width=10, height=10)
        assert field.width == 10
        assert field.height == 10

    def test_field_initialization_with_invalid_coordinates(self):
        """Test the initialization of the Field class with invalid coordinates."""
        with pytest.raises(ValueError, match="Width and height must be positive integers."):
            Field(width=-1, height=10)
