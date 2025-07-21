# data_ingestion.py

import pandas as pd
import os

# Define the directory where your raw Kaggle CSV files are located
RAW_DATA_DIR = 'data/raw_kaggle'

def load_csv_file(file_name, index_col=None):
    """
    Loads a single CSV file into a pandas DataFrame.
    file_name: The name of the CSV file (e.g., 'lap_times.csv').
    index_col: Optional, specifies a column to use as the DataFrame index.
    """
    file_path = os.path.join(RAW_DATA_DIR, file_name)
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}. Please ensure your CSVs are in the '{RAW_DATA_DIR}' directory.")
        return None
    
    try:
        df = pd.read_csv(file_path, index_col=index_col)
        print(f"Successfully loaded {file_name} with {len(df)} rows.")
        return df
    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        return None

def ingest_f1_data():
    """
    Loads all necessary F1 data CSVs from the raw_kaggle directory.
    Returns a dictionary of DataFrames.
    """
    print(f"--- Starting Data Ingestion from {RAW_DATA_DIR} ---")

    data = {}

    # Core race data
    data['races_df'] = load_csv_file('races.csv')
    data['results_df'] = load_csv_file('results.csv')
    data['lap_times_df'] = load_csv_file('lap_times.csv')
    data['pit_stops_df'] = load_csv_file('pit_stops.csv')

    # Metadata (useful for joining and understanding IDs)
    data['drivers_df'] = load_csv_file('drivers.csv')
    data['constructors_df'] = load_csv_file('constructors.csv')
    data['circuits_df'] = load_csv_file('circuits.csv')
    data['status_df'] = load_csv_file('status.csv') # Useful for understanding DNF, finished, etc.

    # Optional but often present and useful:
    data['qualifying_df'] = load_csv_file('qualifying.csv')
    data['driver_standings_df'] = load_csv_file('driver_standings.csv')
    data['constructor_standings_df'] = load_csv_file('constructor_standings.csv')
    data['seasons_df'] = load_csv_file('seasons.csv')

    print("--- Data Ingestion Complete ---")
    return data

def main():
    # Call the ingestion function
    f1_raw_data = ingest_f1_data()

    # You can now access your DataFrames like:
    # races_df = f1_raw_data['races_df']
    # lap_times_df = f1_raw_data['lap_times_df']
    # ... and so on

    # Example: Print head of one DataFrame to verify
    if 'races_df' in f1_raw_data and f1_raw_data['races_df'] is not None:
        print("\n--- Sample from 'races_df' ---")
        print(f1_raw_data['races_df'].head())
    
    if 'lap_times_df' in f1_raw_data and f1_raw_data['lap_times_df'] is not None:
        print("\n--- Sample from 'lap_times_df' ---")
        print(f1_raw_data['lap_times_df'].head())
    
    # You won't save new CSVs in this script since you're just loading them.
    # The cleaned/processed data will be saved by `data_preprocessing.py`.

if __name__ == "__main__":
    main()