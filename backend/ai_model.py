import tensorflow as tf
import pandas as pd
import numpy as np

def predict_traffic(day_value, hour_value):
    data = pd.read_csv("density_data.csv")

    model = tf.keras.models.load_model('bi_lstm_model')

    unique_combinations = data[['lat_bin', 'lon_bin']].drop_duplicates()

    day_of_week = (day_value - 1) % 7
    is_weekend = 1 if day_value in [13, 14, 20, 21] else 0

    unique_combinations['hour'] = hour_value
    unique_combinations['day'] = day_value
    unique_combinations['day_of_week'] = day_of_week
    unique_combinations['is_weekend'] = is_weekend

    # Transform hours into radians
    unique_combinations['hour_rad'] = unique_combinations['hour'] * (2 * np.pi / 24)
    unique_combinations['hour_sin'] = np.sin(unique_combinations['hour_rad'])
    unique_combinations['hour_cos'] = np.cos(unique_combinations['hour_rad'])

    unique_combinations['day_rad'] = unique_combinations['day_of_week'] * (2 * np.pi / 7)
    unique_combinations['day_sin'] = np.sin(unique_combinations['day_rad'])
    unique_combinations['day_cos'] = np.cos(unique_combinations['day_rad'])

    unique_combinations = unique_combinations.drop(['day_rad', 'hour_rad'], axis=1)

    X_test_day_of_week = unique_combinations[['day_of_week']].values
    X_test_hour = unique_combinations[['hour']].values
    X_test_day = unique_combinations[['day']].values
    X_test_numerical = unique_combinations.drop(['day_of_week', 'hour', 'day'], axis=1)

    model_predictions = model.predict([X_test_day, X_test_hour, X_test_day_of_week, X_test_numerical])

    visualize_predictions_df = unique_combinations.copy()
    visualize_predictions_df['count'] = model_predictions.flatten()

    return visualize_predictions_df