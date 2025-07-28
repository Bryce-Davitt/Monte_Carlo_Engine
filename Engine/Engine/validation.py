import numpy as np

def validate_parameters(S0, r, sigma, T, n_steps, n_paths):
    assert S0 > 0, "Initial price must be positive."
    assert sigma >= 0, "Volatility must be non-negative."
    assert T > 0, "Time to maturity must be positive."
    assert n_steps > 0 and isinstance(n_steps, int), "n_steps must be a positive integer."
    assert n_paths > 0 and isinstance(n_paths, int), "n_paths must be a positive integer."
    assert isinstance(r, (int, float)), "Risk-free rate must be numeric."


def validate_outputs(array):
    assert np.all(np.isfinite(array)), "Output contains non-finite values (NaN or Inf)."
    assert np.all(array >= 0), "Output contains negative values where not expected." 