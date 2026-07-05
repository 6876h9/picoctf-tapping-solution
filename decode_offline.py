#!/usr/bin/env python3
"""
Offline Morse Code Decoder
Decodes Morse code from file or command line without network connection
Useful for testing and analyzing Morse patterns locally
"""

import sys
from pathlib import Path


# Complete Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

# Reverse dictionary for encoding plaintext to Morse
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def decode_morse(morse_string):
    """
    Decode Morse code to plaintext.
    
    Args:
        morse_string (str): Morse code with spaces separating characters
    
    Returns:
        str: Decoded plaintext
    """
    result = []
    morse_chars = morse_string.split(' ')
    
    for morse_char in morse_chars:
        if morse_char in ['{', '}']:
            result.append(morse_char)
        elif morse_char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[morse_char])
        elif morse_char == '':
            continue
        else:
            result.append('?')
    
    return ''.join(result)


def encode_to_morse(text):
    """
    Encode plaintext to Morse code.
    
    Args:
        text (str): Plaintext to encode
    
    Returns:
        str: Morse code representation
    """
    morse_result = []
    
    for char in text.upper():
        if char in REVERSE_MORSE_DICT:
            morse_result.append(REVERSE_MORSE_DICT[char])
        elif char in ['{', '}']:
            morse_result.append(char)
        elif char == ' ':
            morse_result.append(' ')
    
    return ' '.join(morse_result)


def print_morse_chart():
    """Display complete Morse code reference chart"""
    print("\nMorse Code Reference Chart")
    print("=" * 50)
    print("\nLetters (A-Z):")
    print("-" * 50)
    for i, (morse, char) in enumerate(sorted(MORSE_CODE_DICT.items()), 1):
        if char.isalpha():
            print(f"{char}: {morse:8s}", end="  ")
            if i % 4 == 0:
                print()
    
    print("\n\nDigits (0-9):")
    print("-" * 50)
    for morse, char in sorted(MORSE_CODE_DICT.items()):
        if char.isdigit():
            print(f"{char}: {morse:8s}", end="  ")
    print("\n")


def main():
    """Main execution"""
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  {sys.argv[0]} decode <morse_string>")
        print(f"  {sys.argv[0]} encode <plaintext>")
        print(f"  {sys.argv[0]} chart")
        print(f"  {sys.argv[0]} file <input_file>")
        print("\nExamples:")
        print(f"  {sys.argv[0]} decode '.--. .. -.-. ---'")
        print(f"  {sys.argv[0]} encode 'PICOCTF'")
        print(f"  {sys.argv[0]} chart")
        return 1
    
    command = sys.argv[1].lower()
    
    if command == 'decode':
        if len(sys.argv) < 3:
            print("Error: Please provide Morse code to decode")
            return 1
        
        morse_input = sys.argv[2]
        decoded = decode_morse(morse_input)
        
        print(f"\nMorse Input:  {morse_input}")
        print(f"Decoded:      {decoded}\n")
        
    elif command == 'encode':
        if len(sys.argv) < 3:
            print("Error: Please provide text to encode")
            return 1
        
        text_input = sys.argv[2]
        encoded = encode_to_morse(text_input)
        
        print(f"\nText Input:   {text_input}")
        print(f"Morse Code:   {encoded}\n")
        
    elif command == 'chart':
        print_morse_chart()
        
    elif command == 'file':
        if len(sys.argv) < 3:
            print("Error: Please provide input file path")
            return 1
        
        file_path = Path(sys.argv[2])
        
        if not file_path.exists():
            print(f"Error: File '{file_path}' not found")
            return 1
        
        try:
            with open(file_path, 'r') as f:
                morse_content = f.read().strip()
            
            decoded = decode_morse(morse_content)
            
            print(f"\nFile: {file_path}")
            print(f"Decoded: {decoded}\n")
            
        except Exception as e:
            print(f"Error reading file: {e}")
            return 1
    
    else:
        print(f"Error: Unknown command '{command}'")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
