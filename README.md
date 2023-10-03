# **Quartus Pro - BSF Python Script**

## **Overview**

Eliminate the step of opening a random project in Intel Quartus Prime Standard to generate a measly bsf file for Intel Quartus Prime Pro. 

This python script automates the generation of Block Symbol Files (BSF) for Intel Quartus Prime Pro by utilizing quartus_map.exe from an Intel Quartus Standard that is able to generate the bsf. The script is written in Python and allows users to generate BSF files without manually opening the Intel Quartus Standard interface.

## **Configuration**
The script reads from a config.json file for necessary parameters. The structure of the config.json file is as follows:
The python script wont work until you change this file!

```
config.json
{
    "quartus_map_path": "C:\\intelFPGA\\18.1\\quartus\\bin64\\quartus_map.exe",
    "input_file_path": "C:\\test.v",
    "output_dir": "C:\\outputFilePath(not folder!)"
}
```
## **Parameters:**
1) quartus_map_path: Specifies the path to quartus_map.exe from Intel Quartus Standard. This executable is responsible for BSF file generation.
Typical location: C:/intelFPGA/<version>/quartus/bin/

2) input_file_path: Specifies the path to the source HDL file from which the BSF file will be generated.

3) output_dir: Specifies the directory where the generated BSF file will be saved. Note that this should be a directory path, not a file path.

## **Usage**
**You will need an Intel Quartus that is able to generate bsf files.**
You need to link this script with its quartus_map.exe command executable in the /bin/ folder of the quartus directory.

1) Update config.json:
- Set quartus_map.exe path to your specific Quartus Standard path.
- Set the input_file_path to the HDL file you wish to generate a BSF file from.
- Set the output_dir where you want the generated BSF file to be saved.
2) Run bsf_parser.py

   
## **Disclaimer**
This script does not perform any logical validation on the provided HDL files. It only produces the bsf file based on the module/component ports.

