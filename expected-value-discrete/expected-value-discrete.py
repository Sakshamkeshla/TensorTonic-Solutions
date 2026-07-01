import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)

    s = np.sum(p)
    if not np.allclose(1.0,s) :
        raise ValueError("within tolerance 10−6")

    return np.sum(x*p)
    pass
