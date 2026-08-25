import os
import sys

# Ensure the repository root is on the Python path so that ``calculator`` can be imported.
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from calculator import add, subtract

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-4, -6) == -10

def test_subtract_positive_numbers():
    assert subtract(10, 3) == 7

def test_subtract_mixed_sign_numbers():
    assert subtract(-5, 2) == -7
