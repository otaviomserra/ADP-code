import os

# Find the absolute path of the main script
this_script_path = os.path.abspath(__file__)

# Define the paths of the other Python scripts relative to the main script
main_script_path = os.path.join(os.path.dirname(this_script_path), "main.py")
script1_path = os.path.join(os.path.dirname(this_script_path), "datenverarbeitung/datenverarbeitung_main.py")
script2_path = os.path.join(os.path.dirname(this_script_path), "datenverarbeitung/extra_process_logs.py")

# Convert the paths to the correct format for your OS (e.g., Windows)
main_script_path = main_script_path.replace("/", "\\")
script1_path = script1_path.replace("/", "\\")
script2_path = script2_path.replace("/", "\\")

# Open the other Python scripts in separate Python shells
os.startfile(main_script_path)
os.startfile(script1_path)
os.startfile(script2_path)
