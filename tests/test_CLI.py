import pytest
from src.CLI import CLI

class TestCLIMessages:
    """Test cases for the CLI class."""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to run before each test."""
        self.cli = CLI()

    def test_cli_initialization(self):
        """Test the CLI initialization."""
        assert self.cli is not None, "CLI should be initialized successfully."

    def test_cli_welcome_message(self, capsys):
        """Test the CLI welcome message."""
        self.cli.welcome()

        captured = capsys.readouterr()
        assert "Welcome to Auto Driving Car Simulation!\n" in captured.out, "Welcome message should be displayed."

    def test_cli_create_field_message(self, capsys):
        """Test the CLI create field method."""

        self.cli.create_field_message()

        captured = capsys.readouterr()
        assert "Please enter the width and height of the simulation field in x y format:" in captured.out, "Field creation message should be displayed."

    def test_cli_field_created_message(self, capsys):
        """Test the CLI field created message."""
        width, height = 10, 10
        self.cli.field_created_message(width, height)

        captured = capsys.readouterr()
        assert f"You have created a field of {width} x {height}." in captured.out, "Field creation confirmation should be displayed."

    def test_cli_options_menu_message(self, capsys):
        """Test the CLI options menu message."""
        self.cli.options_menu_message()
        
        captured = capsys.readouterr()
        assert "Please choose from the following options:" in captured.out, "Options menu message should be displayed."
        assert "[1] Add a car to field" in captured.out, "Option to add a car should be displayed."
        assert "[2] Run simulation" in captured.out, "Option to run simulation should be displayed."

    def test_cli_add_car_name_message(self, capsys):
        """Test the CLI add car message."""
        self.cli.add_car_name_message()
        
        captured = capsys.readouterr()
        assert "Please enter the name of the car:" in captured.out, "Car name prompt should be displayed."

    def test_cli_add_car_initial_position_and_orientation_message(self, capsys):
        """Test the CLI add car position message."""

        car_name = "TestCar"

        self.cli.add_car_initial_position_and_orientation_message(car_name)
        
        captured = capsys.readouterr()
        assert f"Please enter initial position of car {car_name} in x y Direction format:" in captured.out, "Car position prompt should be displayed."

    def test_cli_add_car_instructions_message(self, capsys):
        """Test the CLI add car instructions message."""
        car_name = "TestCar"

        self.cli.add_car_instructions_message(car_name)
        
        captured = capsys.readouterr()
        assert f"Please enter the commands for car {car_name}:" in captured.out, "Car instructions prompt should be displayed."

    def test_cli_list_no_cars_message(self, capsys):
        """Test the CLI list cars message."""
        self.cli.list_cars_message()
        
        captured = capsys.readouterr()
        assert "Your current list of cars are:" in captured.out, "List cars message should be displayed."


    def test_cli_list_cars_with_details(self, capsys):
        """Test the CLI list cars with details."""
        from src.simulation import Simulation
        from src.car import Car
    
        self.cli.simulation = Simulation(field_size=(10, 10))
        self.cli.simulation.add_car(Car(name="B", position=(1, 2), orientation='N', instructions="FFRFFFFRRL"))

        self.cli.list_cars_message()
        
        captured = capsys.readouterr()

        assert "B, (1, 2) N, FFRFFFFRRL" in captured.out, "Car details should be displayed."

    def test_cli_list_multiple_cars(self, capsys):
        """Test the CLI list multiple cars."""
        from src.simulation import Simulation
        from src.car import Car
    
        self.cli.simulation = Simulation(field_size=(10, 10))
        self.cli.simulation.add_car(Car(name="Car1", position=(0, 0), orientation='N', instructions="F"))
        self.cli.simulation.add_car(Car(name="Car2", position=(1, 1), orientation='W', instructions="L"))
        
        self.cli.list_cars_message()

        captured = capsys.readouterr()
        assert "Your current list of cars are:" in captured.out, "List of cars message should be displayed."

        assert "Car1, (0, 0) N, F" in captured.out, "First car details should be displayed."
        assert "Car2, (1, 1) W, L" in captured.out, "Second car details should be displayed."

    def test_cli_simulation_results_message(self, capsys):
        """Test the CLI simulation results message."""
        from src.simulation import Simulation
        from src.car import Car
        self.cli.simulation = Simulation(field_size=(10, 10))
        self.cli.simulation.add_car(Car(name="Car1", position=(0, 0), orientation='N', instructions="F"))
        self.cli.simulation.add_car(Car(name="Car2", position=(1, 1), orientation='W', instructions="L"))
        self.cli.simulation_results_message()

        captured = capsys.readouterr()
        assert "After simulation, the result is:" in captured.out, "Simulation results message should be displayed."
        assert "Car1, (0, 0) N, F" in captured.out, "First car results should be displayed."
        assert "Car2, (1, 1) W, L" in captured.out, "Second car results should be displayed."

    def test_cli_after_simulation_options_menu_message(self, capsys):
        """Test the CLI options menu after simulation."""
        self.cli.after_simulation_options_menu_message()

        captured = capsys.readouterr()
        assert "Please choose from the following options:" in captured.out, "Options menu after simulation should be displayed."
        assert "[1] Start over" in captured.out, "Option to start over should be displayed."
        assert "[2] Exit" in captured.out, "Option to exit should be displayed."

    def test_cli_goodbye_message(self, capsys):
        """Test the CLI goodbye message."""
        self.cli.goodbye()

        captured = capsys.readouterr()
        assert "Thank you for running the simulation. Goodbye!" in captured.out, "Goodbye message should be displayed."

class TestCLIGetFieldUserInput:
    """Test cases for the CLI get field input method."""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to run before each test."""
        self.cli = CLI()

    def test_cli_get_field_input(self, mocker):
        """Test the CLI field input handling."""
        user_input = "10 10"
        mocker.patch('builtins.input', return_value=user_input)

        height, width = self.cli.get_field_input()

        assert height == 10, "Height should be set to 10."
        assert width == 10, "Width should be set to 10."

    def test_cli_get_field_input_invalid(self, mocker):
        """Test the CLI field input handling with invalid input."""
        user_input = "10 -5"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid input. Please enter two positive integers separated by a space."):
            self.cli.get_field_input()

    def test_cli_get_field_input_non_integer(self, mocker):
        """Test the CLI field input handling with non-integer input."""
        user_input = "10 a"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid input. Please enter two positive integers separated by a space."):
            self.cli.get_field_input()

    def test_cli_get_field_input_invalid_format(self, mocker):
        """Test the CLI field input handling with invalid format."""
        user_input = "10, 10"
        mocker.patch('builtins.input', return_value=user_input)
    
        with pytest.raises(ValueError, match="Invalid input. Please enter two positive integers separated by a space."):
            self.cli.get_field_input()

    def test_cli_get_field_input_empty(self, mocker):
        """Test the CLI field input handling with empty input."""
        user_input = ""
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid input. Please enter two positive integers separated by a space."):
            self.cli.get_field_input()

class TestCLIGetOptionsMenuUserInput:
    """Test cases for the CLI get options menu input method."""
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to run before each test."""
        self.cli = CLI()

    def test_cli_get_options_menu_input(self, mocker):
        """Test the CLI menu options input handling."""
        user_input = "1"
        mocker.patch('builtins.input', return_value=user_input)

        option = self.cli.get_options_menu_input()

        assert option == "1", "Option should be set to 1."

    def test_cli_get_options_menu_input_invalid(self, mocker):
        """Test the CLI menu options input handling with invalid input."""
        user_input = "3"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid choice. Please enter 1 or 2."):
            self.cli.get_options_menu_input()
            
    def test_cli_get_options_menu_input_empty(self, mocker):
        """Test the CLI menu options input handling with empty input."""
        user_input = ""
        mocker.patch('builtins.input', return_value=user_input)
        with pytest.raises(ValueError, match="Invalid choice. Please enter 1 or 2."):
            self.cli.get_options_menu_input()
            
    def test_cli_get_options_menu_input_non_numeric(self, mocker):
        """Test the CLI menu options input handling with non-numeric input."""
        user_input = "abc"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid choice. Please enter 1 or 2."):
            self.cli.get_options_menu_input()

    def test_cli_get_options_menu_input_multiple_choices(self, mocker):
        """Test the CLI menu options input handling with multiple choices."""
        user_input = "1 2"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid choice. Please enter 1 or 2."):
            self.cli.get_options_menu_input()

    def test_cli_get_options_menu_input_special_characters(self, mocker):
        """Test the CLI menu options input handling with special characters."""
        user_input = "@"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid choice. Please enter 1 or 2."):
            self.cli.get_options_menu_input()
    
    def test_cli_get_options_menu_input_invalid_input(self, mocker):
        """Test the CLI menu options input handling with invalid input."""
        user_input = "1a"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid choice. Please enter 1 or 2."):
            self.cli.get_options_menu_input()

class TestClIGetCarNameUserInput:
    """Test cases for the CLI get car name input method."""
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to run before each test."""
        self.cli = CLI()
        
    def test_cli_get_car_name_input(self, mocker):
        """Test the CLI car name input handling."""
        user_input = "TestCar"
        mocker.patch('builtins.input', return_value=user_input)

        car_name = self.cli.get_car_name_input()

        assert car_name == "TestCar", "Car name should be set to 'TestCar'."

    def test_cli_get_car_name_input_whitespace(self, mocker):
        """Test the CLI car name input handling with whitespace."""
        user_input = "   TestCar   "
        mocker.patch('builtins.input', return_value=user_input)

        car_name = self.cli.get_car_name_input()

        assert car_name == "TestCar", "Car name should be stripped of whitespace."

    def test_cli_get_car_name_input_empty(self, mocker):
        """Test the CLI car name input handling with empty input."""
        user_input = ""
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Car name cannot be empty."):
            self.cli.get_car_name_input()
            

class TestCLIGetCarInitialPositionOrientationUserInput:
    """Test cases for the CLI get car initial position and orientation input method."""
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to run before each test."""
        self.cli = CLI()

    def test_cli_get_car_initial_position_orientation_input(self, mocker):
        """Test the CLI car initial position and orientation input handling."""
        user_input = "1 2 N"
        mocker.patch('builtins.input', return_value=user_input)

        position, orientation = self.cli.get_car_initial_position_and_orientation_input()

        assert position == (1, 2), "Position should be set to (1, 2)."
        assert orientation == 'N', "Orientation should be set to 'N'."

    def test_cli_get_car_initial_position_orientation_invalid(self, mocker):
        """Test the CLI car initial position and orientation input handling with invalid input."""
        user_input = "1 -2 N"
        mocker.patch('builtins.input', return_value=user_input)
        
        with pytest.raises(ValueError, match="Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W."):
            self.cli.get_car_initial_position_and_orientation_input()

    def test_cli_get_car_initial_position_orientation_non_integer(self, mocker):
        """Test the CLI car initial position and orientation input handling with non-integer input."""
        user_input = "1 a N"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W."):
            self.cli.get_car_initial_position_and_orientation_input()
    
    def test_cli_get_car_initial_position_orientation_invalid_direction(self, mocker):
        """Test the CLI car initial position and orientation input handling with invalid direction."""
        user_input = "1 2 X"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W."):
            self.cli.get_car_initial_position_and_orientation_input()
        
    def test_cli_get_car_initial_position_orientation_empty(self, mocker):
        """Test the CLI car initial position and orientation input handling with empty input."""
        user_input = ""
        mocker.patch('builtins.input', return_value=user_input)
        
        with pytest.raises(ValueError, match="Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W."):
            self.cli.get_car_initial_position_and_orientation_input()

    def test_cli_get_car_initial_position_orientation_multiple_values(self, mocker):
        """Test the CLI car initial position and orientation input handling with multiple values."""
        user_input = "1 2 N E"
        mocker.patch('builtins.input', return_value=user_input)
        
        with pytest.raises(ValueError, match="Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W."):
            self.cli.get_car_initial_position_and_orientation_input()
    
    def test_cli_get_car_initial_position_orientation_special_characters(self, mocker):
        """Test the CLI car initial position and orientation input handling with special characters."""
        user_input = "1 2 @"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W."):
            self.cli.get_car_initial_position_and_orientation_input()

    def test_cli_get_car_initial_position_orientation_invalid_input(self, mocker):
        """Test the CLI car initial position and orientation input handling with invalid input."""
        user_input = "1 2 N1"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W."):
            self.cli.get_car_initial_position_and_orientation_input()

class TestCLIGetCarInstructionsUserInput:
    """Test cases for the CLI get car instructions input method."""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method to run before each test."""
        self.cli = CLI()
        
    def test_cli_get_car_instructions_input(self, mocker):
        """Test the CLI car instructions input handling."""
        user_input = "FFRFFFFRRL"
        mocker.patch('builtins.input', return_value=user_input)

        instructions = self.cli.get_car_instructions_input()

        assert instructions == "FFRFFFFRRL", "Instructions should be set to 'FFRFFFFRRL'."

    def test_cli_get_car_instructions_input_invalid(self, mocker):
        """Test the CLI car instructions input handling with invalid input."""
        user_input = "FFRFFFFRRL123"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid command. Only 'L', 'R', and 'F' are allowed."):
            self.cli.get_car_instructions_input()
            
    def test_cli_get_car_instructions_input_special_characters(self, mocker):
        """Test the CLI car instructions input handling with special characters."""
        user_input = "FFR@FFFFRRL"
        mocker.patch('builtins.input', return_value=user_input)
        with pytest.raises(ValueError, match="Invalid command. Only 'L', 'R', and 'F' are allowed."):
            self.cli.get_car_instructions_input()
            
    def test_cli_get_car_instructions_input_whitespace(self, mocker):
        """Test the CLI car instructions input handling with whitespace."""
        user_input = " FFRFFFFRRL "
        mocker.patch('builtins.input', return_value=user_input)
        instructions = self.cli.get_car_instructions_input()
        
        assert instructions == "FFRFFFFRRL", "Instructions should be stripped of whitespace."

    def test_cli_get_car_instructions_input_mixed_case(self, mocker):
        """Test the CLI car instructions input handling with mixed case."""
        user_input = "FfRrL"
        mocker.patch('builtins.input', return_value=user_input)

        with pytest.raises(ValueError, match="Invalid command. Only 'L', 'R', and 'F' are allowed."):
            self.cli.get_car_instructions_input()

class TestCLIGetAfterSimulationOptionsMenuUserInput:
    """Test cases for the CLI get after simulation options menu input method."""