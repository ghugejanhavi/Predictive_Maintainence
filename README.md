# Air Temperature Prediction of Machine at failure

This model predicts the air temperature of a machine at failure.
It is trained using linear regression on the AI4I 2020 Predictive Maintenance Dataset from the UCI Machine Learning Repository.
Refer the Predictive_Maintainence_data.ipynb notebook for EDA performed on the dataset.

## Python Libraries Used
- scikit-learn
- streamlit
- pandas
- pickle
- pandas_profiling
- plotly.express
- statsmodels

## Usage
For live demo:
[python3 app.py](https://janhavighuge-predictive-maintainence.onrender.com/)https://janhavighuge-predictive-maintainence.onrender.com/

Side bar panel select Predict
  Required input parameters 
  - Process Temperature in K
  - Rotational speed of the machine in rpm
  - Heat Dissipation Failure (Failure = 1)
Side bar panel select Explore
  To see simple analysis of the dataset

## Screen Recording
![predictive_maintainence](https://github.com/ghugejanhavi/Predictive_Maintainence/assets/72988080/d3aa354a-5137-468e-8969-5b5df07ef888)



