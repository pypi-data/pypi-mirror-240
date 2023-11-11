from scipy.linalg import svd
from sklearn.utils.extmath import randomized_svd
import numpy as np


def tsvd(A, tol=0):
    U, S, V = svd(A, full_matrices=False)
    i = len(S)
    tol = tol*S[0]
    i = i - np.sum(np.nonzero(S[:i] <= tol))
    
    U = U[:,:i]
    S = S[:i]
    V = V.T[:,:i]
    return U, S, V



def rand_svd(A, tol, n_oversamples, random_state):
    n_components = min(A.shape)
    U, S, V = randomized_svd(A, n_components=n_components, n_oversamples=n_oversamples, random_state=random_state)
    i = len(S)
    tol = tol*S[0]
    i = i - np.sum(np.nonzero(S[:i] <= tol))
    
    U = U[:,:i]
    S = S[:i]
    V = V.T[:,:i]
    return U, S, V