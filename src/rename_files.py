# src/rename_files.py
import os
import argparse

def rename_files(folder, prefix, dry_run=False):
    files = sorted(os.listdir(folder))
    for i, fname in enumerate(files, 1):
        old = os.path.join(folder, fname)
        if os.path.isfile(old):
            new_name = f"{prefix}_{i:03d}_{fname}"
            new = os.path.join(folder, new_name)
            if dry_run:
                print(f"[DRY] {old} -> {new}")
            else:
                os.rename(old, new)
                print(f"{old} -> {new}")

def main():
    p = argparse.ArgumentParser(description="Batch rename files with prefix and index.")
    p.add_argument("folder", help="target folder")
    p.add_argument("--prefix", default="file", help="prefix to add")
    p.add_argument("--dry", action="store_true", help="dry run (don't rename, just show)")
    args = p.parse_args()

    rename_files(args.folder, args.prefix, args.dry)

if __name__ == "__main__":
    main()
