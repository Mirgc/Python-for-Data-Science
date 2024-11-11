import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

def main():
    """
    A program that takes a string as an argument and encodes it into Morse Code.
    """
    try:
        assert len(sys.argv) == 2
        input_string = sys.argv[1]
        
        for char in input_string:
            if char.upper() not in NESTED_MORSE:
                print("AssertionError: the arguments are bad")
                exit(0)
        
        for char in input_string:
            print(NESTED_MORSE[char.upper()], end=" ")

    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit()

if __name__ == "__main__":
    main()