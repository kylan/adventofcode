def get_input():
    with open('input.txt', 'r') as f:
        content = [int(line.strip()) for line in f]
        return content

def find_pair(numbers, target):
    while numbers:
        b = numbers.pop()
        for c in numbers:
            if b + c == target:
                return(b * c)

def find_triplet(numbers):
    while numbers:
        a = numbers.pop()
        pair = find_pair(numbers.copy(), 2020 - a)
        if pair is not None:
            return a * pair

## Part 1
answer = find_pair(get_input(), 2020)
assert(answer == 1007104)
print(answer)
## Part 2
answer = find_triplet(get_input())
assert(answer == 18847752)
print(answer)
