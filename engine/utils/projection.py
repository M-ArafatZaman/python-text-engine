import numpy as np

def projection(u: np.array, v: np.array) -> np.array:
    """
    Projection of vector u onto v
    """
    u = np.array(u)
    v = np.array(v)

    return ((np.dot(u, v))/(np.dot(v,v))) * v