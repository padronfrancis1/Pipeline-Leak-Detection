import pandas as pd
import numpy as np

# Define oil-specific pressure ranges and scenarios
n_samples = 1000  # Total number of samples to generate
oil_pressure_levels = [30, 40, 50, 60]  # Higher pressure ranges for oil pipelines
leak_sizes = [0, 0.5, 0.7, 1.0]  # Leak sizes in mm
oil_medium = "Oil"

np.random.seed(42)
oil_data = []

for pressure in oil_pressure_levels:
    for leak_size in leak_sizes:
        condition = "Normal" if leak_size == 0 else "Leak"
        for _ in range(n_samples // (len(oil_pressure_levels) * len(leak_sizes))):
            # Time-domain features (with adjustments for oil properties)
            p1 = np.random.normal(loc=0.6 if condition == "Normal" else 1.2, scale=0.1)  # Mean Frequency
            p2 = np.random.normal(loc=0.25 if condition == "Normal" else 0.6, scale=0.05)  # Variance
            p3 = np.random.normal(loc=0.12 if condition == "Normal" else 0.35, scale=0.02)  # Skewness
            p4 = np.random.normal(loc=3.2 if condition == "Normal" else 4.8, scale=0.3)  # Spectral Kurtosis
            p5 = np.random.normal(loc=140 if condition == "Normal" else 170, scale=10)  # Centroid Frequency
            p6 = np.random.normal(loc=25 if condition == "Normal" else 45, scale=5)  # Std Dev of Centroid Frequency
            p7 = np.random.normal(loc=0.7 if condition == "Normal" else 1.4, scale=0.1)  # RMS Frequency
            p8 = np.random.normal(loc=2.2 if condition == "Normal" else 3.7, scale=0.2)  # Fourth Moment of Frequency
            p9 = np.random.normal(loc=1.6 if condition == "Normal" else 2.1, scale=0.1)  # Flattening Factor
            p10 = np.random.normal(loc=0.06 if condition == "Normal" else 0.12, scale=0.01)  # Coefficient of Variation
            p11 = np.random.normal(loc=0.18 if condition == "Normal" else 0.4, scale=0.05)  # Skewness of Centroid Frequency
            p12 = np.random.normal(loc=3.2 if condition == "Normal" else 5.2, scale=0.4)  # Kurtosis of Centroid Frequency
            p13 = np.random.normal(loc=0.9 if condition == "Normal" else 1.6, scale=0.1)  # Square Root of Centroid Frequency
            p14 = np.random.normal(loc=0.5 if condition == "Normal" else 0.9, scale=0.05)  # RMS Centroid Frequency Deviation
            
            # Append to dataset
            oil_data.append([pressure, oil_medium, leak_size, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, condition])

# Create DataFrame
columns = [
    "Pressure (bar)", "Medium", "Leak Size (mm)", 
    "P1: Mean Frequency", "P2: Variance", "P3: Skewness", "P4: Spectral Kurtosis",
    "P5: Centroid Frequency", "P6: Std Dev Centroid Frequency", 
    "P7: RMS Frequency", "P8: Fourth Moment of Frequency", "P9: Flattening Factor",
    "P10: Coefficient of Variation", "P11: Skewness of Centroid Frequency", 
    "P12: Kurtosis of Centroid Frequency", "P13: Square Root Centroid Frequency", 
    "P14: RMS Centroid Frequency Deviation", "Condition"
]
oil_dataset = pd.DataFrame(oil_data, columns=columns)

# Save to CSV
oil_dataset.to_csv("Synthetic_Oil_Leak_Dataset.csv", index=False)
print("Synthetic oil dataset saved as 'Synthetic_Oil_Leak_Dataset.csv'")
