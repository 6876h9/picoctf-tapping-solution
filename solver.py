#!/usr/bin/env python3
"""
PicoCTF Tapping Challenge Solver
Decodes Morse code transmitted over network connection
"""

from pwn import *

# Complete Morse code dictionary (A-Z, 0-9)
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


def fetch_morse_from_server(host, port, timeout=10):
    """
    Connect to the challenge server and retrieve the Morse code message.
    
    Args:
        host (str): Target hostname or IP address
        port (int): Target port number
        timeout (int): Connection timeout in seconds (default: 10)
    
    Returns:
        str: The Morse code message or empty string on failure
    
    Raises:
        ConnectionError: If unable to establish connection
    """
    try:
        print(f"[*] Establishing connection to {host}:{port}...")
        conn = remote(host, port, timeout=timeout)
        print(f"[+] Connection established")
        
        morse_message = conn.recvline().decode().strip()
        conn.close()
        
        return morse_message
    except Exception as e:
        print(f"[-] Error connecting to server: {e}")
        return ""


def validate_morse(morse_string):
    """
    Validate that the input string contains valid Morse code characters.
    
    Args:
        morse_string (str): String to validate
    
    Returns:
        bool: True if string contains only Morse-valid characters
    """
    valid_chars = {'.', '-', ' ', '{', '}'}
    return all(char in valid_chars for char in morse_string)


def decode_morse(morse_string):
    """
    Decode a Morse code string to plaintext characters.
    
    The function handles:
    - Individual Morse sequences separated by spaces
    - Curly braces { } (used in flag format)
    - Unknown sequences (marked as ?)
    
    Args:
        morse_string (str): Morse code with spaces separating characters
    
    Returns:
        tuple: (decoded_string, error_count)
    
    Example:
        >>> decode_morse(".-. .--. .. -.-. --- -.-. - ..-. { -- }")
        ('RP1PICOCTF{ m }', 0)
    """
    result = []
    error_count = 0
    morse_chars = morse_string.split(' ')
    
    for morse_char in morse_chars:
        # Handle flag format delimiters
        if morse_char in ['{', '}']:
            result.append(morse_char)
        # Decode standard Morse sequences
        elif morse_char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[morse_char])
        # Skip empty strings from multiple consecutive spaces
        elif morse_char == '':
            continue
        # Unknown character
        else:
            result.append('?')
            error_count += 1
    
    return ''.join(result), error_count


def analyze_morse(morse_string):
    """
    Analyze Morse code structure and provide statistics.
    
    Args:
        morse_string (str): Morse code to analyze
    
    Returns:
        dict: Statistics about the Morse code
    """
    morse_chars = morse_string.split(' ')
    valid_morse_chars = [m for m in morse_chars if m in MORSE_CODE_DICT]
    
    return {
        'total_sequences': len(morse_chars),
        'valid_sequences': len(valid_morse_chars),
        'length': len(morse_string),
        'has_braces': '{' in morse_string and '}' in morse_string,
    }


def main():
    """Main execution function"""
    print("=" * 60)
    print("PicoCTF Tapping Challenge Solver")
    print("Author: 6876h9")
    print("=" * 60)
    
    host = "fickle-tempest.picoctf.net"
    port = 52422
    
    # Attempt to fetch Morse code from server
    morse_message = fetch_morse_from_server(host, port)
    
    if not morse_message:
        print("[-] Failed to retrieve message from server")
        return 1
    
    # Validate Morse code format
    if not validate_morse(morse_message):
        print("[-] Warning: Input contains unexpected characters")
    
    print(f"\n[+] Received transmission:")
    print(f"    {morse_message[:70]}...")
    
    # Analyze the Morse code structure
    analysis = analyze_morse(morse_message)
    print(f"\n[*] Analysis:")
    print(f"    Total sequences: {analysis['total_sequences']}")
    print(f"    Valid sequences: {analysis['valid_sequences']}")
    print(f"    Contains flag delimiters: {analysis['has_braces']}")
    
    # Decode the Morse message
    print(f"\n[*] Decoding Morse sequences...")
    flag, errors = decode_morse(morse_message)
    
    if errors > 0:
        print(f"[!] Warning: {errors} unknown sequences encountered")
    
    print("\n" + "=" * 60)
    print(f"[+] DECODED FLAG: {flag}")
    print("=" * 60 + "\n")
    
    return 0


if __name__ == "__main__":
    exit(main())
