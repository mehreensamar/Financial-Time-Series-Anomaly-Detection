anomaly_detector.py
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

def detect_anomalies(df):
    iso = IsolationForest(contamination=0.01)
    df['anomaly'] = iso.fit_predict(df[['Close']])
    anomalies = df[df['anomaly'] == -1]
    
    plt.figure(figsize=(14, 6))
    plt.plot(df['Close'], label='Stock Price')
    plt.scatter(anomalies.index, anomalies['Close'], color='red', label='Anomalies')
    plt.legend()
    plt.title('Anomaly Detection with Isolation Forest')
    plt.show()
