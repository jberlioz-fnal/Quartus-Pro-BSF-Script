import subprocess
import os
from .config import read_config

#hdl to bsf
def run_hdl():
    # Read the configuration
    config = read_config()

    # Extract variables from the config
    quartus_map_path = config['quartus_map_path']
    input_file_path = config['input_file_path']
    output_dir = config['output_dir']

    # Change to the output directory
    os.chdir(output_dir)

    compile_hdl(quartus_map_path,input_file_path)
    generate_symbol(quartus_map_path,input_file_path)

#bdf to bsf
def run_bdf():
    # Read the configuration
    config = read_config()

    # Extract variables from the config
    quartus_map_path = config['quartus_map_path']
    input_file_path = config['input_file_path']
    output_dir = config['output_dir']

    # Change to the output directory
    os.chdir(output_dir)

    bdf2verilog(quartus_map_path, input_file_path)
    input_file_verilog = os.path.splitext(input_file_path)[0] + ".v"
    print(input_file_verilog)
    compile_hdl(quartus_map_path, input_file_verilog)
    generate_symbol(quartus_map_path, input_file_verilog)

def compile_hdl(quartus_map_path, input_file_path):
    command = [
        quartus_map_path,
        "test_vlog",
        "--analyze_file={}".format(input_file_path)
    ]
    subprocess.run(command)

def generate_symbol(quartus_map_path, input_file_path):
    command = [
        quartus_map_path,
        "--generate_symbol={}".format(input_file_path)
    ]
    subprocess.run(command)

def bdf2verilog(quartus_map_path, input_file_path):
    command = [
        quartus_map_path,
        "--convert_bdf_to_verilog={}".format(input_file_path)
    ]
    subprocess.run(command)
