import sys
from ft_filter import ft_filter

def count(string: str, integer: int):
    if len(string) > integer:
        return True
    else:
        return False

def main():
    """
    A program that accepts two arguments: a string(S), and an integer(N). The
    program should output a list of words from S that have a length greater than N.
    """
    try:
        assert len(sys.argv) == 3
        input_string = sys.argv[1]
        try:
            input_integer = int(sys.argv[2])
        except ValueError:
            print("AssertionError: the arguments are bad")
            sys.exit()
        
        words = input_string.split()
        filtered_words = ft_filter(lambda word: count(word, input_integer), words)
        
        print(list(filtered_words))

    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit()

if __name__ == "__main__":
    main()