from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

def create_lstm_model(X_train, y_train, X_val, y_val):
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20, batch_size=16)
    return model
