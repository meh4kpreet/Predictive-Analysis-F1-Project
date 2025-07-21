import zipfile
import os
import pandas as pd

RAW_DATA_DIR = 'data/raw_kaggle'
ZIP_FILE_PATH = 'archive.zip'

def extract_zip():
    if not os.path.exists(RAW_DATA_DIR):
        os.makedirs(RAW_DATA_DIR)

    with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
        zip_ref.extractall(RAW_DATA_DIR)
    print("Extraction complete.")

def main():
    extract_zip()

if __name__ == '__main__':
    main()
