# tests/test_pipeline_unittest.py
import unittest
from pipeline import train_and_score_model
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


class TestPipeline(unittest.TestCase):
    def test_train_and_score_model_unittest(self):
        X, y = fetch_california_housing(return_X_y=True, as_frame=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=201
        )
        n_estimators, score = train_and_score_model(
            X_train, X_test, y_train, y_test, n_estimators=5
        )
        self.assertEqual(n_estimators, 5)
        self.assertGreaterEqual(score, 0.0)


if __name__ == "__main__":
    unittest.main()

