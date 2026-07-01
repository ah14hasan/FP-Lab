# Create a tuple
colors = ("red", "green", "blue")
print(f"Original tuple: {colors}")

# Access elements
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")

# Slicing a tuple
print(f"First two colors: {colors[:2]}")

# Loop through a tuple
print("Looping through tuple:")
for color in colors:
    print(color)

# Count and index
numbers = (1, 2, 3, 2, 4, 2)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of first 3: {numbers.index(3)}")

# Tuples are immutable - this would raise an error if uncommented
# colors[0] = "yellow"

# Tuple unpacking
a, b, c = colors
print(f"Unpacked: a={a}, b={b}, c={c}")
