import pytest


class TestCLIFlows:
    """Test cases for the CLI flows."""

    def test_add_car_loop_flow(self, mocker):
        """Test the flow of adding a car to the simulation."""

        side_effects = [
            "1",  # Add car option
            "Car1",  # Car name
            "2 2 N",  # Initial position and orientation
            "FRFLF",  # Car instructions
            "1",  #  Add another car option
            "Car2",  # Second car name
            "3 3 E",  # Second car initial position and orientation
            "FFRFF",  # Second car instructions
            "2"  # Exit option
        ]


        mocker.patch('builtins.input', side_effect=side_effects)

        from src.CLI import CLI
        from src.simulation import Simulation

        self.cli = CLI()
        self.cli.simulation = Simulation(field_size=(5, 5))

        self.cli.add_car_loop()

        # Check if the cars were added correctly
        assert len(self.cli.simulation.cars) == 2
        assert self.cli.simulation.cars[0].name == "Car1"
        assert self.cli.simulation.cars[0].position == (2, 2)
        assert self.cli.simulation.cars[0].orientation == 'N'
        assert self.cli.simulation.cars[0].instructions == "FRFLF"

        assert self.cli.simulation.cars[1].name == "Car2"
        assert self.cli.simulation.cars[1].position == (3, 3)
        assert self.cli.simulation.cars[1].orientation == 'E'
        assert self.cli.simulation.cars[1].instructions == "FFRFF"
