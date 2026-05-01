# Iris Flower Machine Learning Classifier

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Logistic%20Regression-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Task](https://img.shields.io/badge/Task-Multiclass%20Classification-2E8B57?style=flat-square)

## Project Summary

A beginner-friendly Machine Learning project that trains a Logistic Regression model to classify Iris flowers from four numeric measurements.

## Dataset

The Iris dataset contains three species:

- Setosa
- Versicolor
- Virginica

| Feature | Description |
|---|---|
| Sepal length | Numeric flower measurement |
| Sepal width | Numeric flower measurement |
| Petal length | Numeric flower measurement |
| Petal width | Numeric flower measurement |

## Features

- Loads the built-in Iris dataset from scikit-learn
- Splits data into training and test sets
- Builds a preprocessing and model pipeline
- Trains a Logistic Regression classifier
- Prints accuracy and classification report
- Saves the trained model as `iris_model.joblib`
- Includes a separate prediction script

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming |
| pandas | Data handling |
| scikit-learn | Dataset, pipeline, model, metrics |
| joblib | Model saving and loading |

## Folder Structure

```text
03_ML_Iris_Classifier/
|-- train_model.py
|-- predict.py
|-- requirements.txt
`-- README.md
```

## How To Install

```bash
pip install -r requirements.txt
```

## How To Train

```bash
python train_model.py
```

This creates:

```text
iris_model.joblib
```

## How To Predict

```bash
python predict.py
```

## Example Prediction

The prediction script uses this sample:

```text
sepal length = 5.1
sepal width  = 3.5
petal length = 1.4
petal width  = 0.2
```

Expected output:

```text
Predicted species: setosa
```

## Future Improvements

- Try Random Forest and SVM
- Add confusion matrix plot
- Create a Streamlit web app
- Add user input for custom flower measurements
- Add a Jupyter notebook version

