import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)

    # Apply normal equation
    X_transpose = X.T
    w = np.linalg.inv(X_transpose @ X) @ X_transpose @ y
    return list(w)
    pass