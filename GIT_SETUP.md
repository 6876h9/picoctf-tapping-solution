# Git Repository Setup Instructions

## Repository Information

**Repository Name:** `picoctf-tapping-solution`  
**Author:** 6876h9  
**Repository URL:** (To be hosted on GitHub)  
**License:** MIT

---

## Repository Description

```
Comprehensive solution for PicoCTF Tapping challenge (Cryptography, 200 points).
Includes network-based Morse code decoder using pwntools, offline decoder for testing,
and detailed technical documentation with complete Morse code reference and Python examples.
```

---

## Initial Setup (for fresh repository)

### 1. Create New Repository on GitHub

```bash
# Create a new repo on GitHub at https://github.com/6876h9/picoctf-tapping-solution
# Do NOT initialize with README (we have one)
# Do NOT add .gitignore (we have one)
```

### 2. Clone and Set Up Locally

```bash
git clone https://github.com/6876h9/picoctf-tapping-solution.git
cd picoctf-tapping-solution
```

### 3. Configure User Information

```bash
git config user.name "6876h9"
git config user.email "dev@scarynate.dev"
```

### 4. Verify Configuration

```bash
git config --list | grep user
```

---

## Repository Structure

```
picoctf-tapping-solution/
├── README.md              # Main documentation
├── TECHNICAL.md           # Detailed technical analysis
├── solver.py              # Network-based solver (main script)
├── decode_offline.py      # Offline Morse decoder
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore patterns
```

---

## Common Git Commands

### Clone Repository

```bash
git clone https://github.com/6876h9/picoctf-tapping-solution.git
```

### Install and Run

```bash
cd picoctf-tapping-solution
pip install -r requirements.txt
python3 solver.py
```

### Update Changes

```bash
git add .
git commit -m "Description of changes"
git push origin master
```

### View Commit History

```bash
git log --oneline
git log --graph --all --decorate --oneline
```

---

## File Descriptions

### solver.py
Main solver script that connects to the PicoCTF server and decodes the Morse transmission.

**Usage:**
```bash
python3 solver.py
```

**Output:**
```
============================================================
PicoCTF Tapping Challenge Solver
Author: 6876h9
============================================================

[*] Establishing connection to fickle-tempest.picoctf.net:52422...
[+] Connection established
[+] Received transmission:
    .--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...

[*] Analysis:
    Total sequences: 45
    Valid sequences: 45
    Contains flag delimiters: True

[*] Decoding Morse sequences...

============================================================
[+] DECODED FLAG: PICOCTF{m0rse_c0d3_1s_fun_3874078c}
============================================================
```

### decode_offline.py
Standalone offline decoder for local testing without network access.

**Usage:**
```bash
# Decode Morse to text
python3 decode_offline.py decode ".--. .. -.-. ---"

# Encode text to Morse
python3 decode_offline.py encode "PICOCTF"

# Display reference chart
python3 decode_offline.py chart

# Decode from file
python3 decode_offline.py file morse_message.txt
```

### README.md
Professional documentation including:
- Challenge overview and problem statement
- Morse code fundamentals
- Solution approach
- Python implementation examples
- Complete Morse code reference table
- Architecture diagram

### TECHNICAL.md
In-depth technical analysis:
- Challenge transmission breakdown
- Morse code theory and standards
- Implementation architecture and components
- Algorithm complexity analysis
- Code walkthrough with examples
- Debugging and performance metrics

### requirements.txt
Python package dependencies:
```
pwntools>=4.9.0
```

---

## Commit History Template

Use this format for meaningful commits:

```
git commit -m "Brief description (present tense)

- Detailed change 1
- Detailed change 2
- Detailed change 3"
```

Example:
```
git commit -m "Add solver implementation

- Create network socket connection handler
- Implement Morse code dictionary and decoder
- Add error handling and validation
- Include progress indicators"
```

---

## Repository Best Practices

1. Never commit credentials or sensitive data
2. Keep commits small and focused
3. Write descriptive commit messages
4. Test locally before pushing
5. Use .gitignore to exclude unnecessary files
6. Tag releases with semantic versioning

Example tagging:
```bash
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

---

## Troubleshooting

### Authentication Issues

```bash
# Use SSH keys for authentication
ssh-keygen -t rsa -b 4096 -C "dev@scarynate.dev"

# Add SSH key to GitHub account
cat ~/.ssh/id_rsa.pub
```

### Undoing Changes

```bash
# Discard local changes
git checkout -- <file>

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

### View Differences

```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --cached

# Show changes in specific file
git diff <file>
```

---

## License

MIT License - See LICENSE file for details

---

## Contact

Author: 6876h9
Email: dev@scarynate.dev
