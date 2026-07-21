# Energy Consumption Prediction using Machine Learning

## Project Overview

Energy Consumption Prediction is a machine learning project that predicts energy consumption based on environmental and usage-related factors.

The system uses machine learning regression algorithms to estimate energy consumption in kWh based on:

- Temperature
- Humidity
- Occupancy
- Previous Energy Usage

This project helps in understanding energy usage patterns and supports efficient energy management.

---

## Problem Statement

Increasing energy demand requires better energy management and accurate energy forecasting.

This project develops a machine learning-based prediction system that can estimate future energy consumption using historical and environmental data.

---

## Objectives

- Analyze energy consumption data
- Perform data preprocessing and exploration
- Train machine learning regression models
- Compare different ML algorithms
- Predict future energy consumption
- Visualize energy consumption patterns

---

## Technologies Used

### Programming Language

- Python

### Python Libraries

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## Dataset Description

The dataset contains information related to energy consumption.

| Feature | Description |
|---|---|
| Temperature | Environmental temperature value |
| Humidity | Humidity percentage |
| Occupancy | Number of people using the space |
| Previous_Usage | Previous energy consumption value |
| Energy_Consumption | Target value to predict |

---

## Machine Learning Models Implemented

The following regression models were developed and compared:

1. Linear Regression
2. Decision Tree Regression
3. Random Forest Regression

---

## Project Structure
Energy_Prediction_AWS_Project

│
├── 01_dataset
│ └── energy_data.csv
│
├── 02_code
│ ├── 01_data_analysis.py
│ ├── 02_model_training.py
│ ├── 03_prediction.py
│ ├── 04_visualization.py
│ ├── 05_model_comparison.py
│ └── main.py
│
├── 03_model
│ ├── energy_model.pkl
│ └── best_energy_model.pkl
│
├── 04_output
│ ├── actual_vs_predicted.png
│ ├── correlation_heatmap.png
│ ├── occupancy_energy.png
│ ├── temperature_energy.png
│ ├── prediction_result.csv
│ └── model_performance.txt
│
└── requirements.txt


---

## Model Performance

| Model | Mean Absolute Error (MAE) | R2 Score |
|---|---|---|
| Linear Regression | 0.586 | 0.846 |
| Decision Tree Regression | 0.5 | 0.777 |
| Random Forest Regression | 0.98 | 0.457 |

### Best Performing Model

Linear Regression achieved the best performance with:

- MAE: 0.586
- R2 Score: 0.846

---

## Data Visualization

The project generates visualizations to understand relationships between features and energy consumption.

Generated graphs:

- Temperature vs Energy Consumption
- Occupancy vs Energy Consumption
- Correlation Heatmap
- Actual vs Predicted Energy Consumption

---

## How to Run the Project

### Step 1: Clone Repository


git clone https://github.com/ncas2527psd2332-blip/Energy_Prediction_AWS_Project.git


### Step 2: Install Required Libraries


pip install -r requirements.txt


### Step 3: Run the Project


python 02_code/main.py


---

## Sample Prediction

### Input


Temperature: 32
Humidity: 65
Occupancy: 12
Previous Usage: 6


### Output


Predicted Energy Consumption:
7.62 kWh


---

## Future Improvements

- Deploy the model using AWS cloud services
- Develop a web-based energy monitoring dashboard
- Integrate real-time IoT sensor data
- Implement advanced deep learning models
- Create real-time prediction APIs

---

## Author

**Yuvashree**

MSc Computer Science
