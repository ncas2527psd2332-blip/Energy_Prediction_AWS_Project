# Import Libraries

import pickle
import pandas as pd



# Step 1: Load the saved model

with open("../03_model/energy_model.pkl", "rb") as file:
    model = pickle.load(file)


print("Energy Prediction Model Loaded Successfully")



# Step 2: Get Input From User

temperature = float(input("Enter Temperature: "))

humidity = float(input("Enter Humidity: "))

occupancy = int(input("Enter Occupancy: "))

previous_usage = float(input("Enter Previous Usage: "))



# Step 3: Create Input DataFrame

new_data = pd.DataFrame(
    [
        [
            temperature,
            humidity,
            occupancy,
            previous_usage
        ]
    ],
    columns=[
        "Temperature",
        "Humidity",
        "Occupancy",
        "Previous_Usage"
    ]
)



# Step 4: Predict Energy Consumption

prediction = model.predict(new_data)



# Step 5: Display Prediction Result

print("\nPredicted Energy Consumption:")
print(round(prediction[0], 2), "kWh")



# Step 6: Save Prediction Result

result = pd.DataFrame(
    {
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Occupancy": [occupancy],
        "Previous_Usage": [previous_usage],
        "Predicted_Energy": [round(prediction[0], 2)]
    }
)



# Save result into 04_output folder

result.to_csv(
    "../04_output/prediction_result.csv",
    index=False
)



print("\nPrediction result saved successfully")