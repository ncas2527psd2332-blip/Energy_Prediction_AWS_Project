import os

print("========== ENERGY PREDICTION PROJECT ==========")


print("\n1. Running Data Analysis...")
os.system("python 01_data_analysis.py")


print("\n2. Running Model Training...")
os.system("python 02_model_training.py")


print("\n3. Running Prediction System...")
os.system("python 03_prediction.py")


print("\n4. Generating Visualizations...")
os.system("python 04_visualization.py")


print("\n5. Comparing ML Models...")
os.system("python 05_model_comparison.py")


print("\n========== PROJECT EXECUTION COMPLETED ==========")