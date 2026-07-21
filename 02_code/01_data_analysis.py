# Import pandas library
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("../01_dataset/energy_data.csv")


# Step 2: Display the complete dataset
print("----- Energy Consumption Dataset -----")
print(df)


# Step 3: Display first 5 rows of the dataset
print("\n----- First 5 Rows -----")
print(df.head())


# Step 4: Check dataset information
print("\n----- Dataset Information -----")
df.info()


# Step 5: Check missing values
print("\n----- Missing Values -----")
print(df.isnull().sum())


# Step 6: Display statistical details
print("\n----- Statistical Summary -----")
print(df.describe())
import matplotlib.pyplot as plt

# Display first few rows
print(df.head())

# Plot energy consumption
plt.figure(figsize=(8,5))
plt.plot(df["Energy_Consumption"])
plt.xlabel("Data Records")
plt.ylabel("Energy_Consumption")
plt.title("Energy Consumption Pattern")
plt.show()
# Separating features and target

X = df.drop("Energy_Consumption", axis=1)

y = df["Energy_Consumption"]

print("Input Features:")
print(X)

print("\nTarget Values:")
print(y)
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)