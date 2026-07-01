# ─────────────────────────────────────────────
#  Python List Operations – Demo Program
# ─────────────────────────────────────────────

# ── 1. Create a List ──────────────────────────
fruits = ["Apple", "Banana", "Mango"]
print("--- Created List ---")
print(fruits)

# ── 2. Append to a List ───────────────────────
print("\n--- Appending Elements ---")
fruits.append("Grapes")               # adds one item to the end
print(f"After append('Grapes')  : {fruits}")

fruits.insert(1, "Orange")            # inserts at a specific index
print(f"After insert(1,'Orange'): {fruits}")

fruits.extend(["Papaya", "Guava"])    # adds multiple items at once
print(f"After extend([...])     : {fruits}")

# ── 3. Remove from a List ─────────────────────
print("\n--- Removing Elements ---")
fruits.remove("Banana")               # removes by value (first match)
print(f"After remove('Banana')  : {fruits}")

popped = fruits.pop()                 # removes and returns last item
print(f"After pop()             : {fruits}  (removed: '{popped}')")

popped_idx = fruits.pop(1)            # removes and returns item at index
print(f"After pop(1)            : {fruits}  (removed: '{popped_idx}')")

del fruits[0]                         # deletes item at index
print(f"After del fruits[0]     : {fruits}")

# ── 4. Clear and Delete ───────────────────────
print("\n--- Clear & Delete ---")
backup = fruits.copy()
fruits.clear()                        # empties the list
print(f"After clear()   : {fruits}")

del fruits                            # deletes the list variable entirely
print("After del fruits: variable deleted")
print(f"Backup list     : {backup}")
