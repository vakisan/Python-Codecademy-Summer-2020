single_digits = range(10)
squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit**2)
print(squares)

cubes = [cube**3 for cube in single_digits]

print(cubes)
