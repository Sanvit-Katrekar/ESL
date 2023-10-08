'''
Tests for maximum length value for each attribute.
'''

with open('data/en-data.txt') as f:
    words = f.read().splitlines()

stat_data = ['word', 'link']

for i, data in enumerate(stat_data):
    print('-'*10)
    max_val = max((word.split(':', 1)[i].strip() for word in words), key=len)
    print(f'Max {data}:', max_val)
    print(f'Max {data} length:', len(max_val))
print('Total no. of records:', len(words))