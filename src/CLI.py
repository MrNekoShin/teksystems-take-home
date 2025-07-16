
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
        print("List of cars in the simulation:")

        if self.simulation and self.simulation.cars:
            for car in self.simulation.cars.values():
                print(car)