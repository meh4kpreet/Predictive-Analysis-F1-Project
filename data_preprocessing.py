import pandas as pd
import numpy as np
import os

RAW_DIR = 'data/raw_kaggle'
PROCESSED_DIR = 'data/processed'

def parse_pit_duration(duration):
    try:
        # If duration looks like a float (e.g., 22.5), treat it as seconds
        return pd.to_timedelta(float(duration), unit='s')
    except:
        try:
            # If it's in hh:mm:ss or mm:ss, convert as string
            return pd.to_timedelta(duration)
        except:
            return pd.NaT

def clean_and_process():
    # Load CSVs
    lap_times = pd.read_csv(os.path.join(RAW_DIR, 'lap_times.csv'))
    pit_stops = pd.read_csv(os.path.join(RAW_DIR, 'pit_stops.csv'))
    results = pd.read_csv(os.path.join(RAW_DIR, 'results.csv'))

    # --- Clean Lap Times ---
    lap_times.dropna(inplace=True)
    lap_times['milliseconds'] = pd.to_numeric(lap_times['milliseconds'], errors='coerce')
    lap_times['lap_time_seconds'] = lap_times['milliseconds'] / 1000
    lap_times.drop_duplicates(inplace=True)

    # --- Clean Pit Stops ---
    pit_stops['pit_duration'] = pit_stops['duration'].apply(parse_pit_duration)
    pit_stops.dropna(subset=['pit_duration'], inplace=True)

    # --- Clean Results ---
    results['fastestLapTime'] = pd.to_timedelta(results['fastestLapTime'], errors='coerce')
    results['positionOrder'] = pd.to_numeric(results['positionOrder'], errors='coerce')

    # --- Merge ---
    merged = lap_times.merge(results, on=['raceId', 'driverId'], how='left')
    merged = merged.merge(
        pit_stops[['raceId', 'driverId', 'stop', 'lap', 'pit_duration']],
        on=['raceId', 'driverId', 'lap'],
        how='left'
    )

    # --- Feature Engineering ---
    merged['tyre_age'] = merged.groupby(['raceId', 'driverId'])['lap'].diff().fillna(0).astype(int)
    merged['is_pit'] = merged['pit_duration'].notnull().astype(int)
    merged['relative_lap_time'] = merged.groupby('raceId')['lap_time_seconds'].transform(lambda x: x - x.min())

    # Assign tyre compound based on lap number (dummy logic, replace with real logic if available)
    def assign_compound(lap):
        if lap < 10:
            return 'SOFT'
        elif lap < 25:
            return 'MEDIUM'
        else:
            return 'HARD'
    merged['tyre_compound'] = merged['lap'].apply(assign_compound)

    # --- Degradation Summary ---
    degradation_df = (
        merged.groupby(['raceId', 'driverId', 'tyre_compound'])
        .agg(
            avg_lap_time=('lap_time_seconds', 'mean'),
            fastest_lap=('lap_time_seconds', 'min'),
            lap_std=('lap_time_seconds', 'std'),
            total_laps=('lap', 'count')
        )
        .reset_index()
    )
    degradation_df['degradation_per_lap'] = degradation_df['avg_lap_time'] - degradation_df['fastest_lap']

    # Save Processed
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    merged.to_csv(os.path.join(PROCESSED_DIR, 'lap_times_processed.csv'), index=False)
    degradation_df.to_csv(os.path.join(PROCESSED_DIR, 'tyre_degradation_summary.csv'), index=False)
    print("✅ Data preprocessing complete and saved.")

def main():
    clean_and_process()

if __name__ == '__main__':
    main()
