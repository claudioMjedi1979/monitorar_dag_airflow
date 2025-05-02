
# DAG Failure Predictor

A simple machine learning project to **predict whether a DAG (Directed Acyclic Graph) is likely to fail**, using simulated metadata from Airflow.  
Ideal for data engineering teams looking to anticipate pipeline issues before they happen.

## 🔍 What it does

- Accepts input data like: `dag_id`, `execution_time`, `recent_failures`, and `execution_hour`
- Uses a trained `RandomForest` model to predict risk of failure
- Displays the prediction in a clean Streamlit web app

## Project Structure

```
.
├── app.py                      # Streamlit app for uploading CSV and visualizing predictions
├── modelo_dag_falha.pkl       # Trained model using Scikit-learn
├── dags_simuladas.csv         # Simulated DAG history data
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation
```

## How to Run

1. Clone this repository:
```bash
git clone https://github.com/seu-usuario/dag-failure-predictor.git
cd dag-failure-predictor
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

5. Upload the sample CSV (`dags_simuladas.csv`) or your own DAG metadata file.

## How to Extend

You can replace the CSV input with:
- A database query (`pandas.read_sql()` from PostgreSQL or MySQL)
- A REST API (FastAPI or Flask)
- A real-time stream (Kafka, RabbitMQ)
- Integration with Airflow as a pre-check DAG

## Tech Stack

- Python
- Scikit-learn
- Pandas
- Streamlit
- Joblib

## 📄 License

MIT License

---

Made with 💡 by Claudio
