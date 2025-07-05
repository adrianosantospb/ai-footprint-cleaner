import unicodedata
import re
import os

# Default list of file extensions supported by the cleaner
SUPPORTED_EXTENSIONS = (
    '.py', '.pyw', '.ipynb',
    '.c', '.cpp', '.cc', '.cxx', '.h', '.hpp',
    '.cs', '.go', '.java', '.kt', '.kts',
    '.js', '.ts', '.jsx', '.tsx',
    '.rb', '.php', '.rs', '.swift',
    '.sh', '.bash', '.zsh', '.fish',
    '.lua', '.pl', '.r', '.m',
    '.html', '.htm', '.xml', '.xhtml',
    '.css', '.scss', '.sass',
    '.md', '.markdown',
    '.json', '.yaml', '.yml', '.toml', '.ini',
    '.env', '.cfg', '.conf', '.config',
    '.dockerfile', '.make', '.txt', '.csv', '.tsv', '.log',
)

# Files without extensions that are still valid source/build files
SPECIAL_FILES = {'Dockerfile', 'Makefile', 'CMakeLists.txt'}

def clean_file(file_path: str):
    """
    Cleans a single file in place by removing:
    - Byte Order Mark (BOM)
    - Zero-width and invisible Unicode characters
    - Control characters (excluding tabs and newlines)
    - Non-ASCII printable characters
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Remove BOM
        content = content.replace('\ufeff', '')

        # Remove specific invisible characters (zero-width spaces, etc.)
        content = re.sub(r'[\u200b\u200c\u200d\u2060\uFEFF]', '', content)

        # Remove control characters, keep newline and tab
        content = ''.join(
            c for c in content
            if unicodedata.category(c)[0] != 'C' or c in '\n\t'
        )

        # Keep only printable ASCII characters (plus newline and tab)
        content = ''.join(
            c for c in content
            if (32 <= ord(c) <= 126) or c in '\n\t'
        )

        # Overwrite file with cleaned content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[CLEANED] {file_path}")
    except Exception as e:
        print(f"[ERROR] Could not clean {file_path}: {e}")

def clean_directory(base_path: str, extra_extensions=None, exclude_extensions=None):
    """
    Recursively walks through the given directory and cleans all supported files.

    :param base_path: root directory to clean
    :param extra_extensions: set of additional file extensions to include
    :param exclude_extensions: set of file extensions to exclude
    """
    all_extensions = set(SUPPORTED_EXTENSIONS)

    if extra_extensions:
        all_extensions.update(extra_extensions)

    if exclude_extensions:
        all_extensions.difference_update(exclude_extensions)

    for root, _, files in os.walk(base_path):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in all_extensions or filename in SPECIAL_FILES:
                clean_file(os.path.join(root, filename))
