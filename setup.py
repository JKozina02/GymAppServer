import os
import subprocess
import sys

VENV_DIR = '.venv'

#create venv if its not there
def create_venv():
    if not os.path.exists(VENV_DIR):
        print("Creating virtual envirement...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print("Virtual envirement created.")

#install required packages
def install_requirements():
    pip_exec = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "pip")
    print("Installing dependencies")
    subprocess.check_call([pip_exec, "install", "-r", "requirements.txt"])
    print("Installed")

if __name__ == "__main__":
    create_venv()
    install_requirements()
    print("Ready!!! Activate venv with:")
    print(f"Windows:   {VENV_DIR}\\Scripts\\activate")
    print(f"Mac/Linux: source {VENV_DIR}/bin/activate")