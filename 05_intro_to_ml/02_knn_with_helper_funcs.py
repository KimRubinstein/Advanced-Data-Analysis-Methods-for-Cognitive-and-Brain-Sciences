# Importing necessary libraries
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.neighbors
import sklearn.metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# Load data
df = pd.read_csv('penguins.csv')

# Separate the features X from the target y
numerical_features = ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']
X = df[numerical_features]
y = df['species']

# Remove rows with missing values from X and y
X = X.dropna()
y = y[X.index]

# # # optionally: simulate measurement errors by adding random noise to the features
# rng = np.random.default_rng(123) # random number generator
# for col in X.columns:
#     X[col] = X[col] + rng.normal(loc=0, scale=X[col].std()*0.5, size=len(X))

# Split the data into training and test sets
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create a pipeline
pipe = Pipeline([
    ('scaler', sklearn.preprocessing.StandardScaler(with_mean=True, with_std=True)),
    ('knn', sklearn.neighbors.KNeighborsClassifier())
])

# Create parameter grid for GridSearchCV
param_grid = {'knn__n_neighbors': list(range(1, 101))}

# Create GridSearchCV object
grid = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')

# Fit to the data and find best parameters
grid.fit(X_train, y_train)


# Print best parameters
print('Best parameters found by grid search:', grid.best_params_)
best_k = grid.best_params_['knn__n_neighbors']
k_values = grid.cv_results_['param_knn__n_neighbors'].data # just 1:100
k_scores = grid.cv_results_['mean_test_score']

# Plot the average accuracy scores for each K value
plt.plot(k_values, k_scores)
plt.xlabel('K')
plt.ylabel('Validation accuracy')
plt.plot(best_k, np.max(k_scores), 'ro')
plt.annotate(f'k={best_k}', (best_k, np.max(k_scores)), xytext=(12,0), textcoords='offset points', fontsize=22, va='center', ha='left')



# Predict the labels for test data and calculate accuracy
y_test_pred = grid.predict(X_test)
test_accuracy = np.mean(y_test_pred == y_test)
print(f'Test accuracy: {test_accuracy}')

# Plot the confusion matrix
sklearn.metrics.ConfusionMatrixDisplay.from_predictions(
    y_true=y_test, y_pred=y_test_pred,)
plt.show()
