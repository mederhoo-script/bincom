#!/usr/bin/python3
import random

# Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert binary to decimal
decimal_number = int(binary_number, 2)

print(f"Generated Binary Number: {binary_number}")
print(f"Equivalent Decimal Number: {decimal_number}")
