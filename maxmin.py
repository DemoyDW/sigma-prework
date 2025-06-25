import sys

numbers = sys.argv[1:]


low = int(numbers[0])
high = int(numbers[0])
for i in range(len(numbers)):
    if int(numbers[i]) < low:
        low = int(numbers[i])
    if int(numbers[i]) > high:
        high = int(numbers[i])

print([low, high])
