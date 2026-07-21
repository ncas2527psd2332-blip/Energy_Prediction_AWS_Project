# Import Libraries

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, r2_score



# Step 1: Load Dataset

df = pd.read_csv("../01_dataset/energy_data.csv")


print("Dataset Loaded Successfully")

print(df)



# Step 2: Select Input Features (X)

X = df[
    [
        "Temperature",
        "Humidity",
        "Occupancy",
        "Previous_Usage"
    ]
]



# Step 3: Select Target Output (Y)

Y = df["Energy_Consumption"]



# Step 4: Split Dataset into Training and Testing Data

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)



# Step 5: Create Machine Learning Models

linear_model = LinearRegression()


decision_tree_model = DecisionTreeRegressor(
    random_state=42
)


random_forest_model = RandomForestRegressor(
    random_state=42
)



# Step 6: Train Models

linear_model.fit(
    X_train,
    Y_train
)


decision_tree_model.fit(
    X_train,
    Y_train
)


random_forest_model.fit(
    X_train,
    Y_train
)


print("\nModel Training Completed")



# Step 7: Make Predictions

linear_prediction = linear_model.predict(X_test)


decision_tree_prediction = decision_tree_model.predict(X_test)


random_forest_prediction = random_forest_model.predict(X_test)



# Step 8: Compare Model Performance


model_names = [
    "Linear Regression",
    "Decision Tree Regression",
    "Random Forest Regression"
]


predictions = [
    linear_prediction,
    decision_tree_prediction,
    random_forest_prediction
]



for name, prediction in zip(model_names, predictions):

    print("\n-----------------------------")

    print(name)


    mae = mean_absolute_error(
        Y_test,
        prediction
    )


    r2 = r2_score(
        Y_test,
        prediction
    )


    print("Mean Absolute Error:", mae)

    print("R2 Score:", r2)



print("\nModel Comparison Completed")



# Step 9: Save Best Model

# Linear Regression gave the best R2 Score,
# so we save Linear Regression as the final model


with open(
    "../03_model/best_energy_model.pkl",
    "wb"
) as file:

    pickle.dump(
        linear_model,
        file
    )


print("\nBest Model Saved Successfully")