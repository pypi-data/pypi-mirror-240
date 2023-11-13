import numpy as np
from scipy.linalg import svd, toeplitz
from statsmodels.tsa.stattools import acf
from scipy.stats import entropy, zscore

def JSD(p):
    """
        Calculates the normalized Jensen-Shannon divergence against the uniform distribution
        Input: 
            - p = probaility distribution
        Output:
            - Jensen divergence (JSD)
    """
    n = len(p)
    q = np.ones(n)/n # Uniform reference
    m = (p + q) / 2
    jensen0 = -2*((((n+1)/n)*np.log(n+1)-2*np.log(2*n) + np.log(n))**(-1))
    return jensen0*(entropy(p, m) + entropy(q, m)) / 2

def index(x, lag):
    """
        Ecoacoustics Global Complexity Index (EGCI) package
        
        Inputs:
            - x = the input signal, it must be a one-dimensional np.ndarray()
            - lag = time lag for autocorrelation, it must be one of the following values [64, 128, 256, 512]

        Outputs:
            - EGCI = aka complexity
            - Entropy = The normalized John von Neumann entropy
            - Divergence = The normalized Jensen-Shannon divergence
    """

    assert isinstance(x, np.ndarray), "the input signal must be a one-dimensional np.ndarray()"
    assert x.ndim == 1, "the input signal must be a one-dimensional np.ndarray()"
    assert np.std(x) > np.finfo(np.float32).eps, "the signal variance is too small"
    assert lag < len(x)/2, "the time lag cannot be greater than half the length of the input vector"
    assert lag in set([64, 128, 256, 512, 1024]), "the time lag must be in the set [64, 128, 256, 512]"

    x = zscore(x)                                           # z-score normalization
    
    # Algorithm steps 
    rxx = acf(x, nlags=lag, fft=True)
    _, s, _ = svd(toeplitz(rxx))
    s = s/np.sum(s)                                         # Probaility Distribution
    
    normalized_entropy = entropy(s)/np.log(lag)        # Normalized Entropy
    normalized_divergence = JSD(s)                     # Normalized Jensen-Shannon divergence
    complexity = normalized_entropy * normalized_divergence # Complexity, also called EGCI index

    return complexity, normalized_entropy, normalized_divergence



def boundaries(n_bins):
    """
        Returns the upper and lower boundaries for HxC plot

    """
    assert n_bins in set([64, 128, 256, 512, 1024]), "the n_bins (aka time lag) must be in the set [64, 128, 256, 512]"

    resolution = 100
    prob = resolution*np.ones(int(n_bins))
    log_n_bins = np.log(n_bins)
    H = []
    C = []

    # loop to go from equiprobability to certainty (usign inverse order)
    for i in range(n_bins-1):   
        n = prob[i]
        for _ in range(int(n)):
            p = prob/sum(prob)
            h = entropy(p)/log_n_bins
            H.append(h)
            C.append(h * JSD(p))
            prob[i] = prob[i] - 1

    p = prob/sum(prob)
    h = entropy(p)/log_n_bins
    H.append(h)
    C.append(h * JSD(p))

    # loop to go from certainty to equiprobability
    prob = np.zeros(int(n_bins))
    resolution = 100*resolution
    prob[0] = resolution
    for _ in range(resolution):
        prob[1:n_bins] = prob[1:n_bins] + 1
        p = prob/sum(prob)
        h = entropy(p)/log_n_bins
        H.append(h)
        C.append(h * JSD(p))

    return C, H
