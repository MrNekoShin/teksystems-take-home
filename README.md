# Auto Driving Car Simulation

> A command-line simulation program for autonomous driving cars with collision detection and step-by-step execution.

## Features

- **Interactive CLI interface** - User-friendly command-line experience
- **Field creation** - Custom dimensions for simulation environment  
- **Multiple car management** - Handle multiple vehicles simultaneously
- **Command-based movement** - Forward, Left, Right navigation
- **Collision detection** - Real-time collision tracking with step details
- **Input validation** - Robust error handling and retry logic
- **Graceful error handling** - Comprehensive error management

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Teksystems-X-GIC
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Simulation

```bash
python main.py
```

### Basic Commands

1. **Field Setup** - Enter field dimensions (e.g., `10 10`)
2. **Add Cars** - Provide name, position, and commands
3. **Run Simulation** - Execute all car movements step-by-step

### Car Commands

| Command | Action |
|---------|--------|
| `F` | Move forward one step |
| `L` | Turn left 90 degrees |
| `R` | Turn right 90 degrees |

### Example Session

```
Welcome to Auto Driving Car Simulation!

Please enter the width and height of the simulation field in x y format:
> 10 10
You have created a field of 10 x 10.

Please choose from the following options:
[1] Add a car to field
[2] Run simulation
> 1

Please enter the name of the car:
> CarA

Please enter initial position of car CarA in x y Direction format:
> 1 2 N

Please enter the commands for car CarA:
> FFRFFFFRRL

Your current list of cars are:
- CarA, (1,2) N, FFRFFFFRRL

Please choose from the following options:
[1] Add a car to field
[2] Run simulation
> 2

After simulation, the result is:
- CarA, (5,4) S

Please choose from the following options:
[1] Start over
[2] Exit
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_cli.py

# Run with verbose output
pytest -v
```

### Project Structure

```
├── src/
│   ├── __init__.py
│   ├── car.py           # Car class and logic
│   ├── field.py         # Field class and boundaries
│   ├── simulation.py    # Simulation engine
│   └── CLI.py          # Command-line interface
├── tests/
│   ├── test_car.py     # Car tests
│   ├── test_field.py   # Field tests
│   ├── test_simulation.py # Simulation tests
│   └── test_CLI.py     # CLI tests
├── main.py             # Application entry point
├── requirements.txt    # Dependencies
└── README.md          # This file
```

### Dependencies

```
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0
```
