import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def train_and_score_model(train_set, test_set, train_labels, test_labels, n_estimators):
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=201)
    model.fit(train_set, train_labels)
    y_pred = model.predict(test_set)
    score = mean_squared_error(test_labels, y_pred)
    print(f"n_estimators={n_estimators}, mse={score:.4f}")
    return n_estimators, score


def main():
    # load data
    X, y = fetch_california_housing(return_X_y=True, as_frame=True)
    # simple train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=201
    )
    train_and_score_model(X_train, X_test, y_train, y_test, n_estimators=50)


if __name__ == "__main__":
    main()
