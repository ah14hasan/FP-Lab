# ─────────────────────────────────────────────
#  Recursive Function – n'th Item in a List
# ─────────────────────────────────────────────

def nth_item(lst, n):
    if n == 0:
        return lst[0]
    return nth_item(lst[1:], n - 1)

# ── Demo ──────────────────────────────────────
numbers = [10, 20, 30, 40, 50]
n = int(input("Enter index (0-based): "))

print(f"List      : {numbers}")
print(f"Item at {n} : {nth_item(numbers, n)}")
