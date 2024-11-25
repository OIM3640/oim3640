import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some 2D sample data
X_train = np.random.rand(50, 2)
y_train = 2 * X_train[:, 0] - 3 * X_train[:, 1] + 4 + 0.1 * np.random.randn(50)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Generate a grid of points to evaluate the regression plane
x1 = np.linspace(0, 1, 10)  # Range for feature 1
x2 = np.linspace(0, 1, 10)  # Range for feature 2
x1, x2 = np.meshgrid(x1, x2)  # Create a grid
y_plane = model.coef_[0] * x1 + model.coef_[1] * x2 + model.intercept_

# Step 1: Show data points only
fig1 = plt.figure(figsize=(10, 7))
ax1 = fig1.add_subplot(111, projection="3d")

ax1.scatter(
    X_train[:, 0],
    X_train[:, 1],
    y_train,
    c=y_train,
    cmap="viridis",
    s=50,
    label="Data Points",
)
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Target (y)")
ax1.set_title("3D Scatter Plot of Data Points")
ax1.legend()
plt.show()

# Step 2: Show data points with regression plane
fig2 = plt.figure(figsize=(10, 7))
ax2 = fig2.add_subplot(111, projection="3d")

ax2.scatter(
    X_train[:, 0],
    X_train[:, 1],
    y_train,
    c=y_train,
    cmap="viridis",
    s=50,
    label="Data Points",
)
ax2.plot_surface(x1, x2, y_plane, color="orange", alpha=0.5, label="Regression Plane")
ax2.set_xlabel("Feature 1")
ax2.set_ylabel("Feature 2")
ax2.set_zlabel("Target (y)")
ax2.set_title("3D Visualization with Regression Plane")
ax2.legend()
plt.show()
