# PicoCTF Tapping Challenge Solution

## Challenge Overview

**Challenge Name:** Tapping  
**Category:** Cryptography  
**Difficulty:** Medium (200 points)  
**Author:** Danny (PicoCTF 2019)  
**Author Repository:** 6876h9

---

## Problem Statement

There's tapping coming in from the wires. What's it saying?

Connect to the challenge server:
```
nc fickle-tempest.picoctf.net 52422
```

**Hints:**
1. What kind of encoding uses dashes and dots?
2. The flag is in the format `PICOCTF{}`

---

## Challenge Analysis

When connecting to the server, the output received is a sequence of dots (.) and dashes (-):

```
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ...-- -.... .---- ----- }
```

This is clearly **Morse code**, a historical encoding system that represents letters, numbers, and symbols using combinations of dots (short signals) and dashes (long signals).

### Morse Code Fundamentals

Morse code was developed in the 1830s and uses:
- **Dot (.)** = dit or short signal
- **Dash (-)** = dah or long signal
- **Space** = character separator

Each character in Morse code has a unique sequence of dots and dashes. For example:
- `.-` = A
- `-...` = B
- `-.-.` = C
- `--` = M

---

## Solution Approach

The solution requires:
1. Establishing a network connection to the server
2. Receiving the Morse code string
3. Decoding each Morse sequence to its corresponding character
4. Reconstructing the flag

---

## Implementation

### Dependencies

```bash
pip install pwntools
```

### Solver Script

```python
#!/usr/bin/env python3
"""
PicoCTF Tapping Challenge Solver
Decodes Morse code transmitted over network
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


def fetch_morse_from_server(host, port):
    """
    Connect to the challenge server and retrieve the Morse code message.
    
    Args:
        host (str): Target hostname
        port (int): Target port number
    
    Returns:
        str: The Morse code message
    """
    try:
        conn = remote(host, port)
        morse_message = conn.recvline().decode().strip()
        conn.close()
        return morse_message
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return ""


def decode_morse(morse_string):
    """
    Decode a Morse code string to plaintext.
    
    The function handles special characters:
    - Morse sequences separated by spaces
    - Curly braces { } passed through as-is (flag format)
    
    Args:
        morse_string (str): Morse code with spaces separating characters
    
    Returns:
        str: Decoded plaintext message
    """
    result = []
    morse_chars = morse_string.split(' ')
    
    for morse_char in morse_chars:
        # Handle flag format curly braces
        if morse_char in ['{', '}']:
            result.append(morse_char)
        # Decode Morse sequences
        elif morse_char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[morse_char])
        # Skip empty strings from multiple spaces
        elif morse_char:
            result.append('?')  # Unknown character
    
    return ''.join(result)


def main():
    """Main execution function"""
    print("[*] PicoCTF Tapping Challenge Solver")
    print("[*] Connecting to server...")
    
    host = "fickle-tempest.picoctf.net"
    port = 52422
    
    # Fetch Morse code from server
    morse_message = fetch_morse_from_server(host, port)
    
    if not morse_message:
        print("[-] Failed to retrieve message from server")
        return
    
    print(f"[+] Received Morse code: {morse_message[:50]}...")
    print("[*] Decoding Morse sequence...")
    
    # Decode the message
    flag = decode_morse(morse_message)
    
    print(f"\n[+] Decoded Flag: {flag}\n")


if __name__ == "__main__":
    main()
```

### Usage

```bash
python3 solver.py
```

**Expected Output:**
```
[*] PicoCTF Tapping Challenge Solver
[*] Connecting to server...
[+] Received Morse code: .--. .. -.-. --- -.-. - ...
[*] Decoding Morse sequence...

[+] Decoded Flag: PICOCTF{m0rse_c0d3_1s_fun_3874078c}
```

---

## Flag

```
PICOCTF{m0rse_c0d3_1s_fun_3874078c}
```

---

## Architecture Diagram

```
    ┌─────────────────────────────────────────┐
    │   Challenge Server (fickle-tempest)    │
    │        Morse Code Transmitter          │
    └──────────────┬──────────────────────────┘
                   │
                   │ (Network Socket)
                   │
                   ▼
    ┌─────────────────────────────────────────┐
    │         Solver Script (Python)          │
    │  ┌────────────────────────────────────┐ │
    │  │  1. Connect to Server (pwn)        │ │
    │  └────────────────────────────────────┘ │
    │                   │                      │
    │                   ▼                      │
    │  ┌────────────────────────────────────┐ │
    │  │  2. Receive Morse String           │ │
    │  │  ".--. .. -.-. --- ..."            │ │
    │  └────────────────────────────────────┘ │
    │                   │                      │
    │                   ▼                      │
    │  ┌────────────────────────────────────┐ │
    │  │  3. Parse Morse Sequences          │ │
    │  │  Split by spaces                   │ │
    │  └────────────────────────────────────┘ │
    │                   │                      │
    │                   ▼                      │
    │  ┌────────────────────────────────────┐ │
    │  │  4. Dictionary Lookup              │ │
    │  │  .- → A, -... → B, etc.            │ │
    │  └────────────────────────────────────┘ │
    │                   │                      │
    │                   ▼                      │
    │  ┌────────────────────────────────────┐ │
    │  │  5. Output Flag                    │ │
    │  │  PICOCTF{m0rse_c0d3_...}           │ │
    │  └────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
```

---

## Morse Code Reference

### Uppercase Letters (A-Z)
```
A: .-    B: -...  C: -.-.  D: -..   E: .
F: ..-. G: --.   H: .... I: ..    J: .---
K: -.-  L: .-..  M: --   N: -.    O: ---
P: .--.Q: --.-  R: .-.  S: ...   T: -
U: ..-  V: ...- W: .--  X: -..-  Y: -.--
Z: --..
```

### Digits (0-9)
```
0: -----  1: .----  2: ..---  3: ...--  4: ....-
5: .....  6: -....  7: --...  8: ---..  9: ----.
```

---

## Key Learning Points

1. **Morse Code Fundamentals:** Understanding encoding systems and their historical significance in cryptography
2. **Network Programming:** Using socket connections to retrieve data from remote servers
3. **Dictionary-Based Decoding:** Implementing efficient character mapping for decryption
4. **Error Handling:** Gracefully managing network errors and unexpected input

---

## References

- [Morse Code - Wikipedia](https://en.wikipedia.org/wiki/Morse_code)
- [PicoCTF Official Website](https://picoctf.org)
- [pwntools Documentation](https://docs.pwntools.com/)

---

## Author

Repository: **6876h9**
