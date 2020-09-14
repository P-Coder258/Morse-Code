def encode_morse(message):
	new_message = message.upper()
	morse = ""
	char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

	for x in new_message:
		for y in char_to_dots:
			if x == y:
				morse += char_to_dots[y]
				morse += ' '
	return morse
    
repeat = True
while(repeat):
    code = input("Hey what word would you like to translate to morse code?")
    encoded_message = encode_morse(code)
    print("Your word encoded is " + encoded_message)
    again = input("Would you like to do another word?\nPlease enter yes or no.")
    if (again.lower() != 'yes'):
        repeat = False
