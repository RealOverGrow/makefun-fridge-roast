#!/usr/bin/env python3
"""Fridge roast, one line.

Entry: a program that writes one text to /output/entry.txt: a one-line
roast of a fridge.
"""
import os

JOKE = "My fridge hums all night like it's judging my 2 a.m. snack choices — and honestly, it's right."

# The entry must be exactly one line.
assert "\n" not in JOKE, "JOKE must be a single line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
