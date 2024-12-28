# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '? '
    return morse_code.strip()

# Function to convert Morse code to text
def morse_to_text(morse):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    text = ''
    morse_chars = morse.split(' ')
    for code in morse_chars:
        if code in reverse_dict:
            text += reverse_dict[code]
        elif code == '/':
            text += ' '
        else:
            text += '?' 
    return text

# Main function for user interaction
def main():
    print("Welcome to the Text-Morse Converter!")
    while True:
        print("\nChoose an option:")
        print("1. Convert Text to Morse Code")
        print("2. Convert Morse Code to Text")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            user_text = input("Enter the text to convert to Morse code: ")
            print("Morse Code:", text_to_morse(user_text))
        elif choice == '2':
            user_morse = input("Enter the Morse code to convert to text (use spaces between characters and '/' for spaces): ")
            print("Text:", morse_to_text(user_morse))
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
