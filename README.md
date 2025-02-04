# geekfest2025

GitHub repo for Geekfest demo - we want you to contribute!

## Word Guessing Game

This project is a simple word guessing game implemented in Python. The game selects a random word from a list and the player has to guess the letters in the word within a limited number of attempts.

### Features

- Random word selection from a JSON file
- ASCII art welcome message using `pyfiglet`
- Colored text output using `colorama`
- Tracks guessed letters and remaining attempts

### Requirements

- Python 3.x
- `colorama` library
- `pyfiglet` library

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/geekfest2025.git
   cd geekfest2025
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. Ensure you have a `words.json` file in the same directory as `main.py`. The JSON file should have the following structure:
   ```json
   {
       "words": [
           "python", "opensource", "contribution", "development", "programming",
           "repository", "commitment", "branching", "merging", "debugging",
           "testing", "deployment", "feature", "release", "version",
           "forking", "cloning", "push", "continuous", "integration",
           "automation", "scalability", "performance", "geekfest"
       ]
   }
   ```

2. Run the game:
   ```sh
   python main.py
   ```

3. Follow the on-screen instructions to guess the letters in the word.

## Contributing

We welcome contributions from everyone. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.
