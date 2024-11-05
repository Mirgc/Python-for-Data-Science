import sys

def main():
    """Take a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters, digits and spaces.

    Parameters:
    ----------
    string: str
        A string to be analyzed.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
        exit(0)
    elif len(sys.argv) < 2:
        print("What is the text to count?")
        message = sys.stdin.readline()
    else:
        message = sys.argv[1]

    if message:
        string = message
        upper_case = 0
        lower_case = 0
        punctuation = 0
        digits = 0
        spaces = 0

        for char in string:
            if char.isupper():
                upper_case += 1
            elif char.islower():
                lower_case += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            else:   
                punctuation += 1

        print(f"The text contains {len(string)} characters:")
        print(f"{upper_case} upper letters")
        print(f"{lower_case} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    return None

if __name__ == "__main__":
    ## How use __doc__ and help
    #print("Using __doc__:")
    #print(main.__doc__)
    #print("Using help:")
    #help(main)
    main()