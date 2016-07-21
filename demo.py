import sys

# Read list of numbers
numbers = [int(line) for line in open(sys.argv[1])]
N = len(numbers)

# Print two lists of numbers, labeled 'A' and 'B'
print 'A', ' '.join(map(str, numbers[:N/2]))
print 'B', ' '.join(map(str, numbers[N/2:]))
