import pandas as pd

df_main = pd.read_csv("data/processed/lap_times_processed.csv")

# Group by raceId, driverId, tyre_compound and aggregate both lap count and average lap time
df_avg_lap = df_main.groupby(['raceId', 'driverId', 'tyre_compound'], as_index=False).agg({
    'lap': 'count',
    'lap_time_seconds': 'mean'
})

# Rename columns for clarity
df_avg_lap.rename(columns={'lap': 'lap_count', 'lap_time_seconds': 'avg_lap_time_seconds'}, inplace=True)

print(df_avg_lap.head(10))

df_avg_lap.to_csv("data/processed/average_laptime_compoundwise.csv",index=False)
