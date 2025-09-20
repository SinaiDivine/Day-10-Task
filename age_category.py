# age_category.py
# Day 10: Age category assignment

name = input("Enter your name: ").strip()
try:
    age = int(input("Enter your age: ").strip())
    if age < 0:
        raise ValueError("Negative age")
except Exception:
    print("Invalid age. Please enter a non-negative whole number (e.g. 21).")
    exit(1)

if age <= 12:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teen"
elif 20 <= age <= 59:
    category = "Adult"
else:
    category = "Senior"

print(" Age Category Summary ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Category: {category}")
