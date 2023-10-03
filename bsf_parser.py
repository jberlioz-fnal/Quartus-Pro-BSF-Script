import subprocess
import os
import json

# Read the configuration file
with open('config.json', 'r') as f:
    config = json.load(f)

# Extract variables from the config
quartus_map_path = config['quartus_map_path']
input_file_path = config['input_file_path']
output_dir = config['output_dir']

# Change to the output directory
os.chdir(output_dir)

# Construct the command
command = [
    quartus_map_path,
    "--generate_symbol={}".format(input_file_path)
]

# Run the command
subprocess.run(command)
