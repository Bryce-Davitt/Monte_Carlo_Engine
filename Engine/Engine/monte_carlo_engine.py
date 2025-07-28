import numpy as np

class MonteCarloEngine:
    """
    Monte Carlo engine for simulating asset price paths using Geometric Brownian Motion,
    pricing European options, and computing Delta and Gamma Greeks.
    """
    def __init__(self, S0, r, sigma, T, n_steps, n_paths):
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.n_steps = n_steps
        self.n_paths = n_paths
        self.dt = T / n_steps

    def simulate_paths(self, S0=None):
        """
        Simulate asset price paths using Geometric Brownian Motion.
        Args:
            S0 (float, optional): Initial asset price. If None, use self.S0.
        Returns:
            np.ndarray: Simulated asset paths of shape (n_paths, n_steps + 1)
        """
        if S0 is None:
            S0 = self.S0
        dt = self.dt
        paths = np.zeros((self.n_paths, self.n_steps + 1))
        paths[:, 0] = S0
        for t in range(1, self.n_steps + 1):
            z = np.random.standard_normal(self.n_paths)
            paths[:, t] = paths[:, t-1] * np.exp((self.r - 0.5 * self.sigma ** 2) * dt + self.sigma * np.sqrt(dt) * z)
        return paths

    def price_european_option(self, K, option_type='call', S0=None):
        """
        Price a European option using the simulated paths.
        Args:
            K (float): Strike price
            option_type (str): 'call' or 'put'
            S0 (float, optional): Initial asset price. If None, use self.S0.
        Returns:
            float: Estimated option price
        """
        paths = self.simulate_paths(S0)
        S_T = paths[:, -1]
        if option_type == 'call':
            payoffs = np.maximum(S_T - K, 0)
        elif option_type == 'put':
            payoffs = np.maximum(K - S_T, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")
        price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return price

    def compute_delta(self, K, option_type='call', dS=1e-4):
        """
        Compute the Delta Greek using finite differences.
        Args:
            K (float): Strike price
            option_type (str): 'call' or 'put'
            dS (float): Small change in S0 for finite difference
        Returns:
            float: Estimated Delta
        """
        price_up = self.price_european_option(K, option_type, S0=self.S0 + dS)
        price_down = self.price_european_option(K, option_type, S0=self.S0 - dS)
        delta = (price_up - price_down) / (2 * dS)
        return delta

    def compute_gamma(self, K, option_type='call', dS=1e-4):
        """
        Compute the Gamma Greek using finite differences.
        Args:
            K (float): Strike price
            option_type (str): 'call' or 'put'
            dS (float): Small change in S0 for finite difference
        Returns:
            float: Estimated Gamma
        """
        price_up = self.price_european_option(K, option_type, S0=self.S0 + dS)
        price_mid = self.price_european_option(K, option_type, S0=self.S0)
        price_down = self.price_european_option(K, option_type, S0=self.S0 - dS)
        gamma = (price_up - 2 * price_mid + price_down) / (dS ** 2)
        return gamma 