# Importing necessary libraries
# note that sklearn is installed using pip install scikit-learn
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.neighbors
import sklearn.metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Information about the data: https://allisonhorst.github.io/palmerpenguins
df = pd.read_csv('penguins.csv')

print(df.head())
print(df.describe())

numerical_features = ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']

# Assuming you have a DataFrame `df` with your data
# Separate the features X from the target y
X = df[numerical_features]
y = df['species']

# remove rows with missing values from X and y
X = X.dropna()
y = y[X.index] # we use X's index to keep the same rows in X and y

# # # optionally: simulate measurement errors by adding random noise to the features
# rng = np.random.default_rng(123) # random number generator
# for col in X.columns:
#     X[col] = X[col] + rng.normal(loc=0, scale=X[col].std()*0.5, size=len(X))

# Split the data into training and test sets
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y,
    test_size=0.2, # (80% train, 20% test)
    random_state=42, # changing this random state will change the split
    stratify=y # we'd like to have the same proportion of positive and negative samples in train and test
    )

# Before we start, let's just check the proportion of the different classes in the training and test sets
print('Proportion of different classes in the training set:')
print(y_train.value_counts(normalize=True))
print('Proportion of different classes in the test set:')
print(y_test.value_counts(normalize=True))

# What would be the accuracy of a classifier that always predicts the majority class in the training set?

# Now, let's train a KNN classifier and evaluate it on the test set

# Data preprocessing

# Like most ML algorithms, KNN works better if the features are on the same scale
# Create a scaler for the numerical features (z = (x - u) / s)
scaler = sklearn.preprocessing.StandardScaler(with_mean=True, with_std=True)
# we can turn off centering or scaling to demonstrate their effect
# do we really need to center the data? what if we don't center it?

# Fit the scaler on the training data and transform the training, validation and test data
X_train_transformed = scaler.fit_transform(X_train) # fit u and s on X_train, then transform X_train
X_test_transformed = scaler.transform(X_test) # transform X_test using the u and s from X_train.
# Note that we don't fit the scaler on X_test, we only transform it. X_test is our holdout set, we don't want to peek into it.


# Hyperparameter tuning with grid search and k-fold cross validation.

# List of potential K values for KNN
k_values = list(range(1, 101)) # we are going to grid search over these values

# Empty list to store average accuracy scores for each K value
k_scores = []

# Split the training set into five folds (setting aside 20% of the training data for validation at each iteration)
kfold = sklearn.model_selection.StratifiedKFold(
    n_splits=5,
    shuffle=True, # shuffle means that the data will be shuffled before splitting into folds
    random_state=123)
# We will reuse this kfold object for each potential K value

# Loop over k_values to find the one with the highest cross-validated score
for k in k_values:
    fold_scores = []

    # Instantiate a KNN classifier with current K value
    knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=k) # it still doesn't know anything about the data

    # Perform 5-fold cross validation
    for train_index, val_index in kfold.split(X_train_transformed, y_train):
        # Split the data
        kfold_X_train, kfold_X_val = X_train_transformed[train_index], X_train_transformed[val_index]
        kfold_y_train, kfold_y_val = y_train.iloc[train_index], y_train.iloc[val_index]

        # Fit the KNN classifier
        knn.fit(kfold_X_train, kfold_y_train)

        # Predict the labels for validation data and calculate accuracy
        y_pred = knn.predict(kfold_X_val)
        accuracy = np.sum(y_pred == kfold_y_val) / len(kfold_y_val)

        # Append to fold_scores list
        fold_scores.append(accuracy)

    # Calculate the mean score for the current K value and append to k_scores list
    k_scores.append(np.mean(fold_scores))


# The best K value is the one that gives the highest score
best_k = k_values[np.argmax(k_scores)]
print(f'Best K value: {best_k}')

# Plot the average accuracy scores for each K value
plt.plot(k_values, k_scores)
plt.xlabel('K')
plt.ylabel('Validation accuracy')
plt.plot(best_k, np.max(k_scores), 'ro')
plt.annotate(f'k={best_k}', (best_k, np.max(k_scores)), xytext=(12,0), textcoords='offset points', fontsize=22, va='center', ha='left')

# Set the best K value in the classifier and fit it to the entire training data
knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train_transformed, y_train)

# Predict the labels for test data and calculate accuracy
y_test_pred = knn.predict(X_test_transformed)
test_accuracy = np.sum(y_test_pred == y_test) / len(y_test)
print(f'Test accuracy: {test_accuracy}')

# Plot the confusion matrix
sklearn.metrics.ConfusionMatrixDisplay.from_predictions(
    y_true=y_test, y_pred=y_test_pred,
)
plt.show()