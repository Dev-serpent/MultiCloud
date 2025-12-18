import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VENDOR_DIR = os.path.join(BASE_DIR, "vendor")

if VENDOR_DIR not in sys.path:
    sys.path.insert(0, VENDOR_DIR)
