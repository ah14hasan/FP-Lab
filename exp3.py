# ==========================================
# Python Strings: Create, Concatenate,
# Print & Access Substrings
# ==========================================

# --- 1. CREATING STRINGS ---
str1 = 'Hello'                        # Single quotes
str2 = "World"                        # Double quotes
str3 = """Python is fun to learn."""  # Triple quotes (multi-line)
str4 = 'It\'s a great language'       # Escaped apostrophe
empty = ""                            # Empty string

print("--- Creating Strings ---")
print("str1:", str1)
print("str2:", str2)
print("str3:", str3)
print("str4:", str4)
print("Empty string:", empty)
print("Length of str1:", len(str1))

# --- 2. CONCATENATING STRINGS ---
print("\n--- String Concatenation ---")

# Method 1: Using + operator
result1 = str1 + " " + str2
print("Using + operator     :", result1)

# Method 2: Using * operator (repetition)
result2 = str1 * 3
print("Using * operator     :", result2)

# Method 3: Using join()
words = ["Python", "is", "awesome"]
result3 = " ".join(words)
print("Using join()         :", result3)

# Method 4: Using f-string (modern and recommended)
name = "Ali"
language = "Python"
result4 = f"My name is {name} and I love {language}!"
print("Using f-string       :", result4)

# Method 5: Using format()
result5 = "Hello, {}! Welcome to {}.".format(name, language)
print("Using format()       :", result5)

# --- 3. PRINTING STRINGS ---
print("\n--- Printing Strings ---")

# print with separator
print("Hello", "World", "Python", sep=" | ")

# print with custom end character
print("Line 1", end=" --> ")
print("Line 2")

# Escape characters
print("Tab:\tHello")
print("Newline:\nHello")
print("Backslash: \\")

# --- 4. STRING INDEXING ---
# Strings are zero-indexed
# Positive index: left to right → 0, 1, 2, ...
# Negative index: right to left → -1, -2, -3, ...
print("\n--- String Indexing ---")
s = "PYTHON"
print("String:", s)
print("Index chart: P=0, Y=1, T=2, H=3, O=4, N=5")
print("s[0]  =", s[0])    # First character
print("s[3]  =", s[3])    # 4th character
print("s[-1] =", s[-1])   # Last character
print("s[-3] =", s[-3])   # 3rd from the end

# --- 5. ACCESSING SUBSTRINGS (SLICING) ---
# Syntax: string[start : end : step]
# start → inclusive, end → exclusive
print("\n--- Substring Slicing ---")
text = "Hello, Python World!"
print("Original String:", text)
print("Length:", len(text))

print("\n# Basic Slicing")
print("text[0:5]    =", text[0:5])    # First 5 characters
print("text[7:13]   =", text[7:13])   # 'Python'
print("text[14:20]  =", text[14:20])  # 'World!'

print("\n# Slicing with omitted start/end")
print("text[:5]     =", text[:5])     # From start to index 5
print("text[7:]     =", text[7:])     # From index 7 to end
print("text[:]      =", text[:])      # Full copy of string

print("\n# Slicing with step")
print("text[::2]    =", text[::2])    # Every 2nd character
print("text[0:10:2] =", text[0:10:2])  # Every 2nd char from 0 to 10
print("text[::-1]   =", text[::-1])   # Reverse the string

print("\n# Negative index slicing")
print("text[-6:]    =", text[-6:])    # Last 6 characters
print("text[-6:-1]  =", text[-6:-1])  # 5 chars before the last

# --- 6. USEFUL STRING METHODS ---
print("\n--- Useful String Methods ---")
sample = "  hello, python world!  "
print("Original     :", sample)
print("upper()      :", sample.upper())
print("lower()      :", sample.lower())
print("strip()      :", sample.strip())         # Remove spaces
print("replace()    :", sample.replace("python", "amazing"))
print("find()       :", sample.find("python"))  # Returns index
print("count()      :", sample.count("l"))      # Count occurrences
print("split()      :", sample.strip().split(", "))
print("startswith() :", sample.strip().startswith("hello"))
print("endswith()   :", sample.strip().endswith("!"))
