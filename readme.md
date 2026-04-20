✅ 1. Project Folder Structure
ml-container/
│
├── Dockerfile
├── app.py
└── requirements.txt
✅ 2. Simple ML Model Code (app.py)
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
✅ 3. Requirements File (requirements.txt)
scikit-learn


✅ 4. Dockerfile  -->open docker and keep it minimized

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]

✅ 5. Commands to Run (VERY IMPORTANT)

Step 1: Open terminal inside folder

cd mlops_exp_3

Step 2: Build Docker Image

docker build -t ml-model .

Step 3: Run Container

docker run --rm ml-model

✅ Output (Example)
Prediction: [0]