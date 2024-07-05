def generate_soundex(name):
    if not name:
        return ""

    # Initialize the soundex with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    # Process each character after the first one
    for char in name[1:]:
        code = get_soundex_code(char.upper())
        
        # Ignore non-mapped characters
        if code != '0':
            # Append the code if it's different from the previous code and not a duplicate
            if code != prev_code:
                soundex += code
                prev_code = code
            
            # Stop if the soundex length is 4
            if len(soundex) == 4:
                break

    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex
