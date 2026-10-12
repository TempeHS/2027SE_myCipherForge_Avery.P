"""Test Phase 5 (your wild card) in isolation.

Run from the project root with:  python tests/test_phase5.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import phase5_encrypt, phase5_decrypt

test = "Hello World!"
encrypted = phase5_encrypt(test, {})
print(f"Original:  {test}")
print(f"Phase 5:   {encrypted}")
print(f"Reversed:  {phase5_decrypt(encrypted, {})}")
print(f"Match:     {test == phase5_decrypt(encrypted, {})}")


encrypted = phase5_encrypt(test, {})
decrypted = phase5_decrypt(encrypted, {})

# add these lines
print(f"Encrypted type: {type(encrypted).__name__}")
print(f"Decrypted type: {type(decrypted).__name__}")
print(f"Type check passed: {isinstance(encrypted, str) and isinstance(decrypted, str)}")
