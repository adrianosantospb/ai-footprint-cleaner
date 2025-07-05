
from src.aifootprintcleaner.cleaner import clean_directory


if __name__ == '__main__':
    target_dir = input("Enter directory to clean (default: current directory): ").strip()
    if not target_dir:
        target_dir = '.'

    clean_directory(target_dir, extra_extensions={'.md'}, exclude_extensions={'.log'})
    print(f"Cleaning completed for directory: {target_dir}")
