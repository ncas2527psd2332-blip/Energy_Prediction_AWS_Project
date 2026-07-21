import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load Dataset

df = pd.read_csv("../01_dataset/energy_data.csv")

print("Dataset Loaded Successfully")


# -----------------------------
# Graph 1: Occupancy vs Energy Consumption
# -----------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["Occupancy"],
    df["Energy_Consumption"]
)

plt.xlabel("Occupancy")
plt.ylabel("Energy Consumption")
plt.title("Occupancy vs Energy Consumption")
plt.grid(True)

# Save Graph
plt.savefig("../04_output/occupancy_energy.png")

plt.show()


# -----------------------------
# Graph 2: Temperature vs Energy Consumption
# -----------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["Temperature"],
    df["Energy_Consumption"]
)

plt.xlabel("Temperature")
plt.ylabel("Energy Consumption")
plt.title("Temperature vs Energy Consumption")
plt.grid(True)

# Save Graph
plt.savefig("../04_output/temperature_energy.png")

plt.show()


# -----------------------------
# Graph 3: Actual vs Predicted
# -----------------------------

with open("../03_model/energy_model.pkl", "rb") as file:
    model = pickle.load(file)

X = df[
    [
        "Temperature",
        "Humidity",
        "Occupancy",
        "Previous_Usage"
    ]
]

actual = df["Energy_Consumption"]

predicted = model.predict(X)

plt.figure(figsize=(6,4))

plt.plot(
    actual.values,
    marker='o',
    label="Actual"
)

plt.plot(
    predicted,
    marker='s',
    label="Predicted"
)

plt.xlabel("Data Samples")
plt.ylabel("Energy Consumption")
plt.title("Actual vs Predicted Energy Consumption")
plt.legend()
plt.grid(True)

# Save Graph
plt.savefig("../04_output/actual_vs_predicted.png")

plt.show()


# -----------------------------
# Graph 4: Correlation Heatmap
# -----------------------------

correlation = df.corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation Heatmap")

# Save Graph
plt.savefig("../04_output/correlation_heatmap.png")

plt.show()

print("\nAll graphs saved successfully!")