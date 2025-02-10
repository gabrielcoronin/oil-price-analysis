import logging
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

def load_lstm_model(model_path, scaler_path):
    try:
        model = load_model(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except Exception as e:
        raise Exception(f"Error loading model or scaler: {e}")

def load_and_preprocess_data(url, cutoff_date):
    try:
        tables = pd.read_html(url, decimal=',', thousands='.')
        df = tables[2].drop(index=0).reset_index(drop=True)
        df.columns = ['date', 'price']
        df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df.sort_values(by='date', inplace=True)
        df.set_index('date', inplace=True)
        df = df[df.index > cutoff_date].dropna(subset=['price']).reset_index()
        df = create_features(df)
        df = remove_high_correlation(df)
        logging.info(f"Data loaded with {df.shape[0]} records and {df.shape[1]} features.")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

def create_features(df):
    df['SMA_3'] = df['price'].rolling(window=3).mean()
    df['SMA_6'] = df['price'].rolling(window=6).mean()  
    df['SMA_12'] = df['price'].rolling(window=12).mean() 
    df['pct_change'] = df['price'].pct_change()
    df['lag_1'] = df['price'].shift(1)
    df['lag_3'] = df['price'].shift(3)
    df['lag_6'] = df['price'].shift(6)
    df.dropna(inplace=True)
    return df

def remove_high_correlation(df, threshold=0.9):
    correlation_matrix = df.corr()
    upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))
    drop_cols = [column for column in upper_triangle.columns if any(upper_triangle[column] > threshold)]
    df = df.drop(columns=drop_cols)
    logging.info(f"Removed {len(drop_cols)} highly correlated features: {drop_cols}")
    return df

def scale_data(df):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df.drop(columns=['date']))
    return scaled_data, scaler

def predict(num_prediction, data_scaled, sequence_length):
    try:
        model_lstm, scaler = load_lstm_model('models/LSTMModel.keras', 'models/scaler.joblib')
        if model_lstm is None or scaler is None:
            logging.error("Error loading model or scaler.")
            return None

        if len(data_scaled) < sequence_length:
            raise ValueError("The length of the scaled data is smaller than the sequence length.")

        prediction_list = list(data_scaled[-sequence_length:])
        logging.info(f"Initial prediction list size: {len(prediction_list)}")

        num_features = data_scaled.shape[1]
        logging.info(f"Scaled data: {data_scaled}")

        for _ in range(num_prediction):
            x = np.array(prediction_list[-sequence_length:]).reshape((1, sequence_length, num_features))

            predicted_price = model_lstm.predict(x)[0][0]
            logging.info(f"Generated prediction: {predicted_price}")

            next_input = np.array([predicted_price, prediction_list[-1][1]])
            prediction_list.append(next_input)

        prediction_list = prediction_list[-num_prediction:]
        logging.info(f"Prediction list size after adding new predictions: {len(prediction_list)}")

        prediction_list = np.array(prediction_list).reshape(-1, 2)  
        prediction_list = scaler.inverse_transform(prediction_list)
        logging.info(f"Inverse transformed predictions: {prediction_list}")

        return prediction_list[:, 0]

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return None
