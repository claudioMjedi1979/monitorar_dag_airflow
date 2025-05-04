
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("modelo_dag_falha_novo.pkl")


st.title("Previsão de Falhas em DAGs do Airflow")

uploaded_file = st.file_uploader("Envie um CSV com dados das DAGs", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    data_encoded = pd.get_dummies(data, columns=["dag_id"], drop_first=True)

    for col in model.feature_names_in_:
        if col not in data_encoded.columns:
            data_encoded[col] = 0
    data_encoded = data_encoded[model.feature_names_in_]

    previsoes = model.predict(data_encoded)
    data["risco_falha"] = ["ALTO" if p == 1 else "BAIXO" for p in previsoes]
    st.dataframe(data)
