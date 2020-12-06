"""Demonstrating the continue statement"""

while True:
    s = input("Enter a line: ")
    if not s:
        break
    if s.startswith('#'):
        continue
    print("Length", len(s))