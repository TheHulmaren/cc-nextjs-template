#!/usr/bin/env python3
import os

def check_whiteboard():
    filepath = "CLAUDE/WHITEBOARD.md"

    if not os.path.exists(filepath):
        print(f"⚠️  {filepath} not found")
        return

    # Get file stats
    file_size = os.path.getsize(filepath)

    # Count lines and words
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.count('\n') + 1
        words = len(content.split())
        chars = len(content)

    # Format file size
    if file_size < 1024:
        size_str = f"{file_size} bytes"
    elif file_size < 1024 * 1024:
        size_str = f"{file_size / 1024:.1f} KB"
    else:
        size_str = f"{file_size / (1024 * 1024):.1f} MB"

    # Print a prominent notification about whiteboard length
    print("=" * 60)
    print("📊 WHITEBOARD.md LENGTH NOTIFICATION")
    print("=" * 60)
    print(f"Lines:  {lines:,}")
    print(f"Words:  {words:,}")
    print(f"Chars:  {chars:,}")
    print(f"Size:   {size_str}")

    # Warning if file is getting large
    if lines > 1200:
        print("=" * 60)
        print(f"⚠️  WARNING: WHITEBOARD.md is getting long!")
        print(f"    ({lines:,} lines - Consider compressing old tasks)")
    elif lines > 500:
        print("-" * 60)
        print(f"📝 Note: WHITEBOARD.md is moderately sized ({lines} lines)")

    print("=" * 60)
    print()

    # Now output the actual whiteboard content for context
    print("WHITEBOARD.md CONTENT:")
    print("-" * 60)
    print(content)
    print("-" * 60)
    print(f"[End of WHITEBOARD.md - {lines} lines, {words} words]")

if __name__ == "__main__":
    check_whiteboard()