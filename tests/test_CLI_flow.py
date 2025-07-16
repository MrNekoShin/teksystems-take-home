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


    def test_main_loop_flow_once(self, mocker):
        """Test the main loop flow of the CLI."""

        side_effects = [
            "20 20",  # Field size
            "1",  # Add car option
            "Car1",  # Car name
            "2 2 N",  # Initial position and orientation
            "FFFFF",  # Car instructions
            "1",
            "Car2",  # Second car name
            "3 3 E",  # Second car initial position and orientation
            "FFFFF",  # Second car instructions
            "2",  # Run simulation option after adding cars
            "2"  # Exit option after simulation
        ]

        mocker.patch('builtins.input', side_effect=side_effects)

        from src.CLI import CLI
        
        self.cli = CLI()
        self.cli.main_loop()
 
        # Check if the field was created
        assert self.cli.simulation.field.height == 20
        assert self.cli.simulation.field.width == 20

        # Check if the cars were added correctly
        assert len(self.cli.simulation.cars) == 2
        assert self.cli.simulation.cars[0].name == "Car1"
        assert self.cli.simulation.cars[1].name == "Car2"
        assert self.cli.simulation.cars[0].instructions == ""
        assert self.cli.simulation.cars[1].instructions == ""
        assert self.cli.simulation.cars[0].position == (2, 7)
        assert self.cli.simulation.cars[1].position == (8, 3)

        assert self.cli.simulation.cars[0].collision is None
        assert self.cli.simulation.cars[1].collision is None

        # Check if the simulation ran without errors
        assert self.cli.simulation.step > 0


    def test_main_loop_flow_multiple(self, mocker):
        """Test the main loop flow of the CLI with multiple iterations."""

        side_effects = [
            "10 10",  # Field size
            "1",  # Add car option
            "Car1",  # Car name
            "0 0 N",  # Initial position and orientation
            "FFF",  # Car instructions
            "2",  # Run simulation option after adding cars
            "1",  # Restart simulation option
            "12 12",  # New field size
            "1",  # Add car option
            "Car2",  # Second car name
            "1 1 E",  # Second car initial position and orientation
            "FF",  # Second car instructions
            "2",  # Run simulation option after adding second car
            "2"  # Exit option after simulation
        ]

        mocker.patch('builtins.input', side_effect=side_effects)

        from src.CLI import CLI
        
        self.cli = CLI()
        self.cli.main_loop()

        # Check if the first field was created
        assert self.cli.simulation.field.height == 12
        assert self.cli.simulation.field.width == 12

        # Check if the first car was added correctly
        assert len(self.cli.simulation.cars) == 1
        assert self.cli.simulation.cars[0].name == "Car2"
        assert self.cli.simulation.cars[0].position == (3, 1)
        assert self.cli.simulation.cars[0].orientation == 'E'
        assert self.cli.simulation.cars[0].instructions == ""

        # Check if the simulation ran without errors
        assert self.cli.simulation.step == 2

    def test_main_loop_flow_invalid_input_retry(self, mocker):
        """Test the main loop flow of the CLI with invalid input."""

        side_effects = [
            "10 a",  # Invalid field size
            "12 12",  # Valid field size
            "3",  # Invalid menu option
            "1",  # Add car option
            "",  # Invalid Car name
            "Car1",  # Valid Car name
            "0 0",  # Invalid Initial position and orientation
            "0 0 N",  # Initial position and orientation
            "FFU",  # Invalid Car instructions
            "FFFF",  # Invalid Car instructions
            "2",  # Run simulation option after adding cars
            "3"  # Invalid option after simulation
            "2"  # Exit option after simulation
        ]


        mocker.patch('builtins.input', side_effect=side_effects)

        from src.CLI import CLI
        
        self.cli = CLI()
        self.cli.main_loop()

        assert self.cli.simulation.field.height == 12
        assert self.cli.simulation.field.width == 12

        # Check if the car was added correctly
        assert len(self.cli.simulation.cars) == 1
        assert self.cli.simulation.cars[0].name == "Car1"
        assert self.cli.simulation.cars[0].position == (0, 4)
        assert self.cli.simulation.cars[0].orientation == 'N'
        assert self.cli.simulation.cars[0].instructions == ""

        

        

        