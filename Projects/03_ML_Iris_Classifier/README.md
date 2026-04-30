# Iris Flower Machine Learning Classifier

A beginner-friendly Machine Learning project that trains a model to classify Iris flowers.

## Project Overview

The Iris dataset contains flower measurements for three species:

- Setosa
- Versicolor
- Virginica

The goal is to predict the species from four numeric features:

- Sepal length
- Sepal width
- Petal length
- Petal width

## Features

- Loads the built-in Iris dataset from scikit-learn
- Splits data into training and test sets
- Builds a preprocessing and model pipeline
- Trains a Logistic Regression classifier
- Prints accuracy and classification report
- Saves the trained model as `iris_model.joblib`
- Includes a separate prediction script

## Technologies Used

- Python
- pandas
- scikit-learn
- joblib

## Folder Structure

```text
03_ML_Iris_Classifier/
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
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

## What You Learn

- Loading datasets with scikit-learn
- Splitting data into train and test sets
- Building an ML pipeline
- Scaling features
- Training a classification model
- Evaluating accuracy, precision, recall, and F1 score
- Saving and loading a trained model

## Future Improvements

- Try Random Forest and SVM
- Add confusion matrix plot
- Create a Streamlit web app
- Add user input for custom flower measurements
- Add a Jupyter notebook version

