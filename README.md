# 🏎 **Predictive Tyre Strategy Analysis for Formula 1 & Sim Racers**

*A data-driven project built for the motorsport community—empowering sim racers, engineers, and F1 fans with actionable tyre insights derived from real Formula 1 data (sourced from Kaggle). The project leverages Python for preprocessing and Power BI for advanced race visualizations.*

---

### **Project Objective**

To optimize **tyre strategy decisions** by analyzing real-world F1 telemetry, pit data, and stint evolution. This project uncovers how tyre compounds behave over race stints, how lap times evolve, and when pit stops make strategic sense.
**Target Users**: Sim racing strategists, race engineers, motorsport analysts, and fans.

---

### **Datasets Used**

| Dataset                        | Description                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `lap_times_processed.csv`      | Cleaned lap-by-lap data enriched with compound type and pit indicators              |
| `tyre_degradation_summary.csv` | Driver stint summaries including degradation rates, fastest laps, and stint lengths |

---

Here’s the updated **section to add to your `README.md`** file, showing the execution order and purpose of each script:

---

## Script Execution Order

The following scripts should be run in order:

1. **`data_ingestion.py`**
   → Ingests raw data csvs from Kaggle dataset.
   **Output:** `data/raw_kaggle/`

2. **`data_preprocessing.py`**
   →  Cleans the raw data and performs feature engineering (lap time data, extracting tyre compound info, pit indicators, and stint details).
   **Outputs:**

   * `lap_times_processed.csv`: Cleaned lap-by-lap dataset
   * `tyre_degradation_summary.csv`: Summary of tyre degradation across stints

3. **`average_lap_data_processing.py`**
   →  Aggregates the cleaned data to compute lap counts and average lap time per tyre compound stint (per driver and race)
   **Output:** `average_laptime_compoundwise.csv` (for Power BI visuals)

---

### **Tech Stack & Tools**

* **Python**: `pandas` (data manipulation), `numpy` (numerical operations), `os` (file path handling)
* **IDE/Platform**: Visual Studio Code
* **Data Visualizations**: Power BI
* **Data Handling**: CSV files
* **Data Source**: [Kaggle Formula 1 Dataset (1950–2020)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)

<img width="2364" height="1356" alt="TyreStratDash-1" src="https://github.com/user-attachments/assets/1c42b345-04cb-4075-b2d8-2a724e6db288" />




