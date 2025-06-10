import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load_cicids2017_features():
    # Load dataset from CSV with special characters in filename
    filename = "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX (1).csv"
    df = pd.read_csv(filename)

    # Drop rows with missing or infinite values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    # Select important numeric features
    selected_features = [
        'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
        'Total Length of Fwd Packets', 'Total Length of Bwd Packets',
        'Fwd Packet Length Mean', 'Bwd Packet Length Mean',
        'Flow IAT Mean', 'Flow IAT Std',
        'Fwd IAT Mean', 'Fwd IAT Std',
        'Bwd IAT Mean', 'Bwd IAT Std',
        'Fwd PSH Flags', 'Bwd PSH Flags',
        'Fwd URG Flags', 'Bwd URG Flags',
        'FIN Flag Count', 'SYN Flag Count', 'RST Flag Count',
        'ACK Flag Count', 'URG Flag Count'
    ]

    # Filter the columns
    X = df[selected_features].astype(float)

    # Encode the labels
    le = LabelEncoder()
    y = le.fit_transform(df['Label'])  # e.g., Benign → 0, Web Attack → 1, etc.

    return X.values, y, le.classes_
