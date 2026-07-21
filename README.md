Energy Consumption Prediction using Machine Learning
1. Project Overview

Explain what your project does.

Example:

## Project Overview

Energy consumption prediction is a machine learning project that predicts
future energy usage based on environmental and usage-related factors.

The system uses parameters such as:
- Temperature
- Humidity
- Occupancy
- Previous Energy Usage

Machine learning models are trained to predict energy consumption in kWh.
2. Problem Statement

Explain the problem you are solving.

## Problem Statement

Increasing energy demand requires efficient energy management.
Traditional methods cannot accurately predict future energy consumption.

This project develops a machine learning-based prediction system
to estimate energy consumption and support better energy planning.
3. Objectives
## Objectives

- Analyze energy consumption patterns
- Preprocess energy dataset
- Train machine learning regression models
- Compare different ML algorithms
- Predict future energy consumption
- Visualize important relationships in data
4. Technologies Used

Mention your tools:

## Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

### Development Environment
- VS Code

### Version Control
- Git
- GitHub
5. Dataset Description

Explain your dataset.

## Dataset Description

The dataset contains information related to energy consumption.

Features:

| Feature | Description |
|---|---|
| Temperature | Environmental temperature |
| Humidity | Moisture level |
| Occupancy | Number of people present |
| Previous_Usage | Previous energy consumption |
| Energy_Consumption | Target value |
6. Machine Learning Models Used
## Machine Learning Models

The following regression algorithms were implemented:

1. Linear Regression
2. Decision Tree Regression
3. Random Forest Regression
7. Project Structure

Show your folders:

## Project Structure

Energy_Prediction_AWS_Project/

│
├── 01_dataset/
│   └── energy_data.csv
│
├── 02_code/
│   ├── 01_data_analysis.py
│   ├── 02_model_training.py
│   ├── 03_prediction.py
│   ├── 04_visualization.py
│   ├── 05_model_comparison.py
│   └── main.py
│
├── 03_model/
│   └── trained_model.pkl
│
├── 04_output/
│   └── generated graphs
│
└── requirements.txt
8. Model Performance

Add your results:

## Model Performance

| Model | MAE | R2 Score |
|---|---|---|
| Linear Regression | 0.586 | 0.846 |
| Decision Tree | 0.5 | 0.777 |
| Random Forest | 0.98 | 0.457 |

Linear Regression achieved the best performance.
9. How to Run the Project

Very important:

## How to Run

### Step 1: Clone Repository

git clone https://github.com/ncas2527psd2332-blip/Energy_Prediction_AWS_Project.git


### Step 2: Install Requirements

pip install -r requirements.txt


### Step 3: Run Project

python 02_code/main.py
10. Sample Prediction
## Sample Prediction

Input:

Temperature: 32°C  
Humidity: 65%  
Occupancy: 12  
Previous Usage: 6 kWh


Output:

Predicted Energy Consumption:
7.62 kWh
11. Future Improvements
## Future Improvements

- Deploy model using AWS services
- Create a web dashboard
- Use real-time IoT sensor data
- Implement deep learning models
12. Author
## Author

Yuvashree  
MSc Computer Science

After creating README.md, your GitHub workflow will be:

git add README.md

git commit -m "Added project documentation"

git push
