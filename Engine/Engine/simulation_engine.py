import numpy as np

class SimulationEngine:
    def __init__(self, model, S0, r, sigma, T, n_steps, n_paths):
        self.model = model
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.n_steps = n_steps
        self.n_paths = n_paths

    def simulate(self):
        return self.model.simulate_paths(self.S0, self.r, self.T, self.sigma, self.n_steps, self.n_paths)

    def calculate_payoff(self, paths, K, option_type='call'):
        S_T = paths[:, -1]
        if option_type == 'call':
            return np.maximum(S_T - K, 0)
        elif option_type == 'put':
            return np.maximum(K - S_T, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'") 