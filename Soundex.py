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


def generate_soundex(name, soundex=None):
    if soundex is None:
        soundex = name[0].upper() if name else ""
    
    if len(soundex) == 4:
        return soundex.ljust(4, '0')
    
    if len(name) > 1:
        code = get_soundex_code(name[1])
        if code != '0' and code != soundex[-1]:
            soundex += code
    return generate_soundex(name[1:], soundex)
