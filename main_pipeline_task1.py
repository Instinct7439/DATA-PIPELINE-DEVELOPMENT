import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. DATA GENERATION (The Source)
def generate_sensor_data(rows=100):
    np.random.seed(42)
    data = {
        'Timestamp': [datetime.now() - timedelta(minutes=i) for i in range(rows)],
        'Temperature': np.random.uniform(15, 35, rows),
        'Humidity': np.random.uniform(30, 90, rows),
        'CO2_Levels': np.random.uniform(300, 1000, rows)
    }
    df = pd.DataFrame(data)
    
    # Manually inject some "Error Data" to test our validation gate
    df.loc[5, 'Temperature'] = 500  # Impossible heat
    df.loc[10, 'Humidity'] = -10    # Impossible humidity
    return df

# 2. VALIDATION GATE (The "Professional" Touch)
def validate_data(df):
    print("🔍 Starting Data Validation...")
    
    # Define "Normal" Ranges
    valid_temp = (df['Temperature'] >= -10) & (df['Temperature'] <= 60)
    valid_hum = (df['Humidity'] >= 0) & (df['Humidity'] <= 100)
    
    # Separate Clean data from Errors
    clean_df = df[valid_temp & valid_hum].copy()
    error_df = df[~(valid_temp & valid_hum)].copy()
    
    print(f"Clean records: {len(clean_df)}")
    print(f"Flagged errors: {len(error_df)}")
    
    return clean_df, error_df

# 3. TRANSFORMATION (Feature Engineering)
def transform_data(df):
    # Add a 'Status' column based on CO2 levels
    df['Air_Quality'] = np.where(df['CO2_Levels'] > 800, 'Poor', 'Good')
    return df

# EXECUTE PIPELINE
if __name__ == "__main__":
    raw_data = generate_sensor_data()
    clean_data, errors = validate_data(raw_data)
    
    final_data = transform_data(clean_data)
    
    # Save results
    final_data.to_csv('cleaned_air_quality.csv', index=False)
    if not errors.empty:
        errors.to_csv('sensor_errors_log.csv', index=False)
        print("Errors logged to 'sensor_errors_log.csv'")
    
    print("Pipeline Execution Complete!")



import matplotlib.pyplot as plt
import json

def generate_report(df):
    # Create a summary of the cleaned data
    summary = {
        "total_records": len(df),
        "avg_temp": round(df['Temperature'].mean(), 2),
        "avg_humidity": round(df['Humidity'].mean(), 2),
        "avg_co2": round(df['CO2_Levels'].mean(), 2),
        "high_co2_alerts": len(df[df['Air_Quality'] == 'Poor'])
    }
    
    with open('pipeline_summary.json', 'w') as f:
        json.dump(summary, f, indent=4)
    print("📊 Summary report saved to 'pipeline_summary.json'")

def plot_trends(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['Temperature'], label='Temp (°C)', color='orange')
    plt.plot(df['Timestamp'], df['CO2_Levels']/20, label='CO2 (Scaled)', color='green') # Scaled for visibility
    plt.title("Environmental Sensor Trends")
    plt.xlabel("Time")
    plt.legend()
    plt.savefig('data_trends.png')
    print("📈 Trend graph saved as 'data_trends.png'")

# Add these calls to your 'if __name__ == "__main__":' block
if __name__ == "__main__":
    # ... (existing code)
    generate_report(final_data)
    plot_trends(final_data)