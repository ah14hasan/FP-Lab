# ─────────────────────────────────────────────
#  Python Dictionaries – Demonstration Program
# ─────────────────────────────────────────────

# ── 1. Creating a dictionary ──────────────────
student = {
    "name": "Ali",
    "age": 24,
    "branch": "CSE",
    "cgpa": 8.7
}
print("=== Student Record ===")
print(student)

# ── 2. Accessing values ───────────────────────
print("\n=== Accessing Values ===")
print("Name :", student["name"])
print("CGPA :", student.get("cgpa"))          # .get() avoids KeyError
print("City :", student.get("city", "N/A"))   # default if key missing

# ── 3. Adding & updating entries ──────────────
print("\n=== Adding & Updating ===")
student["city"] = "Hyderabad"                 # add new key
student["cgpa"] = 9.0                         # update existing key
print(student)

# ── 4. Removing entries ───────────────────────
print("\n=== Removing Entries ===")
removed = student.pop("age")                  # removes & returns value
print(f"Removed 'age': {removed}")
print(student)

# ── 5. Iterating ─────────────────────────────
print("\n=== Iterating ===")
print("Keys   :", list(student.keys()))
print("Values :", list(student.values()))
print("Items  :")
for key, value in student.items():
    print(f"  {key:10} → {value}")

# ── 6. Dictionary comprehension ───────────────
print("\n=== Dictionary Comprehension ===")
squares = {n: n**2 for n in range(1, 6)}
print("Squares:", squares)

# ── 7. Nested dictionary ──────────────────────
print("\n=== Nested Dictionary ===")
university = {
    "JNTUH": {
        "location": "Hyderabad",
        "college": "UCEST",
        "department": "CSE"
    }
}
print("College :", university["JNTUH"]["college"])
print("Dept    :", university["JNTUH"]["department"])

# ── 8. Merging two dictionaries (Python 3.9+) ─
print("\n=== Merging Dictionaries ===")
extra = {"semester": 2, "project": "Lip Vision"}
merged = student | extra                      # merge operator
print(merged)

# ── 9. Membership test ────────────────────────
print("\n=== Membership Test ===")
print("'name' in student   :", "name" in student)
print("'rollno' in student :", "rollno" in student)

# ── 10. Common utility methods ────────────────
print("\n=== Utility Methods ===")
copy = student.copy()                         # shallow copy
print("Copy equal to original?", copy == student)
copy.clear()
print("After clear(), copy:", copy)
print("Original untouched  :", student)
