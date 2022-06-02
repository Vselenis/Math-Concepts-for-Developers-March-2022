def encode(text):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    encoded_text = ''
    count = 1
    for i in range(0, len(text)):
        if len(text) > i+1 and text[i] == text[i + 1]:
            count += 1
        else:
            encoded_text += text[i]
            if count > 1:
                encoded_text += str(count)
            count = 1

    return encoded_text



def decode(text):
    """
    Decodes the text using run-length encoding
    """
    current_letter = ''
    decode_text = ''
    count = ''
    for i in range(0, len(text)):
        if text[i].isalpha():
            if len(text) == i + 1:
                decode_text += text[i]
            elif (text[i + 1]).isalpha():
                decode_text += text[i]
            elif (text[i + 1]).isnumeric():
                current_letter += text[i]

        if text[i].isnumeric():
            if len(text) == i + 1:
                count += text[i]
                decode_text += current_letter * int(count)
                count = ''
                current_letter = ''
            elif (text[i + 1]).isalpha():
                count += text[i]
                decode_text += current_letter * int(count)
                count = ''
                current_letter = ''
            elif (text[i + 1]).isnumeric():
                count += text[i]


    return decode_text



# Test that the functions work on their own
assert encode("AABCCCDEEEE") == "A2BC3DE4"
assert decode("A2BC3DE4") == "AABCCCDEEEE"

# Test that the functions really invert each other
assert decode(encode("AABCCCDEEEE")) == "AABCCCDEEEE"
assert encode(decode("A2BC3DE4")) == "A2BC3DE4"