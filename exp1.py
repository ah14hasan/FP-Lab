# Experiment 1 - Python Number Data Types

# --- 1. INTEGER (int) ---
# Whole numbers, positive or negative, with no decimal point
a = 100
b = -25
big_num = 99999999999999999999  # Python int has no size limit!

print("--- INTEGER ---")
print("Value:", a)
print("Type:", type(a))
print("Negative int:", b)
print("Very large int:", big_num)

# Different int formats
binary = 0b1010       # Binary (base 2)
octal = 0o17          # Octal (base 8)
hexadecimal = 0xFF    # Hexadecimal (base 16)

print("\nBinary 0b1010 =", binary)
print("Octal 0o17 =", octal)
print("Hexadecimal 0xFF =", hexadecimal)

# --- 2. FLOAT (float) ---
# Numbers with a decimal point or in scientific notation
x = 3.14
y = -0.001
sci = 1.5e3  # Scientific notation: 1.5 × 10³ = 1500.0

print("\n--- FLOAT ---")
print("Value:", x)
print("Type:", type(x))
print("Negative float:", y)
print("Scientific notation (1.5e3):", sci)

# Note: Division always returns a float in Python 3
print("10 / 2 =", 10 / 2, "→ type:", type(10 / 2))

# --- 3. COMPLEX (complex) ---
# Numbers with a real and an imaginary part (written as a + bj)
c1 = 3 + 5j
c2 = 2 - 4j

print("\n--- COMPLEX ---")
print("Value:", c1)
print("Type:", type(c1))
print("Real part:", c1.real)
print("Imaginary part:", c1.imag)
print("Addition of two complex numbers:", c1 + c2)

# --- 4. TYPE CONVERSION ---
print("\n--- TYPE CONVERSION ---")
print("int → float:", float(a))        # 100  → 100.0
print("float → int:", int(x))          # 3.14 → 3 (truncates, doesn't round)
print("int → complex:", complex(a))    # 100  → (100+0j)

# --- 5. ARITHMETIC OPERATIONS ---
print("\n--- ARITHMETIC ---")
print("Addition:      ", 10 + 3)
print("Subtraction:   ", 10 - 3)
print("Multiplication:", 10 * 3)
print("Division:      ", 10 / 3)   # Always float
print("Floor Division:", 10 // 3)  # Drops decimal
print("Modulus:       ", 10 % 3)   # Remainder
print("Exponentiation:", 2 ** 8)   # 2 to the power 8

