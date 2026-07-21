# Import libraries

# Import Libraries

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# Step 1: Load Dataset

df = pd.read_csv("../01_dataset/energy_data.csv")


print("----- Dataset -----")
print(df)



# Step 2: Select Input Features (X)

X = df[
    [
        'Temperature',
        'Humidity',
        'Occupancy',
        'Previous_Usage'
    ]
]



# Step 3: Select Target Output (Y)

Y = df['Energy_Consumption']



# Step 4: Split Data into Training and Testing

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)



# Step 5: Create Linear Regression Model

model = LinearRegression()



# Step 6: Train the Model

model.fit(
    X_train,
    Y_train
)


print("\nModel Training Completed")



# Step 7: Save the Trained Model

with open("../03_model/energy_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model saved successfully")



# Step 8: Predict Energy Consumption

prediction = model.predict(X_test)


print("\nPredicted Values:")
print(prediction)



# Step 9: Evaluate Model Performance

mae = mean_absolute_error(
    Y_test,
    prediction
)


print("\nMean Absolute Error:")
print(mae)



# Step 10: Calculate R2 Score

r2 = r2_score(
    Y_test,
    prediction
)


print("\nR2 Score:")
print(r2)