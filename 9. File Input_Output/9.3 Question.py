# Check if the file exists
import os

filename = "input.txt"

# Check if file exists and is accessible
if os.path.exists(filename) and os.access(filename, os.R_OK):
    # Open file for reading
    file = open(filename, "r")
    
    # Read and print each line
    for line in file:
        print(line.strip())  # strip() removes any trailing newline characters
    
    # Close the file
    file.close()
else:
    print(f"Error: File '{filename}' does not exist or is not accessible.")
