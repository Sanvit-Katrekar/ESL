# Define a dictionary to store word counts
word_counts = {}

# Lists to store unique and duplicate lines
unique_lines = []
duplicate_lines = []

# Open the input text file and create an output text file for unique lines
with open('english-links.txt', 'r') as input_file, open('unique-english-links.txt', 'w') as output_file:
    for line in input_file:
        # Remove leading and trailing whitespace 
        cleaned_line = line.strip()

        if cleaned_line in word_counts:
            word_counts[cleaned_line] += 1
            duplicate_lines.append(cleaned_line)  # Add to duplicate lines list
        else:
            word_counts[cleaned_line] = 1
            unique_lines.append(line)  # Add to unique lines list
            output_file.write(line)  # Write the unique line to the output file

# Print duplicate lines
for line in duplicate_lines:
    print(f'Duplicate line: "{line}"')

# Replace 'english-links.txt' with the path to your input text file and 'unique-english-links.txt' with the path to your output file.
