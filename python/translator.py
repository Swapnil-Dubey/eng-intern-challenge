import sys

braille_dict = {
    # Letters A-Z
    "A": "0.....",  # A
    "B": "0.0...",  # B
    "C": "00....",  # C
    "D": "00.0..",  # D
    "E": "0..0..",  # E
    "F": "000...",  # F
    "G": "0000..",  # G
    "H": "0.00..",  # H
    "I": ".00...",  # I
    "J": ".000..",  # J
    "K": "0...0.",  # K
    "L": "0.0.0.",  # L
    "M": "00..0.",  # M
    "N": "00.00.",  # N
    "O": "0..00.",  # O
    "P": "000.0.",  # P
    "Q": "00000.",  # Q
    "R": "0.000.",  # R
    "S": ".00.0.",  # S
    "T": ".0000.",  # T
    "U": "0...00",  # U
    "V": "0.0.00",  # V
    "W": ".0...0",  # W
    "X": "00..00",  # X
    "Y": "00.000",  # Y
    "Z": "0..000",  # Z

    # Special markers and symbols
    "capital": ".....0",  # Capital follows
    "decimal": ".0...0",  # Decimal follows
    "number": ".0.000",   # Number follows

    # Punctuation
    ".": "..00.0",  # Period
    ",": "..0...",  # Comma
    "?": "..0.00",  # Question mark
    "!": "..000.",  # Exclamation mark
    ":": "..00..",  # Colon
    ";": "..0.0.",  # Semicolon
    "-": "....00",  # Hyphen
    "/": ".0..0.",  # Slash
    "<": ".00..0",  # Less than
    ">": "0..00.",  # Greater than
    "(": "0.0..0",  # Open parenthesis
    ")": ".0.00.",  # Close parenthesis
    "space": "......"  # Space
}

number_dict = {
    "1": "0.....",  # 1
    "2": "0.0...",  # 2
    "3": "00....",  # 3
    "4": "00.0..",  # 4
    "5": "0..0..",  # 5
    "6": "000...",  # 6
    "7": "0000..",  # 7
    "8": "0.00..",  # 8
    "9": ".00...",  # 9
    "0": ".000..",  # 0
}

english_dict = {v: k for k, v in braille_dict.items()}


def translator():
    argumentlist = sys.argv[1:]
    argumentstring = " ".join(argumentlist)

    if argumentstring[0] in [".", "0"] or argumentstring[-1] in [".", "0"]:  # Check if it's Braille
        return (convertToString(argumentstring))
    else:  # Assume it's English
        return (convertToBraille(argumentstring))


def convertToString(argstr):
    returnstr = ""
    i = 0

    while i < len(argstr):
        braille_char = argstr[i:i + 6]
        if braille_char in english_dict:
            char = english_dict[braille_char]
            if char == "capital":
                returnstr += char.upper()
            elif char == "number":
                returnstr += ''.join([english_dict[argstr[j:j + 6]] for j in range(
                    i + 6, len(argstr), 6) if argstr[j:j + 6] in english_dict])
                i += 6  # Skip over the numeric representation
            else:
                returnstr += char
            i += 6  # Move to the next Braille character
        else:
            i += 1  # Move to the next character if not valid

    return returnstr


def convertToBraille(argstr):
    returnstr = ""
    for char in argstr:
        if char == " ":
            returnstr += braille_dict['space']
        elif char.isdigit():
            returnstr += braille_dict["number"] + number_dict[char]
        elif char.isupper():
            returnstr += braille_dict["capital"] + braille_dict[char]
        else:
            returnstr += braille_dict[char.upper()]
    return returnstr


if __name__ == "__main__":
    print(translator())
