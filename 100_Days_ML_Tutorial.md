# 100 Days Machine Learning Tutorial

Use this as your daily guide. For each day, create a notebook named like `Day_001_Python_Setup.ipynb`, write short notes, code examples, and save your output.

## Setup Before Day 1

Install:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

Optional later:

```bash
pip install tensorflow streamlit xgboost
```

If any package does not install, continue with the others first.

## Days 1-20: Python, Math, and Data Foundations

### Day 1: Python Setup and First Program

Concept: Python is the main language used for ML because it has strong libraries for data, math, and modeling.

Learn:

- Install Python or use Anaconda.
- Open Jupyter Notebook or VS Code.
- Understand cells, scripts, comments, and print output.

Code:

```python
print("Hello Machine Learning")
name = "ML learner"
print(name)
```

Practice: Create variables for your name, age, and goal. Print them in one sentence.

Deliverable: `01_Python_Math/Day_001_Python_Setup.ipynb`

### Day 2: Variables and Data Types

Concept: ML code uses numbers, text, booleans, and collections to represent data.

Learn:

- `int`, `float`, `str`, `bool`
- Type conversion
- Basic arithmetic

Code:

```python
price = 100
discount = 0.2
final_price = price * (1 - discount)
print(final_price)
print(type(final_price))
```

Practice: Calculate BMI from height and weight.

Deliverable: notebook with 10 variable examples.

### Day 3: Conditions and Loops

Concept: Conditions make decisions; loops repeat work. Data cleaning and model evaluation use both.

Learn:

- `if`, `elif`, `else`
- `for` loops
- `while` loops

Code:

```python
marks = [45, 78, 91, 32]
for mark in marks:
    if mark >= 50:
        print("pass")
    else:
        print("fail")
```

Practice: Print all even numbers from 1 to 100.

### Day 4: Functions

Concept: Functions make reusable logic. ML projects should avoid repeating code.

Learn:

- Function definition
- Parameters and return values
- Default arguments

Code:

```python
def accuracy(correct, total):
    return correct / total

print(accuracy(85, 100))
```

Practice: Write a function to calculate mean of a list.

### Day 5: Lists, Tuples, Sets, Dictionaries

Concept: Python collections store groups of values. Dictionaries are common for model configuration.

Learn:

- List indexing and slicing
- Dictionary keys and values
- Set uniqueness

Code:

```python
student = {"name": "Aman", "score": 88}
print(student["score"])
```

Practice: Store 5 students and their scores, then print the highest score.

### Day 6: File Handling and Exceptions

Concept: Real projects read data from files and handle errors safely.

Learn:

- Read and write text files
- `try` and `except`
- File paths

Code:

```python
try:
    with open("notes.txt", "w") as f:
        f.write("Starting ML journey")
except Exception as e:
    print(e)
```

Practice: Create a text file containing your 100-day goals.

### Day 7: NumPy Arrays

Concept: NumPy gives fast numerical arrays. Most ML libraries are built around array operations.

Learn:

- Create arrays
- Shape and dimension
- Indexing arrays

Code:

```python
import numpy as np

x = np.array([1, 2, 3, 4])
print(x.mean())
print(x.shape)
```

Practice: Create an array of 10 numbers and calculate mean, max, min.

### Day 8: NumPy Operations

Concept: Vectorized operations are faster and cleaner than loops.

Learn:

- Element-wise operations
- Broadcasting
- Matrix multiplication

Code:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(a * b)
```

Practice: Normalize an array using `(x - mean) / std`.

### Day 9: Pandas Series and DataFrame

Concept: Pandas is used to load, inspect, clean, and transform tabular data.

Learn:

- Series
- DataFrame
- `head`, `info`, `describe`

Code:

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "score": [80, 90, 75]
})
print(df.head())
print(df.describe())
```

Practice: Create a DataFrame for 5 people with age and salary.

### Day 10: Pandas Cleaning Basics

Concept: Raw data is messy. Cleaning is one of the most important ML skills.

Learn:

- Missing values
- Duplicate rows
- Rename columns
- Filter rows

Code:

```python
df = df.drop_duplicates()
df = df.rename(columns={"score": "exam_score"})
```

Practice: Create a DataFrame with missing values and fill them.

### Day 11: Matplotlib Basics

Concept: Visualization helps you understand patterns before modeling.

Learn:

- Line plot
- Bar plot
- Scatter plot
- Labels and title

Code:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
plt.plot(x, y)
plt.title("Simple line")
plt.show()
```

Practice: Plot marks of 5 students.

### Day 12: Seaborn Basics

Concept: Seaborn makes statistical plots easier and cleaner.

Learn:

- Histogram
- Boxplot
- Countplot
- Heatmap

Code:

```python
import seaborn as sns

tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"])
```

Practice: Plot relationship between total bill and tip.

### Day 13: Statistics Basics

Concept: Statistics helps you summarize and reason about data.

Learn:

- Mean, median, mode
- Variance and standard deviation
- Percentiles

Code:

```python
import numpy as np

values = np.array([10, 20, 30, 40, 100])
print(values.mean())
print(np.median(values))
print(values.std())
```

Practice: Explain why median can be better than mean when outliers exist.

### Day 14: Probability Basics

Concept: ML predictions are often probabilistic.

Learn:

- Probability
- Conditional probability
- Random variables
- Distribution intuition

Code:

```python
import random

heads = 0
for _ in range(1000):
    if random.choice(["H", "T"]) == "H":
        heads += 1
print(heads / 1000)
```

Practice: Simulate rolling a dice 1000 times.

### Day 15: Linear Algebra Basics

Concept: Data is represented as vectors and matrices in ML.

Learn:

- Vector
- Matrix
- Dot product
- Matrix shape

Code:

```python
import numpy as np

x = np.array([1, 2])
w = np.array([0.5, 1.5])
print(np.dot(x, w))
```

Practice: Multiply a 2x2 matrix with a vector.

### Day 16: Calculus and Gradient Intuition

Concept: Models learn by reducing error. Gradients tell the model how to change.

Learn:

- Slope
- Loss function
- Gradient descent idea

Code:

```python
x = 2
learning_rate = 0.1
gradient = 2 * x
x = x - learning_rate * gradient
print(x)
```

Practice: Write in your own words how gradient descent improves a model.

### Day 17: Data Preprocessing Overview

Concept: Preprocessing prepares raw data for algorithms.

Learn:

- Cleaning
- Encoding
- Scaling
- Splitting features and target

Code:

```python
X = df[["age", "salary"]]
y = df["purchased"]
```

Practice: Choose features and target from a sample dataset.

### Day 18: Train Test Split and Validation

Concept: You need unseen test data to estimate real performance.

Learn:

- Training data
- Testing data
- Validation data
- Random state

Code:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Practice: Split any small dataset into train and test sets.

### Day 19: Mini Project - Student Score Analysis

Concept: Combine Python, Pandas, stats, and plots.

Task:

- Create or download a student scores dataset.
- Clean missing values.
- Calculate average marks.
- Plot score distribution.
- Find top 5 students.

Deliverable: A notebook with analysis and 5 written insights.

### Day 20: Revision

Concept: Revision converts learning into memory.

Task:

- Recode NumPy examples without looking.
- Recode Pandas cleaning examples.
- Explain mean, standard deviation, train-test split.
- Update progress tracker.

## Days 21-40: Data Analysis and ML Workflow

### Day 21: EDA Workflow

Concept: Exploratory Data Analysis means understanding data before modeling.

Checklist:

- Shape
- Column types
- Missing values
- Duplicates
- Target distribution
- Feature relationships

Practice: Run this checklist on Titanic or Iris dataset.

### Day 22: Missing Values

Concept: Missing values can break models or create bias.

Learn:

- Drop missing values
- Fill with mean, median, mode
- Add missing indicator

Code:

```python
df["age"] = df["age"].fillna(df["age"].median())
```

Practice: Try two filling strategies and compare results.

### Day 23: Outliers

Concept: Outliers are unusual values that can distort models.

Learn:

- Boxplot
- IQR method
- Z-score idea

Practice: Detect outliers in a salary column and decide whether to keep them.

### Day 24: Encoding Categorical Data

Concept: Most ML models need numbers, not text categories.

Learn:

- One-hot encoding
- Label encoding
- Ordinal encoding

Code:

```python
pd.get_dummies(df, columns=["city"], drop_first=True)
```

Practice: Encode a column with city names.

### Day 25: Feature Scaling

Concept: Scaling makes numeric features comparable.

Learn:

- StandardScaler
- MinMaxScaler
- When scaling matters

Code:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Practice: Scale age and salary columns.

### Day 26: Feature Engineering

Concept: Better features often improve models more than better algorithms.

Examples:

- Age group from age
- Price per room
- Text length
- Date parts

Practice: Create 3 new useful features from any dataset.

### Day 27: Correlation and Covariance

Concept: Correlation measures linear relationship between variables.

Code:

```python
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
```

Practice: Find which features correlate most with target.

### Day 28: Visualization for Insights

Concept: Good plots answer questions.

Use:

- Histogram for distribution
- Boxplot for outliers
- Scatter plot for relationships
- Countplot for categories

Practice: Create 6 plots from one dataset and write insights.

### Day 29: Data Leakage

Concept: Leakage happens when training data contains information unavailable in real prediction.

Examples:

- Using future data
- Scaling before train-test split
- Including target-like columns

Practice: Write 3 leakage examples in your notes.

### Day 30: Scikit-learn Workflow

Concept: Scikit-learn gives a consistent API: create model, fit, predict, evaluate.

Code:

```python
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

Practice: Train any simple model using this pattern.

### Day 31: Supervised vs Unsupervised Learning

Concept:

- Supervised learning uses labels.
- Unsupervised learning finds patterns without labels.

Practice:

- Classification example
- Regression example
- Clustering example

### Day 32: Regression Metrics

Concept: Regression predicts continuous values.

Learn:

- MAE
- MSE
- RMSE
- R2 score

Code:

```python
from sklearn.metrics import mean_absolute_error, r2_score

print(mean_absolute_error(y_test, pred))
print(r2_score(y_test, pred))
```

### Day 33: Classification Metrics

Concept: Accuracy is not always enough.

Learn:

- Confusion matrix
- Precision
- Recall
- F1 score

Code:

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, pred))
```

### Day 34: Bias Variance Tradeoff

Concept:

- High bias: model is too simple.
- High variance: model memorizes training data.

Practice: Compare a shallow tree and deep tree.

### Day 35: Cross Validation

Concept: Cross validation evaluates a model across multiple splits.

Code:

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(scores.mean())
```

### Day 36: Pipelines

Concept: Pipelines combine preprocessing and modeling safely.

Code:

```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", model)
])
```

Practice: Build a pipeline with scaler and classifier.

### Day 37: Model Persistence

Concept: Save trained models for later use.

Code:

```python
import joblib

joblib.dump(model, "model.pkl")
loaded_model = joblib.load("model.pkl")
```

Practice: Save and reload a trained model.

### Day 38: EDA Mini Project

Task: Choose a dataset and create a full EDA notebook.

Required:

- Data overview
- Cleaning
- 8 plots
- 10 insights
- Final summary

### Day 39: Clean ML Dataset Project

Task: Take a messy dataset and prepare it for ML.

Required:

- Handle missing values
- Encode categories
- Scale numeric features
- Split train and test

### Day 40: Revision

Task:

- Revise EDA checklist.
- Revise preprocessing.
- Rebuild a pipeline.
- Update tracker.

## Days 41-65: Machine Learning Algorithms

### Day 41: Linear Regression Theory

Concept: Linear regression predicts a number using a weighted sum of features.

Formula:

```text
y = w1*x1 + w2*x2 + b
```

Practice: Explain weight and bias in your own words.

### Day 42: Linear Regression Practice

Code:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

Practice: Predict house prices or student marks.

### Day 43: Polynomial Regression

Concept: Polynomial features allow curved relationships.

Practice: Compare linear and polynomial regression on curved data.

### Day 44: Ridge and Lasso Regression

Concept: Regularization reduces overfitting.

Learn:

- Ridge shrinks weights.
- Lasso can make some weights zero.

Practice: Compare LinearRegression, Ridge, and Lasso.

### Day 45: Logistic Regression Theory

Concept: Logistic regression predicts class probability.

Use cases:

- Spam or not spam
- Churn or not churn
- Disease or no disease

### Day 46: Logistic Regression Practice

Code:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

Practice: Train on Iris or Titanic dataset.

### Day 47: K-Nearest Neighbors

Concept: KNN predicts using nearby examples.

Important:

- Needs scaling
- Simple but can be slow
- `k` controls smoothness

Practice: Try `k=3`, `k=5`, `k=9`.

### Day 48: Naive Bayes

Concept: Naive Bayes is useful for text classification and simple probabilistic classification.

Practice: Build a spam classifier with `MultinomialNB`.

### Day 49: Decision Tree

Concept: A decision tree splits data with rules.

Practice:

- Train a tree.
- Plot tree.
- Change `max_depth`.

### Day 50: Random Forest

Concept: Random forest combines many decision trees to reduce overfitting.

Practice: Compare tree vs forest accuracy.

### Day 51: Gradient Boosting

Concept: Boosting builds models sequentially, each correcting previous errors.

Practice: Use `GradientBoostingClassifier` or `GradientBoostingRegressor`.

### Day 52: XGBoost or HistGradientBoosting

Concept: Advanced boosting is very strong for tabular data.

Practice:

- If XGBoost is installed, use it.
- Otherwise use sklearn `HistGradientBoostingClassifier`.

### Day 53: Support Vector Machine

Concept: SVM finds a boundary with maximum margin.

Important:

- Scaling is important.
- Kernels help with nonlinear patterns.

Practice: Try linear and RBF kernels.

### Day 54: K-Means Clustering

Concept: K-means groups similar rows into clusters.

Practice:

- Cluster customer data.
- Try different `k`.
- Plot clusters.

### Day 55: Hierarchical Clustering

Concept: Hierarchical clustering builds a tree of clusters.

Practice: Create a dendrogram for a small dataset.

### Day 56: PCA

Concept: PCA reduces dimensions while preserving important variation.

Practice:

- Reduce features to 2 components.
- Plot the result.

### Day 57: Imbalanced Data

Concept: When one class is rare, accuracy can mislead.

Learn:

- Class imbalance
- Precision and recall
- Class weights
- Oversampling idea

Practice: Evaluate using F1 score.

### Day 58: Hyperparameter Tuning

Concept: Hyperparameters are settings chosen before training.

Code:

```python
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(model, param_grid, cv=5)
grid.fit(X_train, y_train)
```

Practice: Tune random forest depth and number of trees.

### Day 59: Model Interpretation

Concept: You should understand why a model predicts something.

Learn:

- Feature importance
- Coefficients
- Permutation importance

Practice: Show top 10 important features.

### Day 60: End-to-End ML Project 1

Project: House price prediction.

Steps:

- Load data
- Clean data
- EDA
- Train regression models
- Compare metrics
- Save best model

### Day 61: Improve Project 1

Task:

- Add feature engineering.
- Add cross validation.
- Add README.
- Explain model result clearly.

### Day 62: End-to-End ML Project 2

Project: Customer churn classification.

Steps:

- Clean data
- Encode categories
- Train classification models
- Compare F1 score
- Explain business meaning

### Day 63: Improve Project 2

Task:

- Tune hyperparameters.
- Handle imbalance.
- Add confusion matrix.
- Save model.

### Day 64: ML Revision

Task: Create a table comparing all algorithms.

Columns:

- Algorithm
- Task type
- Needs scaling?
- Handles nonlinear data?
- Pros
- Cons

### Day 65: ML Interview Questions

Practice answering:

- What is overfitting?
- What is cross validation?
- Precision vs recall?
- Why scale features?
- Random forest vs boosting?

## Days 66-80: Deep Learning

### Day 66: Neural Network Intuition

Concept: Neural networks learn layers of transformations from input to output.

Learn:

- Neuron
- Weight
- Bias
- Layer
- Activation

### Day 67: TensorFlow or PyTorch Setup

Choose one:

- TensorFlow/Keras is beginner friendly.
- PyTorch is popular for research and custom work.

Keras example:

```python
import tensorflow as tf
print(tf.__version__)
```

### Day 68: First Neural Network

Code:

```python
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
```

Practice: Train a small classifier.

### Day 69: Activation and Loss Functions

Concept:

- ReLU helps hidden layers learn nonlinear patterns.
- Sigmoid is common for binary classification.
- Softmax is common for multiclass classification.
- Loss measures model error.

### Day 70: Backpropagation Intuition

Concept: Backpropagation calculates how each weight contributed to error.

Practice: Draw a small network and explain how error flows backward.

### Day 71: Training Deep Networks

Learn:

- Epoch
- Batch size
- Learning rate
- Optimizer

Practice: Train the same model with different batch sizes.

### Day 72: Regularization

Concept: Regularization helps prevent overfitting.

Learn:

- Dropout
- Early stopping
- Batch normalization

Practice: Add early stopping to a neural network.

### Day 73: CNN Intuition

Concept: CNNs learn image features using filters.

Learn:

- Convolution
- Pooling
- Flatten
- Dense layer

### Day 74: CNN Image Classifier

Practice:

- Use MNIST or Fashion MNIST.
- Train a CNN.
- Plot accuracy and loss.

### Day 75: Transfer Learning

Concept: Use a pretrained model and adapt it to your dataset.

Practice: Use MobileNetV2 or ResNet for image classification.

### Day 76: NLP Text Preprocessing

Concept: Text must be converted into numbers.

Learn:

- Lowercase
- Remove punctuation
- Tokenization
- Stop words
- Vectorization

### Day 77: Text Classification

Practice:

- Build spam detection.
- Use `TfidfVectorizer`.
- Train Logistic Regression or Naive Bayes.

### Day 78: Embeddings Basics

Concept: Embeddings represent words as dense numeric vectors.

Practice: Learn the difference between one-hot encoding, TF-IDF, and embeddings.

### Day 79: Time Series Basics

Concept: Time series data has order and trends.

Learn:

- Trend
- Seasonality
- Lag features
- Rolling average

Practice: Create lag features from a date-based dataset.

### Day 80: Deep Learning Mini Project

Choose one:

- Digit classifier
- Image classifier
- Sentiment classifier

Deliverable: Notebook with model, metrics, plots, and explanation.

## Days 81-95: Portfolio Projects

### Day 81: Project 1 - House Price Prediction

Build a complete regression project.

Required files:

- Notebook
- Saved model
- README
- Metrics

### Day 82: Project 2 - Customer Churn

Build a classification project that predicts whether a customer may leave.

Focus:

- Business explanation
- Recall and precision
- Confusion matrix

### Day 83: Project 3 - Spam Detection

Build a text classification project.

Focus:

- Text preprocessing
- TF-IDF
- Naive Bayes or Logistic Regression

### Day 84: Project 4 - Recommendation System

Build a simple recommendation system.

Options:

- Popularity based
- Content based
- Collaborative filtering basics

### Day 85: Project 5 - Image Classification

Build an image classifier using CNN or transfer learning.

Focus:

- Data loading
- Training curve
- Confusion matrix
- Sample predictions

### Day 86: Deployment Basics

Concept: Deployment means making your model usable by others.

Learn:

- Input form
- Prediction function
- Saved model
- Simple web app

### Day 87: Streamlit App

Practice:

```python
import streamlit as st

st.title("ML Prediction App")
value = st.number_input("Enter value")
st.write(value)
```

Task: Create a small app for one project.

### Day 88: Model API Basics

Concept: APIs allow other programs to use your model.

Learn:

- Request
- Response
- JSON
- FastAPI idea

Practice: Write pseudo-code for a prediction API.

### Day 89: Git and GitHub for ML

Learn:

- Repository
- Commit
- README
- `.gitignore`
- Uploading notebooks

Practice: Create GitHub repo for one project.

### Day 90: Write Project README

Every ML README should include:

- Problem statement
- Dataset
- Approach
- Models tried
- Metrics
- How to run
- Result

### Day 91: Portfolio Cleanup 1

Clean project notebooks:

- Remove unnecessary cells.
- Add headings.
- Add comments.
- Keep outputs meaningful.

### Day 92: Portfolio Cleanup 2

Improve visualizations:

- Clear titles
- Axis labels
- Consistent colors
- Insight after each important plot

### Day 93: Portfolio Cleanup 3

Improve model explanation:

- Why this model?
- What metric matters?
- What are limitations?
- What can improve next?

### Day 94: Case Study Practice

Choose one business problem and design an ML solution.

Example: A bank wants to reduce loan default.

Write:

- Objective
- Data needed
- Target variable
- Metrics
- Risks

### Day 95: Mock Interview Project Explanation

Practice explaining one project in 2 minutes:

- Problem
- Data
- Cleaning
- Model
- Metric
- Result
- Next improvement

## Days 96-100: Revision and Next Steps

### Day 96: Revise Statistics

Revise:

- Mean, median, mode
- Variance, standard deviation
- Probability
- Correlation
- Distribution

Task: Write 20 short Q&A notes.

### Day 97: Revise ML Algorithms

Revise:

- Linear regression
- Logistic regression
- KNN
- Naive Bayes
- Tree
- Random forest
- Boosting
- SVM
- K-means
- PCA

Task: Make a comparison table.

### Day 98: Revise Deep Learning

Revise:

- Neural network
- Activation
- Loss
- Optimizer
- CNN
- Transfer learning
- NLP vectorization

Task: Explain each in simple language.

### Day 99: Final Portfolio Polish

Task:

- Choose best 3 projects.
- Make README files strong.
- Add screenshots or plots.
- Check notebooks run from top to bottom.

### Day 100: Final Review and Next Roadmap

Task:

- Write what you learned.
- List weak topics.
- Plan next 30 days.

Next roadmap options:

- Advanced ML
- Deep learning specialization
- MLOps
- NLP
- Computer vision
- Kaggle practice

## Best Free Dataset Sources

- Kaggle datasets
- UCI Machine Learning Repository
- Scikit-learn built-in datasets
- Google Dataset Search

## Recommended Beginner Datasets

- Iris
- Titanic
- House Prices
- Breast Cancer Wisconsin
- MNIST
- Fashion MNIST
- SMS Spam Collection

## Final Rule

Do not only watch tutorials. For every concept, write code, break it, fix it, and explain it in your own words.

