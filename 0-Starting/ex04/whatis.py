import sys

def whatis(object: any):
    try:
        try:
            assert len(sys.argv) == 2
            number = int(object)
            if number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")

        except ValueError:
            print("AssertionError: argument is not an integer")
            sys.exit()
    except AssertionError:
        print("AssertionError: more than one argument is provided")
        sys.exit()
if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit()
    else:
        whatis(sys.argv[1])