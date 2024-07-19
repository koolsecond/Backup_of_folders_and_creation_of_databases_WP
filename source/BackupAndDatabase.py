import os
import shutil
import sys

def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def format_size(size):
    return f"{size / (1024 * 1024):,.0f}MB"

def copy_with_progress(src, dst):
    total_size = get_folder_size(src)
    copied_size = 0
    last_progress = -1

    def progress_update(src_file, dst_file):
        nonlocal copied_size, last_progress
        copied_size += os.path.getsize(src_file)
        progress = int((copied_size / total_size) * 100)
        if progress % 10 == 0 and progress != last_progress and progress != 0:
            print(f"{progress}% ({format_size(copied_size)}/{format_size(total_size)})")
            last_progress = progress

    if not os.path.exists(src):
        print(f"Error: Source folder '{src}' does not exist.")
        return

    if not os.path.exists(dst):
        print(f"Error: Destination folder '{dst}' does not exist.")
        return

    print(f"0% (0MB/{format_size(total_size)})")  # Initial 0% output

    for dirpath, dirnames, filenames in os.walk(src):
        rel_path = os.path.relpath(dirpath, src)
        dest_dir = os.path.join(dst, rel_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file in filenames:
            src_file = os.path.join(dirpath, file)
            dst_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dst_file)
            progress_update(src_file, dst_file)

    # Final progress update to 100% when done
    if last_progress != 100:
        print(f"100% ({format_size(total_size)}/{format_size(total_size)})")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BackupAndDatabase.py <source_folder> <destination_folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]

    copy_with_progress(source_folder, destination_folder)
