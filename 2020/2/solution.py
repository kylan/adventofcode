import re

def get_input():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]
        return content

## Part 1

count = 0

entries = get_input()
for entry in entries:
    m = re.search('(\d+)-(\d+) (\w+): (\w+)', entry)

    mini = int(m.group(1))
    maxi = int(m.group(2))
    char = m.group(3)
    pasw = m.group(4)
    
    num_char = len(re.findall(char, pasw))
   
    if num_char >= mini and num_char <= maxi:
        count += 1

assert(count == 600)
print(count)

## Part 2

count = 0

entries = get_input()
for entry in entries:
    m = re.search('(\d+)-(\d+) (\w+): (\w+)', entry)
    i1 = int(m.group(1)) - 1
    i2 = int(m.group(2)) - 1
    char = m.group(3)
    pasw = m.group(4)

    first = pasw[i1] == char
    second = pasw[i2] == char

    if first != second:
        count += 1

assert(count == 245)
print(count)
