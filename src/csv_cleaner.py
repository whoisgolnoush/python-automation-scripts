# src/csv_cleaner.py
import argparse
import pandas as pd
import os

def clean_csv(infile, outfile=None, dropna=True):
    df = pd.read_csv(infile)
    if dropna:
        df = df.dropna()
    if outfile is None:
        base, ext = os.path.splitext(infile)
        outfile = base + "_cleaned" + ext
    df.to_csv(outfile, index=False)
    print(f"Saved cleaned CSV to: {outfile}")

def main():
    p = argparse.ArgumentParser(description="Simple CSV cleaner.")
    p.add_argument("infile", help="input CSV file")
    p.add_argument("--outfile", help="output CSV file (optional)")
    p.add_argument("--no-dropna", dest="dropna", action="store_false",
                   help="do not drop rows with NaN")
    args = p.parse_args()
    clean_csv(args.infile, args.outfile, args.dropna)

if __name__ == "__main__":
    main()
