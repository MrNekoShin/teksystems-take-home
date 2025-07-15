import pytest
from src.CLI import CLI

def test_cli_initialization():
    """Test the CLI initialization."""
    cli = CLI()
    assert cli is not None, "CLI should be initialized successfully."
