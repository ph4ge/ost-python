"""Detect any mention of several languages in the user's input."""

uin = input("Please enter a sentence: ")
if "python" in uin.lower():
    print("You mentioned Python")
elif "perl" in uin.lower():
    print("Aha, a Perl user!")
elif "ruby" in uin.lower():
    print("So you use ruby")
else:
    print("Didn't see any languages there")