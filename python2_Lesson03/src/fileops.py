"""Reads a list from a file and writes a list to a file."""

def write_list(fn, list):
    """Writes a list to a named file. Each list item will be on 
    a separate line. Overwrites the file if it already exists.
    """
    f = open(fn, "w")
    for item in list:
        f.write("%s\n" % item)
    f.close()

                
def read_list(fn):
    """Reads a list from a file without using readline. 
    Uses standard line endings ("\n") to delimit list items.
    """
    f = open(fn, "r")
    s = f.read()
    # If the last character in the file is a newline, delete it
    if s[-1] == "\n":
        s = s[:-1]

    l = s.split("\n")
    return l

