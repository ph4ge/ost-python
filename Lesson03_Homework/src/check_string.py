#
#check_string.py
#
g = 1
while g:
    input_string = input("Please enter an upper-case string ending with a period: ")
    if input_string.isupper():
        if input_string.endswith('.'):
            print("Input meets both requirements.")
            g=0
        else:
            print("Input does not end with a period.")
    else:
        print("Input is not all upper case.")