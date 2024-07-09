import os
import shutil
import sys


def parse_arguments():
    if len(sys.argv) < 3:
        print("Usage: python copy_files.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    return source_dir, dest_dir


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def copy_files_recursively(src, dst):
    try:
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            if os.path.isdir(src_path):
                copy_files_recursively(src_path, dst)
            else:
                file_extension = os.path.splitext(item)[1][1:].lower()
                if file_extension:  # If there's an extension
                    target_dir = os.path.join(dst, file_extension)
                    create_directory(target_dir)
                    shutil.copy2(src_path, target_dir)
    except Exception as e:
        print(f"Error processing {src}: {e}")


def main():
    source_dir, dest_dir = parse_arguments()

    if not os.path.exists(source_dir):
        print(f"The source directory '{source_dir}' does not exist.")
        sys.exit(1)

    create_directory(dest_dir)
    copy_files_recursively(source_dir, dest_dir)
    print(
        f"Files copied from '{source_dir}' to '{dest_dir}' and sorted by file extension."
    )


if __name__ == "__main__":
    main()
