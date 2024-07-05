def generate_soundex(name):
    if not name:
        return ""

    soundex = [name[0].upper()]  # Start with the first letter (capitalized)
    prev_code = get_soundex_code(soundex[0])

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex.append(code)
            prev_code = code
        if len(soundex) == 4:
            break

    soundex.extend(['0'] * (4 - len(soundex)))  # Pad with zeros if necessary
    return ''.join(soundex)[:4]  # Ensure soundex is exactly 4 characters long

