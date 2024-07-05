def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def initialize_soundex(name):
    if not name:
        return "", '0'  # Return empty string and '0' if name is empty
    
    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def should_add_code(char, code, prev_code):
    return code != '0' and code != prev_code

def generate_soundex(name):
    if not name:
        return ""

    soundex, prev_code = initialize_soundex(name)
    if not soundex:
        return ""

    i = 1
    while len(soundex) < 4 and i < len(name):
        char = name[i]
        code = get_soundex_code(char)
        if should_add_code(char, code, prev_code):
            soundex += code
            prev_code = code
        i += 1

    return soundex.ljust(4, '0')
