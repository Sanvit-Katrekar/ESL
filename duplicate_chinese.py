# Read the contents of the English file into a set
with open('english.txt', 'r') as english_file:
    english_lines = set(english_file.read().splitlines())

# Read the contents of the Chinese file into a list
with open('chinese.txt', 'r') as chinese_file:
    chinese_lines = chinese_file.read().splitlines()

# Create a list for the unique Chinese lines
unique_chinese_lines = []

# Iterate through the Chinese lines and keep only the unique ones
for line in chinese_lines:
    if line not in english_lines:
        unique_chinese_lines.append(line)

# Write the unique Chinese lines back to a new file
with open('chinese_unique.txt', 'w') as output_file:
    output_file.write('\n'.join(unique_chinese_lines))

# The unique Chinese lines are now saved in 'chinese_unique.txt'
