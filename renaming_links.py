# Specify the input and output file paths
input_file_path = "chinese.txt"
output_file_path = "chinese-links.txt"

# Open the input file for reading and the output file for writing
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        line = line.strip()  # Remove leading and trailing whitespace
        line = line.replace(" ", "-")
        line = line.replace("/", "-")
        newline = line + ".mp4"
        output_file.write(newline + '\n')  # Write the modified line to the output file
        print(newline)  # Print the modified line if needed

