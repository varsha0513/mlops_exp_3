from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load data
X, y = load_iris(return_X_y=True)

# Train model
model = LogisticRegression(max_iter=100)
model.fit(X, y)

# Predict first sample
prediction = model.predict([X[0]])

print("Prediction:", prediction)