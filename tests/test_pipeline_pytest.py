# tests/test_pipeline_pytest.py
from ml_pipeline import train_and_score_model
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


def test_train_and_score_model_runs():
    X, y = fetch_california_housing(return_X_y=True, as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=201
    )
    n_estimators, score = train_and_score_model(
        X_train, X_test, y_train, y_test, n_estimators=10
    )

    assert n_estimators == 10
    assert score >= 0

