import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("ai4i2020.csv")
df.columns = [i.replace("[","_").replace("]","").replace(" ","_").replace("__","_") for i in df.columns]

x = df[["Process_temperature_K","Rotational_speed_rpm","HDF"]]
y = df["Air_temperature_K"]

scaler = StandardScaler()
arr = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(arr, y, test_size = 0.15, random_state =100)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

info = {"model":regressor, "scaler_tranform":scaler}
with open("linear_model.pkl","wb") as file:
    pickle.dump(info, file)