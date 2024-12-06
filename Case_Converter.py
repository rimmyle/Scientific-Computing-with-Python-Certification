# Converts text from camel case to snake cased
# pascal_or_camel_cased_string: passed string to be converted to snake cased string.
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Converts the message to list of words, then converts the case of each word
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))
