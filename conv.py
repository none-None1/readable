"""
Tool for converting between ='s and Unicode minuses
Usage: python conv.py <infile> <outfile>
"""
import sys

if len(sys.argv) > 1:
    fi = open(sys.argv[1], encoding="utf-8")
else:
    fi = sys.stdin
if len(sys.argv) > 2:
    fo = open(sys.argv[2], "w", encoding="utf-8")
else:
    fo = sys.stdout
z = fi.read()
if "=" in z:
    print(z.replace("=", "\u2212"), file=fo)
else:
    print(z.replace("\u2212", "="), file=fo)
