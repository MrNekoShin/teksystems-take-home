"""
Auto Driving Car Simulation CLI Interface
"""

from src.CLI import CLI

def main():
    """Main function to run the CLI."""
    cli = CLI()
    cli.main_loop()

if __name__ == "__main__":
    main()