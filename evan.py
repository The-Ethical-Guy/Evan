import sys
import os
import subprocess
import readline
import shutil
import requests
from zipfile import ZipFile
from io import BytesIO
import tempfile


usage_msg = f"""Usage: evan -api <chatgpt-api-key>
please try 'evan -h' to see the options"""
help_msg = f"""Usage: evan -api <chatgpt-api-key>
Options:
    evan -update | to update the tool
    evan -h | to get the tool guide"""




def update_evan():
    evan_path = "../Evan"

    # Remove the existing Evan directory
    if os.path.exists(evan_path):
        shutil.rmtree(evan_path)

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_path:
        # Download the Evan repository zip from GitHub
        github_url = "https://github.com/The-Ethical-Guy/Evan/archive/main.zip"
        response = requests.get(github_url)

        if response.status_code == 200:
            # Extract the contents of the "Evan-main" folder from the zip file
            with ZipFile(BytesIO(response.content), 'r') as zip_file:
                zip_file.extractall(temp_path)

            # Move the contents of "Evan-main" to the target directory
            source_folder = os.path.join(temp_path, "Evan-main")
            shutil.move(source_folder, evan_path)

            print("Evan updated successfully!")
        else:
            print(f"Failed to download Evan from GitHub. Status code: {response.status_code}")


def handle_args(user_arg):
    if len(user_arg) < 2 or len(user_arg) > 4:
        print(usage_msg)
        sys.exit(1)

    if user_arg[1] == '-h':
        print(help_msg)
        sys.exit(1)
    
    elif user_arg[1] == '-update':
        update_evan()
        sys.exit(1)
    
    elif user_arg[1] == '-api':
        try:
            api_key = user_arg[2]
            subprocess.run(["python3", "main.py", api_key])
        except KeyboardInterrupt:
            pass

        except Exception:
            print("There is an error, please try to enter a valid input or update the tool")



handle_args(sys.argv)
