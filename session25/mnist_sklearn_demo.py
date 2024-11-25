from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time

# Load MNIST data
print("Loading MNIST data...")
X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)
X = X[:20000]
y = y[:20000]

# Split and scale data
print("Splitting and scaling data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model with progress bar
print("Training model...")
clf = LogisticRegression(max_iter=200)
with tqdm(total=100) as pbar:
    clf.fit(X_train_scaled, y_train)
    for i in range(100):
        pbar.update(1)
        time.sleep(0.02)  # Simulate progress

# Final evaluation
y_pred = clf.predict(X_test_scaled)
print(f"Final Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Display 5 test examples
plt.figure(figsize=(15, 3))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(X_test[i].reshape(28, 28), cmap="gray")
    pred = clf.predict(X_test_scaled[i].reshape(1, -1))[0]
    true = y_test[i]
    plt.title(f"Pred: {pred}\nTrue: {true}")
    plt.axis("off")
plt.tight_layout()
plt.show()
