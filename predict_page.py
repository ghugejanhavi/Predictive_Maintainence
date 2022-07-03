import streamlit as st
import pickle



def load_model():
    with open("linear_model.pkl","rb") as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
scaler = data["scaler_tranform"]


def show_predict_page():
    st.title("Air Temperature Prediction of Machine at failure")
    st.write("""#### This model is trained on Predictive Maintenance dataset of a machine, which predicts the Air temperature when machine failure occurs""")

    Process_temperature_K = st.number_input(label="Process Temperature")
    Rotational_speed_rpm = st.number_input(label="Rotational speed in rpm of the machine ")
    HDF = st.number_input(label="Heat Dissipation Failure", min_value=0, max_value=1, step=1)

    ok = st.button("Calculate Air Temperature")
    if ok:
        input_given = [[Process_temperature_K, Rotational_speed_rpm, HDF]]
        test1 = scaler.transform(input_given)

        y = regressor.predict(test1)

        st.subheader(f"The predicted Air Temperature is {y[0]:.2f} K")

