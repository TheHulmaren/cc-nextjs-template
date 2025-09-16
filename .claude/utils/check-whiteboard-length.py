#!/usr/bin/env python3
import os

def check_whiteboard_length():
    filepath = "CLAUDE/WHITEBOARD.md"
    
    if not os.path.exists(filepath):
        return  # Silently exit if file doesn't exist
    
    # Count lines
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = sum(1 for _ in f)
    
    # Output warning if exceeds 1000 lines
    if lines > 1200:
        print(f"⚠️ WHITEBOARD.md has {lines} lines (exceeds 1200). Please ask the user to help compress it to maintain performance.")

if __name__ == "__main__":
    check_whiteboard_length()