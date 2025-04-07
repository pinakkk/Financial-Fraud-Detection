import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """
    Detect anomalies in the transaction data using Isolation Forest.
    Assumes that numerical columns can be used for detection.
    Adds a new column 'is_anomaly' to the DataFrame.
    """
    # For this basic version, select numerical features only
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(num_cols) == 0:
        # No numerical features available, return original df
        df['is_anomaly'] = False
        return df
    
    # Fit Isolation Forest on the numerical features
    model = IsolationForest(contamination=0.05, random_state=42)
    try:
        preds = model.fit_predict(df[num_cols])
        # In IsolationForest, -1 indicates anomaly
        df['is_anomaly'] = [True if x == -1 else False for x in preds]
    except Exception as e:
        print(f"Error in anomaly detection: {e}")
        df['is_anomaly'] = False

    return df
