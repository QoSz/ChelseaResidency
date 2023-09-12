import os

# Get the current directory
current_directory = os.getcwd()

# List all files in the current directory
file_names = os.listdir(current_directory)

# Create a text file to store the file names
output_file = "file_names.txt"

# Open the file for writing
with open(output_file, "w") as file:
    # Write each file name to the file
    for file_name in file_names:
        file.write(file_name + "\n")

print(f"File names have been written to {output_file}")
