# ==========================================
# Python Arithmetic Operations Demo
# ==========================================

a = 17
b = 5

print("Values: a =", a, ", b =", b)
print("=" * 35)

# --- 1. ADDITION (+) ---
result = a + b
print("Addition        (a + b)  =", result)

# --- 2. SUBTRACTION (-) ---
result = a - b
print("Subtraction     (a - b)  =", result)

# --- 3. MULTIPLICATION (*) ---
result = a * b
print("Multiplication  (a * b)  =", result)

# --- 4. DIVISION (/) ---
# Always returns a float, even if result is a whole number
result = a / b
print("Division        (a / b)  =", result)

# --- 5. FLOOR DIVISION (//) ---
# Divides and returns the largest integer ≤ result (drops decimal)
result = a // b
print("Floor Division  (a // b) =", result)

# --- 6. MODULUS (%) ---
# Returns the remainder after division
result = a % b
print("Modulus         (a % b)  =", result)

# --- 7. EXPONENTIATION (**) ---
# Raises left number to the power of the right
result = a ** b
print("Exponentiation  (a ** b) =", result)

# ==========================================
# OPERATOR PRECEDENCE (BODMAS/PEMDAS)
# ==========================================
print("\n--- Operator Precedence ---")
expr1 = 10 + 3 * 2         # Multiplication first, then addition
expr2 = (10 + 3) * 2       # Brackets evaluated first
print("10 + 3 * 2       =", expr1)   # 16
print("(10 + 3) * 2     =", expr2)   # 26

# ==========================================
# ARITHMETIC WITH FLOATS
# ==========================================
print("\n--- Arithmetic with Floats ---")
x = 9.5
y = 2.0
print("Addition:       ", x + y)
print("Subtraction:    ", x - y)
print("Multiplication: ", x * y)
print("Division:       ", x / y)
print("Floor Division: ", x // y)
print("Modulus:        ", x % y)
print("Exponentiation: ", x ** y)

# ==========================================
# AUGMENTED ASSIGNMENT OPERATORS
# ==========================================
# Shorthand for performing operation and re-assigning to same variable
print("\n--- Augmented Assignment Operators ---")
n = 20
print("Initial value of n:", n)

n += 5   # same as n = n + 5
print("After n += 5  →", n)

n -= 3   # same as n = n - 3
print("After n -= 3  →", n)

n *= 2   # same as n = n * 2
print("After n *= 2  →", n)

n /= 4   # same as n = n / 4
print("After n /= 4  →", n)

n //= 3  # same as n = n // 3
print("After n //= 3 →", n)

n %= 4   # same as n = n % 4
print("After n %= 4  →", n)

n **= 3  # same as n = n ** 3
print("After n **= 3 →", n)

# ==========================================
# REAL-WORLD EXAMPLE: Simple Bill Calculator
# ==========================================
print("\n--- Bill Calculator ---")
price_per_item = 49.99
quantity = 3
discount = 10        # 10% discount
tax_rate = 0.18      # 18% GST

subtotal = price_per_item * quantity
discount_amount = subtotal * (discount / 100)
after_discount = subtotal - discount_amount
tax_amount = after_discount * tax_rate
total = after_discount + tax_amount

print(f"Price per item : ₹{price_per_item}")
print(f"Quantity       : {quantity}")
print(f"Subtotal       : ₹{subtotal:.2f}")
print(f"Discount (10%) : ₹{discount_amount:.2f}")
print(f"After Discount : ₹{after_discount:.2f}")
print(f"GST (18%)      : ₹{tax_amount:.2f}")
print(f"Total Payable  : ₹{total:.2f}")
