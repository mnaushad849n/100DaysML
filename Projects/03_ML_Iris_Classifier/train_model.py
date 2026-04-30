import joblib
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


MODEL_FILE = "iris_model.joblib"
RANDOM_STATE = 42


def load_data():
    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target
    return X, y, iris.target_names


def build_model():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])


def main():
    X, y, target_names = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    model = build_model()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions, target_names=target_names))

    joblib.dump({
        "model": model,
        "target_names": target_names,
        "feature_names": list(X.columns),
    }, MODEL_FILE)

    print(f"Model saved to {MODEL_FILE}")


if __name__ == "__main__":
    main()

