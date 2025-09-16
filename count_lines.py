#!/usr/bin/env python3
"""
Code Line Counter Script
Analyzes code in the src directory and provides statistics by language.
"""

from pathlib import Path
from collections import defaultdict
from typing import Dict, Tuple
import json

# Language extensions mapping
LANGUAGE_EXTENSIONS = {
    'TypeScript': ['.ts', '.tsx'],
    'JavaScript': ['.js', '.jsx'],
    'CSS': ['.css'],
    'SCSS/SASS': ['.scss', '.sass'],
    'HTML': ['.html'],
    'JSON': ['.json'],
    'SQL': ['.sql'],
    'Markdown': ['.md'],
    'Python': ['.py'],
    'Shell': ['.sh'],
    'YAML': ['.yml', '.yaml'],
    'Environment': ['.env', '.env.local', '.env.production'],
    'Prisma': ['.prisma'],
    'Config': ['.config.js', '.config.ts', '.config.json'],
}

# Files to ignore
IGNORE_PATTERNS = [
    'node_modules',
    '.next',
    'dist',
    'build',
    '.git',
    '__pycache__',
    '.DS_Store',
    'coverage',
    '.turbo',
]

def get_file_extension(file_path: Path) -> str:
    """Get the file extension including compound extensions like .config.js"""
    name = file_path.name

    # Check for compound extensions first
    for ext in ['.config.js', '.config.ts', '.config.json', '.env.local', '.env.production']:
        if name.endswith(ext):
            return ext

    # Return simple extension
    return file_path.suffix

def get_language(file_path: Path) -> str:
    """Determine the language based on file extension"""
    ext = get_file_extension(file_path)

    for lang, extensions in LANGUAGE_EXTENSIONS.items():
        if ext in extensions:
            return lang

    # Default to extension name if not mapped
    return f"Other ({ext})" if ext else "Unknown"

def should_ignore(path: Path) -> bool:
    """Check if path should be ignored"""
    path_str = str(path)
    for pattern in IGNORE_PATTERNS:
        if pattern in path_str:
            return True
    return False

def count_lines(file_path: Path) -> Tuple[int, int, int]:
    """
    Count lines in a file
    Returns: (total_lines, code_lines, blank_lines, comment_lines)
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except:
        return (0, 0, 0)

    total = len(lines)
    blank = sum(1 for line in lines if line.strip() == '')

    # Simple comment detection (can be improved)
    comment = 0
    in_multiline_comment = False

    for line in lines:
        stripped = line.strip()

        # Check for multiline comments (JS/TS/CSS style)
        if '/*' in stripped:
            in_multiline_comment = True
        if in_multiline_comment:
            comment += 1
        if '*/' in stripped:
            in_multiline_comment = False
            continue

        # Single line comments
        if not in_multiline_comment:
            if stripped.startswith('//') or stripped.startswith('#') or stripped.startswith('<!--'):
                comment += 1

    code = total - blank - comment
    return (total, code, blank)

def analyze_directory(root_path: Path) -> Dict:
    """Analyze all code files in the directory"""
    stats = defaultdict(lambda: {
        'files': 0,
        'total_lines': 0,
        'code_lines': 0,
        'blank_lines': 0,
        'file_list': []
    })

    total_stats = {
        'files': 0,
        'total_lines': 0,
        'code_lines': 0,
        'blank_lines': 0,
    }

    for file_path in root_path.rglob('*'):
        if file_path.is_file() and not should_ignore(file_path):
            language = get_language(file_path)

            # Skip non-code files
            if language == "Unknown":
                continue

            total, code, blank = count_lines(file_path)

            # Update language stats
            stats[language]['files'] += 1
            stats[language]['total_lines'] += total
            stats[language]['code_lines'] += code
            stats[language]['blank_lines'] += blank
            stats[language]['file_list'].append(str(file_path.relative_to(root_path)))

            # Update total stats
            total_stats['files'] += 1
            total_stats['total_lines'] += total
            total_stats['code_lines'] += code
            total_stats['blank_lines'] += blank

    return dict(stats), total_stats

def print_stats(stats: Dict, total_stats: Dict, show_files: bool = False):
    """Print formatted statistics"""
    print("\n" + "="*70)
    print("                    CODE LINE COUNTER REPORT")
    print("="*70)

    # Sort languages by code lines
    sorted_langs = sorted(stats.items(), key=lambda x: x[1]['code_lines'], reverse=True)

    print("\n📊 LANGUAGE BREAKDOWN:")
    print("-"*70)
    print(f"{'Language':<20} {'Files':>8} {'Code':>10} {'Blank':>10} {'Total':>10} {'%':>8}")
    print("-"*70)

    for lang, data in sorted_langs:
        if data['code_lines'] > 0:
            percentage = (data['code_lines'] / total_stats['code_lines'] * 100) if total_stats['code_lines'] > 0 else 0
            print(f"{lang:<20} {data['files']:>8} {data['code_lines']:>10,} {data['blank_lines']:>10,} {data['total_lines']:>10,} {percentage:>7.1f}%")

    print("-"*70)
    print(f"{'TOTAL':<20} {total_stats['files']:>8} {total_stats['code_lines']:>10,} {total_stats['blank_lines']:>10,} {total_stats['total_lines']:>10,} {'100.0':>7}%")

    # Top 5 languages pie chart (text-based)
    print("\n📈 TOP LANGUAGES BY CODE LINES:")
    print("-"*70)
    top_5 = sorted_langs[:5]
    for lang, data in top_5:
        percentage = (data['code_lines'] / total_stats['code_lines'] * 100) if total_stats['code_lines'] > 0 else 0
        bar_length = int(percentage / 2)  # Scale to 50 chars max
        bar = "█" * bar_length
        print(f"{lang:<15} {bar:<50} {percentage:.1f}%")

    # Summary statistics
    print("\n📋 SUMMARY:")
    print("-"*70)
    print(f"Total Files:        {total_stats['files']:,}")
    print(f"Total Code Lines:   {total_stats['code_lines']:,}")
    print(f"Total Blank Lines:  {total_stats['blank_lines']:,}")
    print(f"Total Lines:        {total_stats['total_lines']:,}")

    if total_stats['total_lines'] > 0:
        code_density = (total_stats['code_lines'] / total_stats['total_lines'] * 100)
        print(f"Code Density:       {code_density:.1f}%")

    # Show file lists if requested
    if show_files:
        print("\n📁 FILE LISTS BY LANGUAGE:")
        print("-"*70)
        for lang, data in sorted_langs[:3]:  # Show only top 3 for brevity
            if data['files'] > 0:
                print(f"\n{lang} ({data['files']} files):")
                for file in sorted(data['file_list'])[:10]:  # Show max 10 files
                    print(f"  • {file}")
                if len(data['file_list']) > 10:
                    print(f"  ... and {len(data['file_list']) - 10} more files")

def save_json_report(stats: Dict, total_stats: Dict, output_file: str = "code_stats.json"):
    """Save statistics to JSON file"""
    report = {
        'languages': stats,
        'total': total_stats,
        'summary': {
            'code_density': (total_stats['code_lines'] / total_stats['total_lines'] * 100) if total_stats['total_lines'] > 0 else 0,
            'top_language': max(stats.items(), key=lambda x: x[1]['code_lines'])[0] if stats else 'None'
        }
    }

    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n💾 JSON report saved to: {output_file}")

def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description='Count lines of code in src directory')
    parser.add_argument('--path', default='src', help='Path to analyze (default: src)')
    parser.add_argument('--show-files', action='store_true', help='Show file lists for each language')
    parser.add_argument('--json', action='store_true', help='Save JSON report')
    parser.add_argument('--json-output', default='code_stats.json', help='JSON output filename')

    args = parser.parse_args()

    # Get the path to analyze
    root_path = Path(args.path)

    if not root_path.exists():
        print(f"❌ Error: Path '{root_path}' does not exist!")
        return

    print(f"🔍 Analyzing: {root_path.absolute()}")
    print(f"⏳ Processing files...")

    # Analyze directory
    stats, total_stats = analyze_directory(root_path)

    if not stats:
        print("❌ No code files found in the specified directory!")
        return

    # Print statistics
    print_stats(stats, total_stats, args.show_files)

    # Save JSON report if requested
    if args.json:
        save_json_report(stats, total_stats, args.json_output)

    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    main()