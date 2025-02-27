import os
import subprocess
import sys

def run_command(command, description=None):
    """ Runs a system command and handles errors. """
    if description:
        print(f"\n{description}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        sys.exit(1)

def check_python_version():
    """ Ensures Python 3.10+ is installed. """
    print("Checking Python version...")
    if sys.version_info.major == 3 and sys.version_info.minor >= 10:
        print("✔ Python version is OK.")
    else:
        print("✖ Python 3.10+ is required. Install it from https://www.python.org/downloads/")
        sys.exit(1)

def setup_virtual_env():
    """ Sets up a Python virtual environment. """
    if not os.path.exists("venv"):
        run_command("python3 -m venv venv", "Creating virtual environment...")
    print("✔ Virtual environment created.")
    print("Activate it using: source venv/bin/activate")

def install_requirements():
    """ Installs required Python packages. """
    run_command("pip install -r requirements.txt", "Installing dependencies from requirements.txt...")

def configure_bot():
    """ Guides the user to configure the bot. """
    print("\n✔ Configuration files are in the `config` directory.")
    print("Edit the following files before running the bot:")
    print(" - `config/personals.py` -> Personal details")
    print(" - `config/questions.py` -> Answer automation")
    print(" - `config/search.py` -> Job search preferences")
    print(" - `config/secrets.py` -> LinkedIn credentials")

def run_bot():
    """ Runs the LinkedIn Auto Applier Bot. """
    run_command("python3 runAiBot.py", "Starting job application bot...")

if __name__ == "__main__":
    check_python_version()
    setup_virtual_env()
    install_requirements()
    configure_bot()
    run_bot()
