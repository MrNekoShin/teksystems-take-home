import pytest
from src.CLI import CLI

class TestCLI:
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
