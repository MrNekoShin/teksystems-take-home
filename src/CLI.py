import re

from src.car import Car
from src.simulation import Simulation

class CLI:
    def __init__(self):
        """Initialize the CLI."""
        self.simulation = None  # This will hold the simulation instance once created

    def welcome(self):
        """Display the welcome message."""
        print("Welcome to Auto Driving Car Simulation!\n")

    def create_field_message(self):
        """Prompt user to create a field."""
        print("Please enter the width and height of the simulation field in x y format:")

    def field_created_message(self, width, height):
        """Display confirmation of field creation."""
        print(f"You have created a field of {width} x {height}.")

    def options_menu_message(self):
        """Display the options menu."""
        print("Please choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")

    def add_car_name_message(self):
        """Prompt user to enter car name."""
        print("Please enter the name of the car:")

    def add_car_initial_position_and_orientation_message(self, car_name):
        """Prompt user to enter car position."""
        print(f"Please enter initial position of car {car_name} in x y Direction format:")

    def add_car_instructions_message(self, car_name):
        """Prompt user to enter car instructions."""
        print(f"Please enter the commands for car {car_name}:")

    def list_cars_message(self):
        """Display the list of cars in the simulation."""
        print("Your current list of cars are:")

        if self.simulation and self.simulation.cars:
            for car in self.simulation.cars.values():
                print(car)

    def simulation_results_message(self):
        """Display the results of the simulation."""
        print("After simulation, the result is:")

        if self.simulation and self.simulation.cars:
            for car in self.simulation.cars.values():
                print(car)

    def after_simulation_options_menu_message(self):
        """Display options after simulation."""
        print("Please choose from the following options:")
        print("[1] Start over")
        print("[2] Exit")

    def goodbye(self):
        """Display goodbye message."""
        print("Thank you for running the simulation. Goodbye!")

    ### Getting user input###

    def get_field_input(self):
        """Get the field size from user input."""

        field_size = input()

        pattern = r'^\d+\s+\d+$'
        if not re.match(pattern, field_size):
            raise ValueError("Invalid input. Please enter two positive integers separated by a space.")

        try:
            width, height = map(int, field_size.split())
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive integers.")
            return width, height
        except ValueError as e:
            raise ValueError(e)
    
    def get_options_menu_input(self):
        """Get the user's choice from the options menu."""
        choice = input()

        if choice not in ['1', '2']:
            raise ValueError("Invalid choice. Please enter 1 or 2.")
        
        return choice
    
    def get_car_name_input(self):
        """Get the car name from user input."""
        car_name = input().strip()
        
        if not car_name:
            raise ValueError("Car name cannot be empty.")
        
        return car_name
    
    def get_car_initial_position_and_orientation_input(self):
        """Get the car's initial position and orientation."""
        position = input().strip()

        pattern = r'^\d+\s+\d+\s+[NESW]$'
        if not re.match(pattern, position):
            raise ValueError("Invalid input. Please enter in x y Direction format where Direction is one of N, E, S, W.")

        try:
            x, y, direction = position.split()
            x, y = int(x), int(y)
            
            return (x, y), direction
        except ValueError as e:
            raise ValueError(e)
        
    def get_car_instructions_input(self):
        """Get the car's instructions."""
        instructions = input().strip()
        
        # Validate that instructions only contain valid characters (e.g., L, R, F)
        if not all(char in 'LRF' for char in instructions):
            raise ValueError("Invalid command. Only 'L', 'R', and 'F' are allowed.")
        
        return instructions
    
    def get_after_simulation_options_menu_input(self):
        """Get the user's choice after simulation."""
        choice = input()

        if choice not in ['1', '2']:
            raise ValueError("Invalid choice. Please enter 1 or 2.")
        
        return choice
    
    ### Flow control methods ###

    def add_car_loop(self):
        """Loop to add cars to the simulation."""
        while True:
            self.options_menu_message()
            choice = self.get_options_menu_input()

            if choice == '1':
                self.add_car()
            elif choice == '2':
                break

    def add_car(self):
        """Add a car to the simulation."""
        self.add_car_name_message()
        car_name = self.get_car_name_input()

        self.add_car_initial_position_and_orientation_message(car_name)
        position, orientation = self.get_car_initial_position_and_orientation_input()

        self.add_car_instructions_message(car_name)
        instructions = self.get_car_instructions_input()
        
        # Create and add the car to the simulation
        car = Car(name=car_name, position=position, orientation=orientation, instructions=instructions)
        self.simulation.add_car(car)
            
    def main_loop(self):
        """Main loop to run the CLI."""
        self.welcome()
        
        while True:
            self.create_field_message()
            width, height = self.get_field_input()
            self.simulation = Simulation(field_size=(width, height))
            self.field_created_message(width, height)
            self.add_car_loop()
            
            self.list_cars_message()
            self.simulation.run_simulation()
            self.simulation_results_message()

            self.after_simulation_options_menu_message()
            choice = self.get_after_simulation_options_menu_input()

            if choice == '2':
                break
        
        self.goodbye()