# Define a dictionary to store word counts
word_counts = {}

# Open the text file
with open('chinese.txt', 'r') as file:
    for line in file:
        words = line.split()  # Split the line into words
        for word in words:
            # Increment the word count in the dictionary
            word_counts[word] = word_counts.get(word, 0) + 1

# Iterate through the word counts and print the imposter words
for word, count in word_counts.items():
    if count > 1:
        print(f'Imposter word: "{word}" appears {count} times.')
   
# Replace 'your_file.txt' with the path to your text file.
