# Bitwise Operators
# Bitwise operators are used to compare binary numbers.
# The bitwise operators are:
# & (AND)
# | (OR)
# ^ (XOR)
# ~ (NOT)
# >> (Right Shift)
# << (Left Shift)

a = 5  # 0101 in binary
b = 3  # 0011 in binary

# & (AND)
print(a & b)  # 1 (0001 in binary)
# | (OR)
print(a | b)  # 7 (0111 in binary)
# ^ (XOR)
print(a ^ b)  # 6 (0110 in binary)
# ~ (NOT)
print(~a)  # -6 (in binary, it's the complement of 5)
print(~b)  # -4 (in binary, it's the complement of 3)
# >> (Right Shift)
print(a >> 1)  # 2 (0010 in binary)
# << (Left Shift)
print(a << 1)  # 10 (1010 in binary)
